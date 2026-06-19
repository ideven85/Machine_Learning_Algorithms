import functools
import matplotlib.pyplot as plt
import numpy as np
import pickle

import dist
import util
from plotting import plot_points, animate

from mdp import MDP, TabularQ, sim_episode, evaluate

# to run stand-alone, import these instead of mdp:
# from mdp_solutions import *
# from nnq import *


class NoExit(MDP):
    # Like breakout or pong, but one player, no walls to break out, no
    # way to win You can move paddle vertically up or down or stay
    actions = (+1, 0, -1)

    def __init__(self, field_size, ball_speed=1, random_start=True):
        # image space is n by n
        self.q = None
        self.n = field_size
        h = self.n * ball_speed
        self.discount_factor = (h - 1.0) / h
        self.ball_speed = ball_speed

        # state space is: ball position and velocity, paddle position
        # and velocity
        # - ball position is n by n
        # - ball velocity is one of (-1, -1), (-1, 1), (0, -1), (0, 1),
        #                          (1, -1), (1, 1)
        # - paddle position is n; this is location of bottom of paddle,
        #    can stick "up" out of the screen
        # - paddle velocity is one of 1, 0, -1
        self.states = [
            ((br, bc), (brv, bcv), pp, pv)
            for br in range(self.n)
            for bc in range(self.n)
            for brv in (-1, 0, 1)
            for bcv in (-1, 1)
            for pp in range(self.n)
            for pv in (-1, 0, 1)
        ]
        self.states.append("over")
        self.start = (
            dist.uniform_dist([((br, 0), (0, 1), 0, 0) for br in range(self.n)])
            if random_start
            else dist.delta_dist(((int(self.n / 2), 0), (0, 1), 0, 0))
        )

    ax = None
    ims = None

    # Updating values in google colab
    try:
        from google.colab import widgets

        IS_COLAB = True
        grid = widgets.Grid(1, 10, header_row=False, header_column=False)
        parity = 0
    except:
        IS_COLAB = False
        grid = None

    def draw_state(self, state=None, pause=False):

        def _update(self, state, pause):
            if self.ax is None or self.IS_COLAB:
                plt.ion()
                plt.figure(facecolor="white")
                self.ax = plt.subplot()

            if state is None:
                state = self.state
            ((br, bc), (brv, bcv), pp, pv) = state
            im = np.zeros((self.n, self.n + 1))
            im[br, bc] = -1
            im[pp, self.n] = 1
            self.ax.cla()
            self.ims = self.ax.imshow(
                im,
                interpolation="none",
                cmap="viridis",
                extent=[-0.5, self.n + 0.5, -0.5, self.n - 0.5],
                animated=True,
            )
            self.ims.set_clim(-1, 1)
            plt.pause(0.0001)
            if pause:
                input("go?")
            else:
                plt.pause(0.1 if self.IS_COLAB else 0.01)

        if self.IS_COLAB:
            with self.grid.output_to(0, (self.parity % 10)):
                # _update(self, state, pause)
                self.grid.clear_cell(0, (self.parity + 1) % 10)
                self.parity = (self.parity + 9) % 10
        else:
            _update(self, state, pause)

    def state2vec(self, s):
        if s == "over":
            return np.array([[0, 0, 0, 0, 0, 0, 1]])
        ((br, bc), (brv, bcv), pp, pv) = s
        return np.array([[br, bc, brv, bcv, pp, pv, 0]])

    def terminal(self, state):
        return state == "over"

    def reward_fn(self, s, a):
        return 0 if s == "over" else 1

    def greedy(self, s):
        return argmax(self.actions, lambda a: self.q.get(s, a))

    def transition_model(self, s, a, p=0.4):
        # Only randomness is in brv and brc after a bounce
        # 1- prob of negating nominal velocity
        if s == "over":
            return dist.delta_dist("over")

        # Current state
        ((br, bc), (brv, bcv), pp, pv) = s

        # Nominal next ball state
        new_br = br + self.ball_speed * brv
        new_brv = brv
        new_bc = bc + self.ball_speed * bcv
        new_bcv = bcv

        # nominal paddle state, a is action (-1, 0, 1)
        new_pp = max(0, min(self.n - 1, pp + a))
        new_pv = a
        new_s = None
        hit_r = hit_c = False

        # bottom, top contacts
        if new_br < 0:
            new_br = 0
            new_brv = 1
            hit_r = True
        elif new_br >= self.n:
            new_br = self.n - 1
            new_brv = -1
            hit_r = True

        # back, front contacts
        if new_bc < 0:  # back bounce
            new_bc = 0
            new_bcv = 1
            hit_c = True
        elif new_bc >= self.n:
            if self.paddle_hit(pp, new_pp, br, bc, new_br, new_bc):
                new_bc = self.n - 1
                new_bcv = -1
                hit_c = True
            else:
                return dist.delta_dist("over")

        new_s = ((new_br, new_bc), (new_brv, new_bcv), new_pp, new_pv)
        if (not hit_c) and (not hit_r):
            return dist.delta_dist(new_s)
        elif hit_c:  # also hit_c and hit_r
            if abs(new_brv) > 0:
                return dist.DDist(
                    {
                        new_s: p,
                        ((new_br, new_bc), (-new_brv, new_bcv), new_pp, new_pv): 1 - p,
                    }
                )
            else:
                return dist.DDist(
                    {
                        new_s: p,
                        ((new_br, new_bc), (-1, new_bcv), new_pp, new_pv): 0.5
                        * (1 - p),
                        ((new_br, new_bc), (1, new_bcv), new_pp, new_pv): 0.5 * (1 - p),
                    }
                )
        elif hit_r:
            return dist.DDist(
                {
                    new_s: p,
                    ((new_br, new_bc), (new_brv, -new_bcv), new_pp, new_pv): 1 - p,
                }
            )

    def paddle_hit(self, pp, new_pp, br, bc, new_br, new_bc):
        # Being generous to paddle, any overlap in row
        prset = set(range(pp, pp + 2)).union(set(range(new_pp, new_pp + 2)))
        brset = set([br, br + 1, new_br, new_br + 1])
        return len(prset.intersection(brset)) >= 2


##############################


def test_learn_play(
    d=5,
    num_layers=2,
    num_units=100,
    eps=0.5,
    iters=10_000,
    draw=False,
    tabular=True,
    batch=False,
    batch_epochs=10,
    num_episodes=10,
    episode_length=100,
    nnq_lr=3e-3,
):
    iters_per_value = 1 if iters <= 10 else int(iters / 10)
    scores = []

    game = NoExit(d)
    if game.q is None:
        if tabular:
            game.q = TabularQ(game.states, game.actions)
        else:
            game.q = NNQ(
                game.states,
                game.actions,
                game.state2vec,
                num_layers,
                num_units,
                epochs=batch_epochs if batch else 1,
                lr=nnq_lr,
            )

    def interact(iter=0, s=None, a=None, r=None):
        if iter % iters_per_value == 0:
            scores.append(
                (iter, evaluate(game, game.greedy, num_episodes, episode_length)[0])
            )
            print("score", scores[-1], flush=True)

    # learn the game
    if batch:
        Q_learn_batch(
            game,
            iters=iters + 1,
            eps=eps,
            episode_length=100,
            n_episodes=10,
            interactive_fn=interact,
        )
    else:
        Q_learn(game, iters=iters + 1, eps=eps, interactive_fn=interact)

    if scores:
        print("Plotting learning curve")
        x_scores, y_length = (
            np.array([s[0] for s in scores]),
            np.array([s[1] for s in scores]),
        )
        ax = plot_points(x_scores, y_length, style="ro-")
        # Plot the running mean to smooth the learning curve
        plot_points(
            x_scores,
            np.cumsum(y_length) / np.arange(1, len(y_length) + 1),
            style="bx-",
            ax=ax,
        )
        plt.show()

    # play the game using greedy policy
    print("simulating episodes to play the game...", flush=True)
    rewards = []
    for i in range(num_episodes):
        reward, _, animation = sim_episode(
            game,
            game.greedy,
            episode_length,
            draw=(i == (num_episodes - 1)),
            animate=animate,
        )
        print("Reward", reward)
        rewards.append(reward)

    print("String to upload (incude quotes):")
    print(f'"{to_hex(pickle.dumps([tabular, batch, scores, rewards], 0).decode())}"')

    return animation


def to_hex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace("0x", "")
        if len(hv) == 1:
            hv = "0" + hv
        lst.append(hv)
    return functools.reduce(lambda x, y: x + y, lst)


def test_solve_play(d=5, draw=False, num_episodes=10, episode_length=100):
    """Use value_iteration to optimally 'solve' the game, then play it"""
    game = NoExit(d)
    game.q = TabularQ(game.states, game.actions)

    # solve the game
    value_iteration(game)

    # print(f"{game.q=}") #DEBUG
    # return

    # play the game using greedy policy
    print("simulating episodes to play the game...")
    for i in range(num_episodes):
        reward, _, animation = sim_episode(
            game,
            game.greedy,
            episode_length,
            draw=(i == (num_episodes - 1)),
            animate=animate,
        )
        print("Reward", reward)
    return animation


##########   Test cases


def try_value_iteration(d=5, draw=True, num_episodes=1, episode_length=100):
    return test_solve_play(d, draw, num_episodes, episode_length)


def try_tabular_q_learning(iters=10000, eps=0.5):
    return test_learn_play(
        iters=iters, tabular=True, batch=False, draw=True, num_episodes=10, eps=eps
    )


def try_tabular_batch_q_learning(iters=10, eps=0.5):
    return test_learn_play(
        iters=iters, tabular=True, batch=True, draw=True, num_episodes=10, eps=eps
    )


def try_nn_q_learning(iters=10000, eps=0.5):
    # nn_q_learning not implemented for lab code; just uses TabularQ
    return test_learn_play(
        iters=iters, tabular=False, batch=False, draw=True, num_episodes=10, eps=eps
    )


def try_nn_batch_q_learning(iters=100, eps=0.5):
    # nn_q_learning not implemented for lab code; just uses TabularQ
    return test_learn_play(
        iters=iters, tabular=False, batch=True, draw=True, num_episodes=100, eps=eps
    )


if __name__ == "__main__":
    pass
    # try_value_iteration()
    # try_tabular_q_learning()
    # try_tabular_batch_q_learning(iters=100)  # used in lab colab notebook
    # try_tabular_batch_q_learning(iters=200, eps=0.5)  # used in lab colab notebook
    # try_nn_q_learning()
    # try_nn_batch_q_learning()

    # Homework
    # test_solve_play()
    # test_learn_play(iters=1000, tabular=True, batch=False)  # Tabular Q-learn
    test_learn_play(iters=50, tabular=True, batch=True)  # Tabular Batch Q-learn
    # test_learn_play(iters=1000, tabular=False, batch=False)  # NN Q-learn
    # test_learn_play(iters=50, tabular=False, batch=True)  # NN Batch Q-learn (Fitted Q-learn)

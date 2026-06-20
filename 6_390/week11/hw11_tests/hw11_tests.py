import functools
import matplotlib.pyplot as plt
import numpy as np
import pickle
import random
import torch
import torch.nn as nn

from dist import DDist, uniform_dist, delta_dist, mixture_dist
from util import argmax, argmax_with_val
from mdp import MDP, TabularQ, sim_episode, evaluate
from no_exit import NoExit
from plotting import plot_points, animate
from test_suite import run_test_suite

from implementations import (
    value,
    greedy,
    epsilon_greedy,
    update,
    value_iteration,
    Q_learn,
    Q_learn_batch,
    NNQ,
)

# from implementations_solutions import (
#    value, greedy, epsilon_greedy, update, value_iteration, Q_learn, Q_learn_batch, NNQ
#    )


# You should implement greedy, epsilon_greedy, value_iteration,
# Q_learn, Q_learn_batch, and NNQ in the colab (or in
# implementations.py) to complete the skeletons there.


### test implementations


def test_value(fn):
    """
    Tests the value() method: test_value(value)
    """
    q = TabularQ([0, 1, 2, 3], ["b", "c"])
    q.set(0, "b", 5)
    q.set(0, "c", 10)
    q.set(1, "b", 2)
    cases = [
        (q, 0, 10),
        (q, 1, 2),
    ]
    run_test_suite(cases, fn, seed=6036)


def test_greedy(fn):
    """
    Tests the greedy() method: test_greedy(greedy)
    """
    q = TabularQ([0, 1, 2, 3], ["b", "c"])
    q.set(0, "b", 5)
    q.set(0, "c", 10)
    q.set(1, "b", 2)
    q.set(1, "c", 2)
    eps = 0.0
    cases = [
        (q, 0, "c"),
        (q, 1, "b"),
    ]
    run_test_suite(cases, fn, seed=6036)


def test_epsilon_greedy(fn):
    """
    Tests the epsilon_greedy() method: test_epsilon_greedy(epsilon_greedy)
    """
    q = TabularQ([0, 1, 2, 3], ["b", "c"])
    q.set(0, "b", 5)
    q.set(0, "c", 10)
    q.set(1, "b", 2)
    eps = 0.0
    cases = [
        (q, 0, 0.0, "c"),
        (q, 1, 0.0, "b"),
        (q, 0, 1.0, "b"),
    ]
    run_test_suite(cases, fn, seed=6037)


def test_update(fn):
    """
    Tests the update() method for TabularQ: test_update(update)
    """
    TabularQ.update = fn
    q = TabularQ([0, 1, 2, 3], ["b", "c"])
    q.update([(0, "b", 50), (2, "c", 30)], 0.5)
    q.update([(0, "b", 25)], 0.5)
    cases = [(0, "b", 25.0), (2, "c", 15.0)]
    run_test_suite(cases, q.get)


def test_value_iteration(value_iteration_fn):
    """
    Tests the value_iteration function: test_value_iteration(value_iteration)
    """
    # This is the same test case as in the exercises and homework
    tiny = MDP([0, 1, 2, 3], ["b", "c"], tinyTrans, tinyR, 0.9)

    keys = [
        (0, "b"),
        (0, "c"),
        (1, "b"),
        (1, "c"),
        (2, "b"),
        (2, "c"),
        (3, "b"),
        (3, "c"),
    ]

    def test_helper(mdp, it):
        mdp.q = TabularQ(tiny.states, tiny.actions)
        value_iteration(mdp, eps=0.01, max_iters=it)
        return np.array([mdp.q.get(s, a) for s, a in keys])

    cases = [
        (tiny, 0, np.array([0.0] * 8)),
        (tiny, 1, np.array([0, 0, 1, 1, 0, 0, 2, 2])),
        (tiny, 2, np.array([0.81, 0.09, 1.09, 1.09, 1.62, 1.62, 2.18, 2.18])),
        (
            tiny,
            3,
            np.array([1.0287, 1.4103, 1.7542, 1.7542, 1.9116, 1.9116, 2.8523, 2.8523]),
        ),
        (
            tiny,
            100,
            np.array(
                [
                    5.77538316,
                    5.96641095,
                    6.40016455,
                    6.40016455,
                    6.66549305,
                    6.66549305,
                    7.49906565,
                    7.49906565,
                ]
            ),
        ),
    ]
    run_test_suite(cases, test_helper, seed=0)


def test_Q_learn(q_learn_fn, update_fn):
    """
    Tests the Q-learn() method: test_Q_learn(Q_learn, update)
    """
    TabularQ.update = update_fn
    small = MDP([0, 1, 2, 3, 4], ["a", "b"], tinyTrans, tinyR, 0.9)
    small.terminal = smallTerminal

    keys = [
        (0, "a"),
        (0, "b"),
        (1, "a"),
        (1, "b"),
        (2, "a"),
        (2, "b"),
        (3, "a"),
        (3, "b"),
        (4, "a"),
        (4, "b"),
    ]

    def test_helper(mdp):
        mdp.q = TabularQ(small.states, small.actions)
        q_learn_fn(mdp)
        return np.array([mdp.q.get(s, a) for s, a in keys])

    expected = np.array(
        [
            0.08694802,
            0.68300509,
            0.99092492,
            1.15964309,
            0.39208978,
            0.37053509,
            1.43171464,
            1.05995431,
            0.0,
            0.0,
        ]
    )
    cases = [(small, expected)]
    run_test_suite(cases, test_helper, seed=0)


def test_Q_learn_batch(q_learn_batch_fn, update_fn):
    TabularQ.update = update_fn
    small = MDP([0, 1, 2, 3, 4], ["a", "b"], tinyTrans, tinyR, 0.9)
    small.terminal = smallTerminal

    keys = [
        (0, "a"),
        (0, "b"),
        (1, "a"),
        (1, "b"),
        (2, "a"),
        (2, "b"),
        (3, "a"),
        (3, "b"),
        (4, "a"),
        (4, "b"),
    ]

    def test_helper(mdp):
        mdp.q = TabularQ(small.states, small.actions)
        q_learn_batch_fn(mdp)
        return np.array([mdp.q.get(s, a) for s, a in keys])

    expected = np.array(
        [
            6.30461114,
            6.0158579,
            6.56742268,
            6.63701232,
            6.98354186,
            7.0346514,
            7.82476127,
            7.76657775,
            0.0,
            0.0,
        ]
    )

    cases = [(small, expected)]
    run_test_suite(cases, test_helper, seed=0)


def test_NNQ(nnq_module):
    """
    Tests the NNQ module: test_NNQ(NNQ)
    """
    data = [(0, "b", 0.3), (1, "b", 0.1), (0, "b", 0.1), (1, "b", 0.5)]
    small = MDP([0, 1, 2, 3, 4], ["b", "c"], smallTrans, smallR, 0.9)
    small.terminal = smallTerminal

    def test_helper(mdp):
        torch.manual_seed(0)
        q = nnq_module(mdp.states, mdp.actions, mdp.state2vec, 2, 10)
        q.update(data, 1)
        return np.array([q.get(s, a) for s in q.states for a in q.actions])

    expected = np.array(
        [
            [[0.07894802]],
            [[-0.20692152]],
            [[0.08004203]],
            [[-0.1686033]],
            [[0.09363519]],
            [[-0.19312027]],
            [[0.06085893]],
            [[-0.24304576]],
            [[0.04742564]],
            [[-0.26113757]],
        ]
    )

    cases = [(small, expected)]
    run_test_suite(cases, test_helper, seed=0)


def test_NNQ2(nnq_module):
    np.random.seed(0)
    torch.manual_seed(0)

    data = [(0, "b", 0.3), (1, "b", 0.1), (0, "b", 0.1), (1, "b", 0.5)]
    small = MDP([0, 1, 2, 3, 4], ["b", "c"], smallTrans2, smallR, 0.9)
    small.terminal = smallTerminal

    def test_helper(mdp):
        q = nnq_module(small.states, small.actions, small.state2vec, 2, 10)
        q.update(data, 1)
        return [q.get(s, a).item(0) for s in q.states for a in q.actions]

    got = test_helper(small)
    print("Result of test_NNQ2(NNQ) for homework question entry:")
    print(got)


### implementation of tiny MDP from lab & homework


def tinyTerminal(s):
    return s == 4


def tinyR(s, a):
    if s == 1:
        return 1
    elif s == 3:
        return 2
    else:
        return 0


def tinyTrans(s, a):
    if s == 0:
        if a == "b":
            return DDist({1: 0.9, 2: 0.1})
        else:
            return DDist({1: 0.1, 2: 0.9})
    elif s == 1:
        return DDist({1: 0.1, 0: 0.9})
    elif s == 2:
        return DDist({2: 0.1, 3: 0.9})
    elif s == 3:
        return DDist({0: 0.9, 3: 0.1})


### implementation of small MDP that adds a terminal state


def smallTerminal(s):
    return s == 4


def smallR(s, a):
    if s == 1:
        return 1
    elif s == 3:
        return 2
    else:
        return 0


def smallTrans(s, a):
    if s == 0:
        if a == "a":
            return DDist({1: 0.9, 2: 0.1})
        else:
            return DDist({1: 0.1, 2: 0.9})
    elif s == 1:
        return DDist({1: 0.1, 0: 0.9})
    elif s == 2:
        return DDist({2: 0.1, 3: 0.9})
    elif s == 3:
        return DDist({3: 0.1, 0: 0.5, 4: 0.4})
    elif s == 4:
        return DDist({4: 1.0})


def smallTrans2(s, a):
    if s == 0:
        return DDist({1: 1.0})
    elif s == 1:
        return DDist({2: 1.0})
    elif s == 2:
        return DDist({3: 1.0})
    elif s == 3:
        return DDist({4: 1.0})
    elif s == 4:
        return DDist({4: 1.0})


def test_solve_play(d=5, draw=False, num_episodes=10, episode_length=100):
    game = NoExit(d)
    game.q = TabularQ(game.states, game.actions)

    # solve the game
    value_iteration(game)  # USER

    # print(f"{game.q=}") #DEBUG
    # return

    # play the game using greedy policy
    def policy(s):
        return greedy(game.q, s)  # USER

    for i in range(num_episodes):
        reward, _, animation = sim_episode(
            game,
            policy,
            episode_length,
            draw=(i == (num_episodes - 1)),
            animate=animate,
        )
        print("Reward", reward)
    return animation


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
    iters_per_value = 1 if iters <= 10 else int(iters / 10.0)
    scores = []

    game = NoExit(d)
    if game.q is None:
        if tabular:
            TabularQ.update = update  # USER
            game.q = TabularQ(game.states, game.actions)
        else:
            # USER NNQ used here
            game.q = NNQ(
                game.states,
                game.actions,
                game.state2vec,
                num_layers,
                num_units,
                epochs=batch_epochs if batch else 1,
                lr=nnq_lr,
            )

    def policy(s):
        return greedy(game.q, s)  # USER

    def interact(iter=0, s=None, a=None, r=None):
        if iter % iters_per_value == 0:
            scores.append(
                (iter, evaluate(game, policy, num_episodes, episode_length)[0])
            )
            print("score", scores[-1], flush=True)

    # learn the game. #USER Q_learn and Q_learn_batch used here
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
    def policy(s):
        return greedy(game.q, s)  # USER

    print("simulating episodes to play the game...", flush=True)
    rewards = []
    for i in range(num_episodes):
        reward, _, animation = sim_episode(
            game,
            policy,
            episode_length,
            draw=(i == (num_episodes - 1)),
            animate=animate,
        )
        print("Reward", reward)
        rewards.append(reward)

    print("String to upload (incude quotes):")
    print(f'"{to_hex(pickle.dumps([tabular, batch, scores, rewards], 0).decode())}"')

    return animation


# For homework checking
def to_hex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace("0x", "")
        if len(hv) == 1:
            hv = "0" + hv
        lst.append(hv)
    return functools.reduce(lambda x, y: x + y, lst)


if __name__ == "__main__":
    test_value(value)
    test_greedy(greedy)
    test_epsilon_greedy(epsilon_greedy)
    test_update(update)
    test_value_iteration(value_iteration)
    test_Q_learn(Q_learn, update)
    test_Q_learn_batch(Q_learn_batch, update)
    test_NNQ(NNQ)
    test_NNQ2(NNQ)

    # test_solve_play()
    # test_learn_play(iters=1000, tabular=True, batch=False)  # Tabular Q-learn
    # test_learn_play(iters=50, tabular=True, batch=True)  # Tabular Batch Q-learn
    # test_learn_play(iters=1000, tabular=False, batch=False)  # NN Q-learn
    # test_learn_play(iters=50, tabular=False, batch=True)  # NN Batch Q-learn (Fitted Q-learn)

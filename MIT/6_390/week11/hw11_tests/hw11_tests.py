import functools
import pickle
import random

import numpy as np
import torch
import torch.nn as nn

from dist import DDist, uniform_dist
from implementations import greedy, value_iteration, Q_learn, Q_learn_batch, NNQ
from mdp import MDP, TabularQ
from no_exit import NoExit
from plotting import plot_points, animate
from test_suite import run_test_suite


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


def tinyTrans2(s, a):
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


def argmax(l, f):
    """
    @param l: C{List} of items
    @param f: C{Procedure} that maps an item into a numeric score
    @returns: the element of C{l} that has the highest score
    """
    vals = [f(x) for x in l]
    return l[vals.index(max(vals))]


### Implement Q-Learning


def sim_episode(mdp, episode_length, policy, draw=False):
    """
    Simulate an episode (sequence of transitions) of at most
    episode_length, using policy function to select actions.
    If we find a terminal state, end the episode.

    Returns:
        * accumulated reward
        * a list of (s, a, r, s') where s' is None for transition from terminal state.
        * an animation if draw=True, or None if draw=False
    """
    episode = []
    reward = 0
    s = mdp.init_state()
    all_states = [s]
    for i in range(episode_length):
        a = policy(s)
        (r, s_prime) = mdp.sim_transition(s, a)
        reward += r
        if mdp.terminal(s):
            episode.append((s, a, r, None))
            break
        episode.append((s, a, r, s_prime))
        if draw:
            mdp.draw_state(s)
        s = s_prime
        all_states.append(s)
    animation = animate(all_states, mdp.n, episode_length) if draw else None
    return reward, episode, animation


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
    run_test_suite(cases, fn, seed=6036)


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


def test_Q_learn(q_learn_fn, update_fn):
    """
    Tests the Q-learn() method: test_Q_learn(Q_learn, update)
    """
    TabularQ.update = update_fn
    tiny = MDP([0, 1, 2, 3, 4], ["a", "b"], tinyTrans, tinyR, 0.9)
    tiny.terminal = tinyTerminal
    q = TabularQ(tiny.states, tiny.actions)

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

    def test_helper(mdp, q):
        qf = q_learn_fn(tiny, q)
        return np.array([qf.get(s, a) for s, a in keys])

    expected = np.array(
        [
            0.69531115,
            0.2544561,
            1.18388523,
            0.75497725,
            0.56289066,
            0.17751208,
            1.31171463,
            0.97562661,
            0.0,
            0.0,
        ]
    )
    cases = [(tiny, q, expected)]
    run_test_suite(cases, test_helper, seed=0)


def test_Q_learn_batch(q_learn_batch_fn, update_fn):
    TabularQ.update = update_fn
    tiny = MDP([0, 1, 2, 3, 4], ["a", "b"], tinyTrans, tinyR, 0.9)
    tiny.terminal = tinyTerminal
    q = TabularQ(tiny.states, tiny.actions)

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

    def test_helper(mdp, q):
        qf = q_learn_batch_fn(tiny, q)
        return np.array([qf.get(s, a) for s, a in keys])

    expected = np.array(
        [
            4.34435113,
            3.5007353,
            5.05064749,
            5.02523079,
            3.45342765,
            3.43896474,
            3.84099014,
            3.54922581,
            0.0,
            0.0,
        ]
    )

    cases = [(tiny, q, expected)]
    run_test_suite(cases, test_helper, seed=0)


### NNQ: Using neural networks to store the Q function


def make_nn(state_dim, num_layers, num_units):
    """
    Make a ReLU-activated neural network (i.e. ReLU-activated MLP)
    with the specified details. All hidden layers have the same size of num_units

    state_dim: (int) number of states
    num_layers: (int) number of fully connected hidden layers
    num_units: (int) number of dense relu units to use in hidden layers
    """
    model = []
    model += [nn.Linear(state_dim, num_units), nn.ReLU()]
    for i in range(num_layers - 1):
        model += [nn.Linear(num_units, num_units), nn.ReLU()]
    model += [nn.Linear(num_units, 1)]
    model = nn.Sequential(*model)
    return model


def test_NNQ(nnq_module):
    """
    Tests the NNQ module: test_NNQ(NNQ)
    """
    data = [(0, "a", 0.3), (1, "a", 0.1), (0, "a", 0.1), (1, "a", 0.5)]
    tiny = MDP([0, 1, 2, 3, 4], ["a", "b"], tinyTrans, tinyR, 0.9)
    tiny.terminal = tinyTerminal

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

    cases = [(tiny, expected)]
    run_test_suite(cases, test_helper, seed=0)


def test_NNQ2(nnq_module):
    np.random.seed(0)
    torch.manual_seed(0)

    data = [(0, "a", 0.3), (1, "a", 0.1), (0, "a", 0.1), (1, "a", 0.5)]
    tiny = MDP([0, 1, 2, 3, 4], ["a", "b"], tinyTrans2, tinyR, 0.9)
    tiny.terminal = tinyTerminal
    q = nnq_module(tiny.states, tiny.actions, tiny.state2vec, 2, 10)
    q.update(data, 1)
    return [q.get(s, a).item(0) for s in q.states for a in q.actions]


### No Exit: Learning to Play

# Return average reward for n_episodes of length episode_length
# while following policy (a function of state) to choose actions.
def evaluate(mdp, n_episodes, episode_length, policy):
    score = 0
    length = 0
    for i in range(n_episodes):
        # Accumulate the episode rewards
        r, e, _ = sim_episode(mdp, episode_length, policy)
        score += r
        length += len(e)
        # print('    ', r, len(e))
    return score / n_episodes, length / n_episodes


def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace("0x", "")
        if len(hv) == 1:
            hv = "0" + hv
        lst.append(hv)

    return functools.reduce(lambda x, y: x + y, lst)


def test_solve_play(d=5, draw=False, num_episodes=10, episode_length=100):
    game = NoExit(d)
    qf = value_iteration(game, TabularQ(game.states, game.actions))
    for i in range(num_episodes):
        reward, _, animation = sim_episode(
            game,
            (episode_length if d > 3 else episode_length / 2),
            lambda s: greedy(qf, s),
            draw=draw,
        )
        print("Reward", reward)
    return animation


def test_learn_play(
    d=5,
    num_layers=2,
    num_units=100,
    eps=0.5,
    iters=10000,
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

    def interact(q, iter=0):
        if iter % iters_per_value == 0:
            scores.append(
                (
                    iter,
                    evaluate(
                        game, num_episodes, episode_length, lambda s: greedy(q, s)
                    )[0],
                )
            )
            print("score", scores[-1], flush=True)

    game = NoExit(d)
    if tabular:
        q = TabularQ(game.states, game.actions)
    else:
        q = NNQ(
            game.states,
            game.actions,
            game.state2vec,
            num_layers,
            num_units,
            epochs=batch_epochs if batch else 1,
            lr=nnq_lr,
        )
    if batch:
        qf = Q_learn_batch(
            game,
            q,
            iters=iters,
            episode_length=100,
            n_episodes=10,
            interactive_fn=interact,
        )
    else:
        qf = Q_learn(game, q, iters=iters, interactive_fn=interact)
    if scores:
        print(
            'String to upload (incude quotes): "%s"'
            % toHex(pickle.dumps([tabular, batch, scores], 0).decode())
        )
        # Plot learning curve
        plot_points(np.array([s[0] for s in scores]), np.array([s[1] for s in scores]))
    for i in range(num_episodes):
        reward, _, animation = sim_episode(
            game,
            (episode_length if d > 3 else episode_length / 2),
            lambda s: greedy(qf, s),
            draw=draw,
        )
        print("Reward", reward)
    return animation

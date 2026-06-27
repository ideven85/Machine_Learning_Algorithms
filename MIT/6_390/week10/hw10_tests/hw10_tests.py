import numpy as np

from dist import DDist
from mdp import MDP, TabularQ
from test_suite import run_test_suite


def tiny_reward(s, a):
    # Tiny MDP reward function
    if s == 1:
        return 1
    elif s == 3:
        return 2
    else:
        return 0


def tiny_transition(s, a):
    # Tiny MDP transition function
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
        return DDist({3: 0.1, 0: 0.9})


def argmax(l, f):
    """
    @param l: C{List} of items
    @param f: C{Procedure} that maps an item into a numeric score
    @returns: the element of C{l} that has the highest score
    """
    vals = [f(x) for x in l]
    return l[vals.index(max(vals))]


def test_value(fn):
    """
    Tests value function: test_value(value)
    """
    q = TabularQ([0, 1, 2, 3], ["b", "c"])
    q.set(0, "b", 5)
    q.set(0, "c", 10)
    cases = [(q, 0, 10)]
    run_test_suite(cases, fn)


def test_greedy(fn):
    """
    Tests greedy function: test_greedy(greedy)
    """
    q = TabularQ([0, 1, 2, 3], ["b", "c"])
    q.set(0, "b", 5)
    q.set(0, "c", 10)
    q.set(1, "b", -2)
    q.set(1, "c", -5)
    cases = [(q, 0, "c"), (q, 1, "b")]
    run_test_suite(cases, fn)


def test_epsilon_greedy(fn):
    """
    Unused
    """
    q = TabularQ([0, 1, 2, 3], ["b", "c"])
    q.set(0, "b", 5)
    q.set(0, "c", 10)
    q.set(1, "b", 2)
    eps = 0.0
    cases = [(q, 0, eps, "c"), (q, 1, eps, "b")]
    run_test_suite(cases, fn)


def test_value_iteration(value_iteration_fn):
    """
    Tests value iteration function: test_value_iteration(value_iteration)
    """

    def test_helper(mdp, q, eps=0.01, max_iters=1000):
        qvi = value_iteration_fn(tiny, q, eps=eps, max_iters=max_iters)
        return np.array([v for _, v in sorted(list(qvi.q.items()), key=lambda x: x[0])])

    tiny = MDP([0, 1, 2, 3], ["b", "c"], tiny_transition, tiny_reward, 0.9)
    q = TabularQ(tiny.states, tiny.actions)
    expected1 = dict(
        [
            ((2, "b"), 5.962924188028282),
            ((1, "c"), 5.6957634856549095),
            ((1, "b"), 5.6957634856549095),
            ((0, "b"), 5.072814297918393),
            ((0, "c"), 5.262109602844769),
            ((3, "b"), 6.794664584556008),
            ((3, "c"), 6.794664584556008),
            ((2, "c"), 5.962924188028282),
        ]
    )
    expected1_list = np.array(
        [v for _, v in sorted(list(expected1.items()), key=lambda x: x[0])]
    )

    cases = [
        (tiny, q, 0.1, 100, expected1_list),
    ]
    run_test_suite(cases, test_helper)


def test_q_star(fn):
    """
    Tests calculation of horizon-h Q-value from expectimax search: test_q_star(q_star)
    """
    tiny = MDP([0, 1, 2, 3], ["b", "c"], tiny_transition, tiny_reward, 0.9)
    cases = [
        (tiny, 0, "b", 0, np.array([0.0])),
        (tiny, 0, "b", 1, np.array([0.0])),
        (tiny, 0, "b", 2, np.array([0.81])),
        (tiny, 0, "b", 3, np.array([1.0287000000000002])),
        (tiny, 0, "c", 3, np.array([1.4103])),
        (tiny, 2, "b", 3, np.array([1.9116000000000002])),
        (tiny, 2, "c", 3, np.array([1.9116000000000002])),
    ]
    run_test_suite(cases, lambda *args: np.array([fn(*args)]))

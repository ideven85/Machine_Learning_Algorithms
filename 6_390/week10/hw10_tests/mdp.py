import numpy as np

from dist import uniform_dist, delta_dist, MixtureDDist


class MDP:
    """
    Needs the following attributes:
    states: list or set of states
    actions: list or set of actions
    discount_factor: real, greater than 0, less than or equal to 1
    start: optional instance of DDist, specifying initial state dist
       if it's unspecified, we'll use a uniform over states
    These are functions:
    transition_model: function from (state, action) into DDist over next state
    reward_fn: function from (state, action) to real-valued reward
    """

    def __init__(
        self,
        states,
        actions,
        transition_model,
        reward_fn,
        discount_factor=1.0,
        start_dist=None,
    ):
        self.states = states
        self.actions = actions
        self.transition_model = transition_model
        self.reward_fn = reward_fn
        self.discount_factor = discount_factor
        self.start = start_dist if start_dist else uniform_dist(states)

    def terminal(self, s):
        """
        Given a state, return True if the state should be considered to
        be terminal.  You can think of a terminal state as generating an
        infinite sequence of zero reward.
        """
        return False

    def init_state(self):
        """Randomly choose a state from the initial state distribution"""
        return self.start.draw()

    def sim_transition(self, s, a):
        """
        Simulate a transition from state s, given action a.

        Returns a tuple containing
            1. reward for (s,a); and
            2. new state, drawn from transition.
        If a terminal state is encountered, samples next state from
        initial state distribution
        """
        return (
            self.reward_fn(s, a),
            (
                self.init_state()
                if self.terminal(s)
                else self.transition_model(s, a).draw()
            ),
        )

    def state2vec(self, s):
        """
        Return one-hot encoding of state s; used in neural network agent implementations
        """
        v = np.zeros((1, len(self.states)))
        v[0, self.states.index(s)] = 1.0
        return v


class TabularQ:
    # A dictionary that maps (s, a) pairs to their Q values.
    def __init__(self, states, actions):
        self.actions = actions
        self.states = states
        self.q = dict([((s, a), 0.0) for s in states for a in actions])

    def copy(self):
        q_copy = TabularQ(self.states, self.actions)
        q_copy.q.update(self.q)
        return q_copy

    def set(self, s, a, v):
        self.q[(s, a)] = v

    def get(self, s, a):
        return self.q[(s, a)]

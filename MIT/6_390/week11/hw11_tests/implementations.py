import numpy as np
import random
import torch
import torch.nn as nn

from dist import DDist, uniform_dist, delta_dist, mixture_dist
from util import argmax, argmax_with_val
from mdp import MDP, TabularQ, sim_episode, evaluate

"""
Your implementations. These functions will get overwritten with
your finished implementations in the colab.
"""


def value(q, s):
    raise NotImplementedError("Copy your implementation for the previous homework.")


def greedy(q, s):
    raise NotImplementedError("Copy your implementation for the previous homework.")


def epsilon_greedy(q, s, eps=0.5):
    if random.random() < eps:
        # True with prob eps, random action
        raise NotImplementedError("Override in Colab.")
    else:
        # False with prob 1-eps, greedy action
        raise NotImplementedError("Override in Colab.")


def update(self, data, lr):
    raise NotImplementedError("Override in Colab.")


# Note: Different than in previous homework. Here, we expect
# mdp to have mdp.q holding the q function.
def value_iteration(mdp, eps=0.01, max_iters=1_000):
    raise NotImplementedError(
        "Copy & revise your implementation for the previous homework."
    )


# Note: mdp will have mdp.q, with mdp.q.update method. Your update(self, ...) will
# be installed into TabularQ.
def Q_learn(mdp, lr=0.1, iters=100, eps=0.5, interactive_fn=None):
    raise NotImplementedError
    ...  # Your code here
    for i in range(iters):
        ...  # Your code here
        if interactive_fn:
            interactive_fn(i)


# Note: mdp will have mdp.q, with mdp.q.update method. Your update(self, ...) will
# be installed into TabularQ.
def Q_learn_batch(
    mdp,
    lr=0.1,
    iters=100,
    eps=0.5,
    episode_length=10,
    n_episodes=2,
    interactive_fn=None,
):
    raise NotImplementedError
    ...  # Your code here
    for i in range(iters):
        ...  # Your code here
        if interactive_fn:
            interactive_fn(i)


class NNQ:
    def __init__(
        self, states, actions, state2vec, num_layers, num_units, lr=1e-2, epochs=1
    ):
        self.running_loss = 0.0  # To keep a running average of the loss
        self.running_one = 0.0  # idem
        self.num_running = 0.001  # idem
        self.lr = lr
        self.states = states
        self.actions = actions
        self.state2vec = state2vec
        state_dim = state2vec(states[0]).shape[1]  # a row vector
        self.epochs = epochs
        self.models = None  # Your code here

    def predict(self, model, s):
        return model(torch.FloatTensor(self.state2vec(s))).detach().numpy()

    def get(self, s, a):
        raise NotImplementedError
        ...  # Your code here

    def fit(self, model, X, Y, epochs=None, dbg=None):
        # This function expects numpy arrays for X (shape (K, state_dim)) and Y (shape (K, 1)),
        # not Python lists.
        assert type(X) is not type([]), (
            "self.fit expects numpy arrays for X (shape (K, state_dim)) and Y (shape (K, 1)), not Python lists."
        )

        if epochs is None:
            epochs = self.epochs

        train = torch.utils.data.TensorDataset(
            torch.FloatTensor(X), torch.FloatTensor(Y)
        )
        train_loader = torch.utils.data.DataLoader(train, batch_size=256, shuffle=True)
        opt = torch.optim.SGD(model.parameters(), lr=self.lr)

        for epoch in range(epochs):
            for X, Y in train_loader:
                opt.zero_grad()
                loss = torch.nn.MSELoss()(model(X), Y)
                loss.backward()
                self.running_loss = (
                    self.running_loss * (1.0 - self.num_running)
                    + loss.item() * self.num_running
                )
                self.running_one = (
                    self.running_one * (1.0 - self.num_running) + self.num_running
                )
                opt.step()

        # if dbg or (dbg is None and np.random.rand() < (0.001*X.shape[0])):
        #     print('Loss running average: ', self.running_loss/self.running_one)

    def update(self, data, lr, dbg=None):
        # Train the model for every action. Remember to check there is
        # actually data to train on!
        raise NotImplementedError
        ...  # Your code here


def make_nn(state_dim, num_layers, num_units):
    """
    Make a ReLU-activated neural network (i.e., ReLU-activated MLP)
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

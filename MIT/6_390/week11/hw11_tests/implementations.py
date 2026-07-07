"""
Your implementations. These functions will get overwritten with your finished implementations in the colab.
"""

import random


def value(q, s):
    raise NotImplementedError("Copy your implementation for the previous homework.")


def greedy(q, s):
    raise NotImplementedError("Copy your implementation for the previous homework.")


def value_iteration(mdp, q, eps=0.01, max_iters=1000):
    raise NotImplementedError("Copy your implementation for the previous homework.")


def epsilon_greedy(q, s, eps=0.5):
    if random.random() < eps:  # True with prob eps, random action
        raise NotImplementedError("Override in Colab.")
    else:  # False with prob 1-eps, greedy action
        raise NotImplementedError("Override in Colab.")


def Q_learn(mdp, q, lr=0.1, iters=100, eps=0.5, interactive_fn=None):
    # Your code here
    raise NotImplementedError
    for i in range(iters):
        if interactive_fn:
            interactive_fn(q, i)  # don't touch this line
    pass


def Q_learn_batch(
    mdp,
    q,
    lr=0.1,
    iters=100,
    eps=0.5,
    episode_length=10,
    n_episodes=2,
    interactive_fn=None,
):
    raise NotImplementedError
    # Your code here
    for i in range(iters):
        # include this line in the iteration, where i is the iteration number
        if interactive_fn:
            interactive_fn(q, i)
    pass


class NNQ:
    def __init__(
        self, states, actions, state2vec, num_layers, num_units, lr=1e-2, epochs=1
    ):
        self.running_loss = 0.0  # To keep a running average of the loss
        self.running_one = 0.0  # idem
        self.num_running = 0.001  # idem
        self.lr = lr
        self.actions = actions
        self.states = states
        self.state2vec = state2vec
        self.epochs = epochs
        state_dim = state2vec(states[0]).shape[1]  # a row vector
        self.models = None  # TODO: YOUR CODE HERE

    def predict(self, model, s):
        return model(torch.FloatTensor(self.state2vec(s))).detach().numpy()

    def get(self, s, a):
        # TODO: YOUR CODE HERE
        raise NotImplementedError

    def fit(self, model, X, Y, epochs=None, dbg=None):
        # This function receives two numpy arrays (with shape (K,7) and (K,1)), not two lists!
        assert type(X) is not type(
            []
        ), "self.fit receives two numpy arrays (with shape (K,7) and (K,1)), not two lists!"

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

        # if dbg is True or (dbg is None and np.random.rand() < (0.001*X.shape[0])):
        #     print('Loss running average: ', self.running_loss/self.running_one)

    def update(self, data, lr, dbg=None):
        # TODO: YOUR CODE HERE: train the model for every action
        # Remember to check there is actually data to train on!
        raise NotImplementedError

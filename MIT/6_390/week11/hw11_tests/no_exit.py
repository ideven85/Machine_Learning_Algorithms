import matplotlib.pyplot as plt
import numpy as np

from dist import DDist, uniform_dist, delta_dist
from mdp import MDP


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
        if random_start:
            self.start = uniform_dist([((br, 0), (0, 1), 0, 0) for br in range(self.n)])
        else:
            self.start = delta_dist(((int(self.n / 2), 0), (0, 1), 0, 0))

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
            (br, bc), (brv, bcv), pp, pv = state
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
        (br, bc), (brv, bcv), pp, pv = s
        return np.array([[br, bc, brv, bcv, pp, pv, 0]])

    def terminal(self, state):
        return state == "over"

    def reward_fn(self, s, a):
        return 0 if s == "over" else 1

    def transition_model(self, s, a, p=0.4):
        # Only randomness is in brv and brc after a bounce
        # 1- prob of negating nominal velocity
        if s == "over":
            return delta_dist("over")
        # Current state
        (br, bc), (brv, bcv), pp, pv = s
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
                return delta_dist("over")

        new_s = ((new_br, new_bc), (new_brv, new_bcv), new_pp, new_pv)
        if (not hit_c) and (not hit_r):
            return delta_dist(new_s)
        elif hit_c:  # also hit_c and hit_r
            if abs(new_brv) > 0:
                return DDist(
                    {
                        new_s: p,
                        ((new_br, new_bc), (-new_brv, new_bcv), new_pp, new_pv): 1 - p,
                    }
                )
            else:
                return DDist(
                    {
                        new_s: p,
                        ((new_br, new_bc), (-1, new_bcv), new_pp, new_pv): 0.5
                        * (1 - p),
                        ((new_br, new_bc), (1, new_bcv), new_pp, new_pv): 0.5 * (1 - p),
                    }
                )
        elif hit_r:
            return DDist(
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

from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO, StringIO


def tidy_plot(
    xmin, xmax, ymin, ymax, center=False, title=None, xlabel=None, ylabel=None
):
    # plt.ion()  # REMOVE?
    plt.figure(facecolor="white")
    ax = plt.subplot()
    if center:
        ax.spines["left"].set_position("zero")
        ax.spines["right"].set_color("none")
        ax.spines["bottom"].set_position("zero")
        ax.spines["top"].set_color("none")
        ax.xaxis.set_ticks_position("bottom")
        ax.yaxis.set_ticks_position("left")
    else:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
    eps = 0.05
    plt.xlim(xmin - eps, xmax + eps)
    plt.ylim(ymin - eps, ymax + eps)
    if title:
        ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    return ax


def plot_points(
    x,
    y,
    ax=None,
    clear=False,
    xmin=None,
    xmax=None,
    ymin=None,
    ymax=None,
    style="or-",
    equal=False,
    mark_initial=False,
    mark_final=False,
):
    padup = lambda v: v + 0.05 * abs(v)
    paddown = lambda v: v - 0.05 * abs(v)
    if ax is None:
        if xmin == None:
            xmin = paddown(np.min(x))
        if xmax == None:
            xmax = padup(np.max(x))
        if ymin == None:
            ymin = paddown(np.min(y))
        if ymax == None:
            ymax = padup(np.max(y))
        ax = tidy_plot(xmin, xmax, ymin, ymax)
        x_range = xmax - xmin
        y_range = ymax - ymin
        if equal and 0.1 < x_range / y_range < 10:
            plt.axis("equal")
            if x_range > y_range:
                ax.set_xlim((xmin, xmax))
            else:
                ax.set_ylim((ymin, ymax))
        xlim, ylim = ax.get_xlim(), ax.get_ylim()
    elif clear:
        xlim, ylim = ax.get_xlim(), ax.get_ylim()
        ax.clear()
    else:
        xlim, ylim = ax.get_xlim(), ax.get_ylim()
    ax.plot(x, y, style, markeredgewidth=0.0, linewidth=3.0)
    if mark_initial:
        ax.plot(x[0], y[0], "xb", markersize=12)
    if mark_final:
        ax.plot(x[-1], y[-1], "Db", markersize=6)
    # Seems to occasionally mess up the limits
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.grid(True, which="both")
    # plt.show()  # let caller control
    return ax


def animate(states, n, ep_length):
    """
    Create a matplotlib animation from all states of the MDP that
    can be played both in colab and in local versions.
    """
    try:
        from matplotlib import animation, rc
        import matplotlib.pyplot as plt
        from google.colab import widgets

        plt.ion()
        plt.figure(facecolor="white")
        fig, ax = plt.subplots()
        plt.close()

        def animate(i):
            if states[i % len(states)] == None or states[i % len(states)] == "over":
                return
            ((br, bc), (brv, bcv), pp, pv) = states[i % len(states)]
            im = np.zeros((n, n + 1))
            im[br, bc] = -1
            im[pp, n] = 1
            ax.cla()
            ims = ax.imshow(
                im,
                interpolation="none",
                cmap="viridis",
                extent=[-0.5, n + 0.5, -0.5, n - 0.5],
                animated=True,
            )
            ims.set_clim(-1, 1)

        rc("animation", html="jshtml")
        anim = animation.FuncAnimation(fig, animate, frames=ep_length, interval=100)
        return anim
    except:
        # we are not in colab, so the typical animation should work
        return None

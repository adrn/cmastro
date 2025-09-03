import matplotlib.pyplot as plt

import cmastro


def test_plot():
    fig, ax = plt.subplots()
    ax.plot([[0, 1], [2, 3]], cmap=cmastro.hesperia)
    plt.clf(fig)


def test_plot_str():
    fig, ax = plt.subplots()
    ax.plot([[0, 1], [2, 3]], cmap="cma:hesperia")
    plt.clf(fig)

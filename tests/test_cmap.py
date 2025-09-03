import matplotlib.pyplot as plt

import cmastro


def test_plot():
    fig, ax = plt.subplots()
    ax.imshow([[0, 1], [2, 3]], cmap=cmastro.hesperia)
    plt.close(fig)


def test_plot_str():
    fig, ax = plt.subplots()
    ax.imshow([[0, 1], [2, 3]], cmap="cma:hesperia")
    plt.close(fig)

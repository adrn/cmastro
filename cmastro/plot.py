# Third-party
import matplotlib.pyplot as plt
import numpy as np


def plot_all_colormaps(cmaps, grayscale=False):
    """Plot all of the colormaps defined in this package"""

    grid = np.linspace(0, 1, 256)

    cmap_names = [name for name in cmaps if not name.endswith('_r')]
    nrows = len(cmap_names)

    fig, axes = plt.subplots(nrows, 1, figsize=(10, 2*nrows),
                             constrained_layout=True)

    # Turn off ticks & spines
    for ax in axes:
        ax.xaxis.set_visible(False)
        ax.yaxis.set_ticks([])

        for _, sp in ax.spines.items():
            sp.set_visible(False)

    for ax, name in zip(axes, cmap_names):
        cmap = cmaps[name]
        rgb = cmap(grid)[:, :3]

        if grayscale:
            from colorspacious import cspace_converter
            LAB = cspace_converter("sRGB1", "CAM02-UCS")(rgb)
            L = LAB[:, 0] / 1e2
            H = np.repeat(L[:, None], 3, axis=1)[None]
        else:
            H = rgb[None]

        ax.imshow(H, aspect=40)
        ax.set_ylabel(name, ha='right', va='center', rotation=0)

    return fig, axes


def plot_lightness(cmaps):
    """Plot all of the colormaps as 1D lightness curves"""
    from colorspacious import cspace_converter

    grid = np.linspace(0, 1, 256)

    cmap_names = [name for name in cmaps if not name.endswith('_r')]
    nrows = len(cmap_names)

    fig, axes = plt.subplots(1, nrows, figsize=(4*nrows, 4),
                             sharex=True, sharey=True,
                             constrained_layout=True)

    for ax, name in zip(axes, cmap_names):
        cmap = cmaps[name]
        rgb = cmap(grid)[:, :3]

        LAB = cspace_converter("sRGB1", "CAM02-UCS")(rgb)
        L = LAB[:, 0] / 1e2

        ax.plot(L)
        ax.set_title(name)
        ax.xaxis.set_ticks([])

    axes[0].set_ylabel('lightness')
    ax.set_ylim(0, 1)

    return fig, axes


def plot_test_card(cmap, seed=None):
    """
    Makes a 4-panel figure with test plots demoing a given colormap.

    Parameters
    ----------
    cmap : `~matplotlib.colors.ListedColormap`
        Instance of a colormap object
    seed : int
        Random number seed.

    Returns
    -------
    fig : `matplotlib.Figure`
    axes : `matplotlib.Axes`
    """
    rng = np.random.default_rng(seed)

    x = rng.uniform(size=1024)
    y = rng.normal(0., np.sqrt(x) * 0.3, size=x.size)
    c = rng.normal(y, 0.5 * x**2)

    fig, axes = plt.subplots(2, 2, figsize=(10, 10), constrained_layout=True)

    axes[0, 0].scatter(x, y, c=c, cmap=cmap, s=12,
                       vmin=-0.5, vmax=0.5)
    axes[0, 0].set_ylim(-0.6, 0.6)

    _grid = np.linspace(0, 1, 32)
    X, Y = np.meshgrid(_grid, _grid)
    C = X
    axes[0, 1].pcolormesh(X, Y, C, cmap=cmap)

    _grid = np.linspace(-1, 1, 256)
    X, Y = np.meshgrid(_grid, _grid)
    C = np.arcsin(np.sin(2*(X**2 + Y**2) + np.arctan2(Y, X)))
    axes[1, 0].pcolormesh(X, Y, C, cmap=cmap)

    _grid = np.arange(512)
    i, j = np.meshgrid(_grid, _grid)
    axes[1, 1].pcolormesh(i, j, np.bitwise_xor(i, j), cmap=cmap)
    axes[1, 1].set_xlim(_grid.min(), _grid.max())
    axes[1, 1].set_ylim(_grid.min(), _grid.max())

    fig.suptitle(str(cmap.name))

    return fig, axes

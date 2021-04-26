# Third-party
import matplotlib.pyplot as plt
import numpy as np

# This package
from .cm import cmaps


def plot_all_colormaps(grayscale=False):
    """Plot all of the colormaps defined in this package"""

    grid = np.linspace(0, 1, 256)

    cmap_names = [name for name in cmaps if not name.endswith('_r')]
    nrows = len(cmap_names)
    fig, axes = plt.subplots(nrows, 1, figsize=(8, 2*nrows))

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
        ax.set_title(name)

        # ax.text(x_text, y_text, cmap.name, va='center', ha='right')

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()

    return fig, axes


def plot_lightness():
    """Plot all of the colormaps as 1D lightness curves"""
    from colorspacious import cspace_converter

    grid = np.linspace(0, 1, 256)

    cmap_names = [name for name in cmaps if not name.endswith('_r')]
    nrows = len(cmap_names)

    fig, axes = plt.subplots(nrows, 1, figsize=(8, 2*nrows),
                             sharex=True, sharey=True)

    for ax, name in zip(axes, cmap_names):
        cmap = cmaps[name]
        rgb = cmap(grid)[:, :3]

        LAB = cspace_converter("sRGB1", "CAM02-UCS")(rgb)
        L = LAB[:, 0] / 1e2

        ax.plot(L)
        ax.set_title(f"{name} (lightness)")

    ax.set_ylim(0, 1)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()

    return fig, axes

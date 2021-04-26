# Third-party
import matplotlib.pyplot as plt
import numpy as np

# This package
from .cm import cmaps


def plot_all_colormaps():
    """Plot all of the colormaps defined in this package"""

    grid = np.linspace(0, 1, 256)

    cmap_names = [name for name in cmaps if not name.endswith('_r')]
    nrows = len(cmap_names)
    fig, axes = plt.subplots(nrows, 1, figsize=(6, 2*nrows))

    for ax, name in zip(axes, cmap_names):
        cmap = cmaps[name]
        H = cmap(grid).reshape(-1, 1)
        ax.imshow(H, aspect=80)

        # ax.text(x_text, y_text, cmap.name, va='center', ha='right')

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()

    return fig, axes

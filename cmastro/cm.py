# Standard library
import pathlib

# Third-party
from matplotlib import cm
from matplotlib.colors import ListedColormap
import numpy as np


data_path = pathlib.Path(__file__).resolve().parent / 'cmaps'

# Colormap data files:
cmap_files = data_path.glob('[!.]*')

cmaps = dict()
for cmap_file in cmap_files:
    kw = dict()
    if cmap_file.suffix == '.csv':
        kw['delimiter'] = ','

    rgb_data = np.loadtxt(cmap_file, **kw)
    cmap_name = f"cma:{cmap_file.stem}"

    cmaps[cmap_name] = ListedColormap(rgb_data, name=cmap_name)
    cmaps[f"{cmap_name}_r"] = ListedColormap(rgb_data[::-1],
                                             name=f"{cmap_name}_r")

###############################################################################
# Custom colormaps that are constructed through operations on defined colormaps
#

# emph and unph (formerly center_emph and center_deemph)
trim = 64
warm = cmaps['cma:hesperia'].colors[::-1][:256 - trim]
cool = cmaps['cma:laguna'].colors[trim + 1:]
colors = np.concatenate((warm,
                         [0.5 * (warm[-1] + cool[0])],
                         cool))
cmaps['cma:emph'] = ListedColormap(colors, name="cma:emph")
cmaps['cma:emph_r'] = ListedColormap(colors[::-1], name="cma:emph_r")

colors = np.concatenate((cmaps['cma:hesperia'].colors[:-1][trim:],
                         cmaps['cma:laguna'].colors[::-1][:256-trim]))
cmaps['cma:unph'] = ListedColormap(colors, name="cma:unph")
cmaps['cma:unph_r'] = ListedColormap(colors[::-1],
                                     name="cma:unph_r")


for cmap in cmaps.values():
    cm.register_cmap(cmap=cmap)

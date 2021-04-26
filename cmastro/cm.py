# Standard library
import pathlib

# Third-party
from matplotlib import cm
from matplotlib.colors import ListedColormap
import numpy as np


data_path = pathlib.Path(__file__).resolve() / 'cmaps'

# Colormap data files:
cmap_files = data_path.glob('[!.]*')

cmaps = dict()
for cmap_file in cmap_files:
    kw = dict()
    if cmap_file.suffix == '.csv':
        kw['delimiter'] = ','

    rgb_data = np.loadtxt(cmap_file, **kw)
    cmap_name = f"cma_{cmap_file.stem}"

    cmaps[cmap_name] = ListedColormap(rgb_data, name=cmap_name)
    cmaps[f"{cmap_name}_r"] = ListedColormap(rgb_data[::-1],
                                             name=f"{cmap_name}_r")

###############################################################################
# Custom colormaps that are constructed through operations on defined colormaps
#

# emph and unph (formerly center_emph and center_deemph)
cmaps['emph'] = ListedColormap((cmaps['hesperia'].colors[::-1][:192] +
                                cmaps['laguna'].colors[1:][64:]),
                               name="emph")
cmaps['emph_r'] = ListedColormap(cmaps['emph'].colors[::-1],
                                 name="emph_r")

cmaps['unph'] = ListedColormap((cmaps['hesperia'].colors[:-1][64:] +
                                cmaps['laguna'].colors[::-1][:192]),
                               name="unph")
cmaps['unph_r'] = ListedColormap(cmaps['emph'].colors[::-1],
                                 name="unph_r")


for cmap in cmaps.values():
    cm.register_cmap(cmap=cmap)

# make colormaps available to call
locals().update(cmaps)

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
for cmap_file in sorted(cmap_files, key=lambda x: x.stem):
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
warm = cmaps['cma:hesperia'].colors
cool = cmaps['cma:laguna'].colors

dark_trim = 50  # don't go all the way to black
light_trim = 12  # don't go all the way to white

this_warm = warm[dark_trim:-light_trim]
this_cool = cool[dark_trim:-light_trim]

colors = np.concatenate((this_warm[::-1],
                         [0.5 * (this_warm[0] + this_cool[0])],
                         this_cool))
cmaps['cma:emph'] = ListedColormap(colors, name="cma:emph")
cmaps['cma:emph_r'] = ListedColormap(colors[::-1], name="cma:emph_r")

colors = np.concatenate((this_warm,
                         [0.5 * (this_warm[-1] + this_cool[-1])],
                         this_cool[::-1]))
cmaps['cma:unph'] = ListedColormap(colors, name="cma:unph")
cmaps['cma:unph_r'] = ListedColormap(colors[::-1],
                                     name="cma:unph_r")

assert len(this_warm) == len(this_cool)
assert np.allclose(cmaps['cma:emph'](0.5), cmaps['cma:emph_r'](0.5))

for cmap in cmaps.values():
    cm.register_cmap(cmap=cmap)

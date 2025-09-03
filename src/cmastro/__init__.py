"""
cmastro: colormaps for astronomers
"""

from .cm import (
    cmaps,
    emph,
    emph_r,
    hesperia,
    hesperia_r,
    lacerta,
    lacerta_r,
    laguna,
    laguna_r,
    unph,
    unph_r,
)

try:
    from .version import version as __version__
except ImportError:
    __version__ = ""


__all__ = [
    "cmaps",
    "hesperia",
    "laguna",
    "lacerta",
    "emph",
    "unph",
    "hesperia_r",
    "laguna_r",
    "lacerta_r",
    "emph_r",
    "unph_r",
]

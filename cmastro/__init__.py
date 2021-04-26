"""
cmastro: colormaps for astronomers
"""

from .cm import cmaps

try:
    from .version import version as __version__
except ImportError:
    __version__ = ''

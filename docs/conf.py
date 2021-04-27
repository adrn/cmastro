# -*- coding: utf-8 -*-

import os
import pathlib
import sys
import datetime
from importlib import import_module
import warnings

# Get configuration information from setup.cfg
from configparser import ConfigParser
conf = ConfigParser()

conf.read([os.path.join(os.path.dirname(__file__), '..', 'setup.cfg')])
setup_cfg = dict(conf.items('metadata'))

# -- General configuration ----------------------------------------------------

# By default, highlight as Python 3.
highlight_language = 'python3'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

autosummary_generate = True
automodapi_toctreedirnm = 'api'

# The reST default role (used for this markup: `text`) to use for all
# documents. Set to the "smart" one.
default_role = 'obj'

# Class documentation should contain *both* the class docstring and
# the __init__ docstring
autoclass_content = "both"

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'numpydoc',
    'matplotlib.sphinxext.plot_directive'
]

# intersphinx
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'matplotlib': ('https://matplotlib.org/', None)
}

# -- Project information ------------------------------------------------------

# This does not *have* to match the package name, but typically does
project = setup_cfg['name']
author = setup_cfg['author']
copyright = '{0}, {1}'.format(
    datetime.datetime.now().year, setup_cfg['author'])

import_module(project)
package = sys.modules[project]

# The short X.Y version.
version = package.__version__.split('-', 1)[0]
# The full version, including alpha/beta/rc tags.
release = package.__version__


# -- Options for HTML output ---------------------------------------------------

html_theme = 'pydata_sphinx_theme'

# html_logo = '_static/Gala_Logo_RGB.png'

html_theme_options = {
    "logo_link": "index",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/adrn/cmastro",
            "icon": "fab fa-github-square",
        }
    ]
}

# Static files to copy after template files
# html_static_path = ['_static']
# html_css_files = [
#     "cmastro.css"
# ]

plot_apply_rcparams = True
plot_rcparams = mpl_style = {
    'font.size': 16,

    'figure.titlesize': 'x-large',

    # Axes
    'axes.titlesize': 'large',
    'axes.labelsize': 'large',
    'axes.axisbelow': True,

    'xtick.labelsize': 'medium',
    'ytick.labelsize': 'medium',

    'figure.dpi': 300,
    'savefig.dpi': 300,
}

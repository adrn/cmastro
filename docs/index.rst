.. module:: cmastro

************************************
`cmastro`: colormaps for astronomers
************************************

This package contains custom colormaps that have been used in various
astronomical applications, similar to `cmocean for oceanography
<https://matplotlib.org/cmocean/>`_. The colormaps are available as raw data
files through the `GitHub source repository
<https://github.com/adrn/cmastro/tree/main/cmastro/cmaps>`_, or available to use
(through this Python package) as `matplotlib colormaps
<https://matplotlib.org/stable/tutorials/colors/colormaps.html>`_.


Meet the colormaps
==================

.. TODO: like matplotlib, split into sequential, diverging, cyclic?

.. plot::
    :align: center
    :context: close-figs
    :width: 90%

    from cmastro import cmaps
    from cmastro.plot import plot_all_colormaps
    fig, _ = plot_all_colormaps(cmaps)


Installation
============

`cmastro` is available via `pip`, which is the recommended installation method.
To install the latest stable version using `pip`, use::

    python -m pip install cmastro

To install the latest development version::

    python -m pip install git+https://github.com/adrn/cmastro


Contributing new colormaps
==========================

We welcome new contributed colormaps from anyone via pull requests on `GitHub
<https://github.com/adrn/cmastro>`_. If you don't feel comfortable modifying or
adding functionality, we also welcome feature requests and bug reports as
`GitHub issues <https://github.com/adrn/cmastro/issues>`_.


The colormaps in detail
=======================

TODO:

.. plot::
    :align: center
    :context: close-figs
    :width: 90%

    from cmastro.plot import plot_all_colormaps
    fig, _ = plot_all_colormaps(cmaps, grayscale=True)

.. plot::
    :align: center
    :context: close-figs
    :width: 90%

    from cmastro.plot import plot_lightness
    fig, _ = plot_lightness(cmaps)

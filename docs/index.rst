.. module:: cmastro

**********************************
`cmastro`: colormaps for astronomy
**********************************


The Colormaps
=============

.. plot::
    :align: center
    :context: close-figs
    :width: 65%

    from cmastro.plot import plot_all_colormaps
    fig, _ = plot_all_colormaps()

    fig, _ = plot_all_colormaps(grayscale=True)


.. plot::
    :align: center
    :context: close-figs

    from cmastro.plot import plot_lightness
    fig, _ = plot_lightness()


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

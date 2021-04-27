#!/usr/bin/env python
# Licensed under an MIT license - see LICENSE

import os

from setuptools import setup

VERSION_TEMPLATE = """
# Fall back to the hard-coded version if either setuptools_scm can't be
# imported or setuptools_scm can't determine the version
try:
    from setuptools_scm import get_version
    version = get_version(root='..', relative_to=__file__)
except Exception:
    version = '{version}'
""".lstrip()

setup(use_scm_version={'write_to': os.path.join('cmastro', 'version.py'),
                       'write_to_template': VERSION_TEMPLATE})

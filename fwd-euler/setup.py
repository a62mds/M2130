#!/usr/bin/env python
# setup.py

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '<++>',
    'author': '<++>',
    'url': '<++>',
    'download_url': '<++>',
    'author_email': '<++>',
    'version': '<++>',
    'install_requires': ['nose,<++>'],
    'packages': ['fwd-euler'],
    'scripts': ['<++>'],
    'name': 'fwd-euler'
}

setup(**config)

#EOF

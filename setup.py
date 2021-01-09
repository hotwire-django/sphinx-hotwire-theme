#!/usr/bin/env python

import codecs
from setuptools import setup

# Version info -- read without importing
_locals = {}
with open("alabaster_hotwire/_version.py") as fp:
    exec(fp.read(), None, _locals)
version = _locals["__version__"]

# README into long description
with codecs.open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="alabaster_hotwire",
    version=version,
    description="A fork of Alabaster to match the Hotwire.dev style",
    long_description=readme,
    author="Jeff Forcier",
    author_email="jeff@bitprophet.org",
    url="https://github.com/hotwire-django/sphinx-hotwire-theme",
    packages=["alabaster_hotwire"],
    include_package_data=True,
    entry_points={"sphinx.html_themes": ["alabaster_hotwire = alabaster_hotwire"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
    ],
)

========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |github-actions| |codecov|
    * - package
      - |version| |wheel| |supported-versions| |supported-implementations| |commits-since|
.. |docs| image:: https://readthedocs.org/projects/wonderwaller/badge/?style=flat
    :target: https://readthedocs.org/projects/wonderwaller/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/msgtn/wonderwaller/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/msgtn/wonderwaller/actions

.. |codecov| image:: https://codecov.io/gh/msgtn/wonderwaller/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://app.codecov.io/github/msgtn/wonderwaller

.. |version| image:: https://img.shields.io/pypi/v/wonderwaller.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/wonderwaller

.. |wheel| image:: https://img.shields.io/pypi/wheel/wonderwaller.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/wonderwaller

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/wonderwaller.svg
    :alt: Supported versions
    :target: https://pypi.org/project/wonderwaller

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/wonderwaller.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/wonderwaller

.. |commits-since| image:: https://img.shields.io/github/commits-since/msgtn/wonderwaller/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/msgtn/wonderwaller/compare/v0.0.0...main



.. end-badges

lerobot hackathon

* Free software: BSD 2-Clause License

Installation
============

::

    pip install wonderwaller

You can also install the in-development version with::

    pip install https://github.com/msgtn/wonderwaller/archive/main.zip


Documentation
=============


https://wonderwaller.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

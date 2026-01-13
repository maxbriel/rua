Building Documentation
======================

This guide explains how to build the Rua documentation locally.

Prerequisites
-------------

Install the documentation dependencies::

    pip install -e ".[docs]"

Or install from the requirements file::

    pip install -r docs/requirements.txt

Building HTML Documentation
---------------------------

To build the HTML documentation, navigate to the docs directory and run::

    cd docs
    make html

The built documentation will be in ``docs/_build/html/``. Open ``docs/_build/html/index.html`` in your browser to view it.

Building PDF Documentation
--------------------------

To build PDF documentation (requires LaTeX)::

    cd docs
    make latexpdf

Other Formats
-------------

Sphinx supports many output formats. To see all available formats::

    cd docs
    make help

Common formats include:

- ``html`` - HTML pages
- ``dirhtml`` - HTML pages with directory structure
- ``singlehtml`` - Single HTML page
- ``latex`` - LaTeX files
- ``latexpdf`` - PDF via LaTeX
- ``epub`` - EPUB ebook

Cleaning Build Files
--------------------

To clean the build directory::

    cd docs
    make clean

Auto-building Documentation
----------------------------

For development, you can use sphinx-autobuild to automatically rebuild documentation on changes::

    pip install sphinx-autobuild
    cd docs
    sphinx-autobuild . _build/html

This will start a local server at http://127.0.0.1:8000 and automatically rebuild when you save changes.

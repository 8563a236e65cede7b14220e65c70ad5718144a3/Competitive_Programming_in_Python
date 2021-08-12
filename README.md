Competitive Programming in Python
=================================

Introduction
------------

This repository contains solutions to Competitive Programming in Python by Durr and Vie.
The solutions are from working through the textbook and transcribing the algorithms
into my own source files.

Documentation
-------------

To build the documentation you will need to have a working LaTeX installation. On Debian, this can be
achieved with

    sudo apt install texlive-full
    sudo apt install texlive-latex-extra

You will also need Sphinx and the Read the Docs Theme

    python3.9 -m pip install sphinx sphinx_rtd_theme

You can then create the documentation as follows

    cd docs/
    make clean && make html


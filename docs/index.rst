******************************
One Code Python Client Library
******************************

Introduction
============

This package provides 3 major pieces of functionality: (1) a core Python client
library; (2) a simple CLI for interacting with the `One Codex platform
<https://onecodex.com>`_ that uses that core library; and (3) optional
extensions to the client library, which offers many features aimed at advanced
users and provides functionality for use in interactive notebook environments
(e.g., Jupyter notebooks).

For installation instructions and instructions on using the command-line
client, see the :doc:`readme`. You can find the source code on `GitHub
<https://github.com/onecodex/onecodex>`_.

.. toctree::
   :maxdepth: 4
   :caption: Contents
   :hidden:
   :glob:
   :titlesonly:

   index
   ReadMe <readme>
   quickstart
   models
   sample_collection
   notebooks

Getting Started
===============

Installation
------------

.. code-block:: bash

   # The CLI (and core Python library)
   pip install onecodex

   # Optional dependencies (visualization, analysis and reports)
   pip install onecodex[all]


Tutorials
---------

For documentation and examples of common uses of the client library including
interactive data analysis and plotting within Jupyter notebooks see
:doc:`notebooks`.

CLI
===

The Python package also comes with a command-line tool which can be used to
upload samples to One Codex as well as results from the API. See
:doc:`readme` for more information.

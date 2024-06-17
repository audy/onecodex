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

.. contents::
   :depth: 3
   :backlinks: top

.. toctree::
   :maxdepth: 4
   :caption: Contents
   :hidden:
   :glob:

   onecodex.notebooks

Getting Started
===============

Installation
------------

.. code-block:: bash

   # The CLI (and core Python library)
   pip install onecodex

   # Optional dependencies (visualization, analysis and reports)
   pip install onecodex[all]


Quickstart
----------

.. code-block:: python

   import onecodex

   # Instantiate the API (run onecodex login first)
   ocx = onecodex.Api()

   # Fetch some samples
   samples = ocx.Samples.all()

   # Generate a Pandas DataFrame from classification results
   results = samples.to_df()

   # Plot a bar graph
   samples.plot_bargraph()


Tutorials
---------

For documentation and examples of common uses of the client library including
interactive data analysis and plotting within Jupyter notebooks see
:doc:`Notebooks Demo <notebook_examples/notebooks_demo>`.

CLI
===

The Python package also comes with a command-line tool which can be used to
upload samples to One Codex as well as results from the API. See
:doc:`readme` for more information.

Module Documentation
====================

`onecodex.Api`
--------------

.. autoclass:: onecodex.api.Api
   :members:

Models (Main)
-------------

.. autoclass:: onecodex.models.misc.Documents
   :members:
   :show-inheritance:

.. autoclass:: onecodex.models.misc.Jobs
   :members:
   :show-inheritance:

.. autoclass:: onecodex.models.misc.Projects
   :members:
   :show-inheritance:

.. autoclass:: onecodex.models.sample.Samples
   :members:
   :show-inheritance:

.. autoclass:: onecodex.models.misc.Tags
   :members:
   :show-inheritance:

.. autoclass:: onecodex.models.misc.Users
   :members:
   :show-inheritance:

Models (Analyses)
-----------------

.. autoclass:: onecodex.models.analysis.Analyses
   :members:
   :show-inheritance:

.. autoclass:: onecodex.models.analysis.Alignments
   :members:
   :show-inheritance:

.. autoclass:: onecodex.models.analysis.Classifications
   :members:
   :show-inheritance:

.. autoclass:: onecodex.models.analysis.Panels
   :members:
   :show-inheritance:

.. autoclass:: onecodex.models.misc.Assets
   :members:
   :show-inheritance:


Plotting and Analysis: `SampleCollection`
-----------------------------------------

.. autoclass:: onecodex.models.collection.SampleCollection
   :members:
   :show-inheritance:

Exceptions
----------

.. automodule:: onecodex.exceptions
   :members:

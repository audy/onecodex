import os
import datetime

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "One Codex"
copyright = f"{str(datetime.datetime.now().year)}, One Codex"
author = "One Codex"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "nbsphinx", "myst_parser"]

nbsphinx_execute = "always"
nbsphinx_allow_errors = True

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "venv"]

html_logo = "_static/one_codex_logo.png"

html_sidebars = {
    "**": [
        "globaltoc.html",  # ToC tree, shows all sections and subsections
        "relations.html",  # Contextual links (previous, next)
        "sourcelink.html",  # Link to source code
        "searchbox.html",  # Search box
    ]
}

import sys

sys.path.insert(0, os.path.abspath("../"))


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ["_static"]

# Set default options for autodoc directives
autodoc_default_options = {
    "inherited-members": True,  # Automatically document inherited members
}

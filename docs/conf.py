# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Chemical Complexity of Diet'
copyright = '2019, Albert-László Barabási et al'
author = 'Albert-László Barabási, Giulia Menichetti and Joseph Loscalzo'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_immaterial",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_immaterial'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ["custom.css"]


html_sidebars = {
    "**": ["about.html", "navigation.html", "searchbox.html"],
}
html_title = 'Chemical Complexity of Diet'
html_logo = '_static/media/onto-logo.svg'
html_favicon = '_static/media/onto-favicon.svg'

# material theme options (see theme.conf for more information)
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github-square",
    },
    "site_url": "https://isolveit.github.io/chem-complexity-diet/",
    "repo_url": "https://github.com/iSOLveIT/chem-complexity-diet",
    "repo_name": "Chem-Complexity-Diet",
    "repo_type": "github",
    "edit_uri": "blob/main/docs/",
    "globaltoc_collapse": True,
    "features": [
        # "navigation.expand",
        # "navigation.tabs",
        # "toc.integrate",
        # "navigation.sections",
        # "navigation.instant",
        # "header.autohide",
        "navigation.top",
        # "navigation.tracking",
        # "search.highlight",
        "search.share",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "blue",
            "accent": "teal",
            "toggle": {
                "icon": "material/weather-night",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "blue",
            "accent": "teal",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "Switch to light mode",
            },
        },
    ],
    "toc_title_is_page_title": True,
}

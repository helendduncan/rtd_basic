# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html



# -- Project information -----------------------------------------------------

project = "Test"
author = "Helen"
development_branch = "all_of_em"


# -- Customisation  -----------------------------------------------------------


# Set sidebar variables
if "html_context" not in globals():
    html_context = dict()


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx_togglebutton",
    "sphinxcontrib.typer",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "**/*.partial.md",
    "deployment/security_checklist/security_checklist_template.md",
]
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "pydata_sphinx_theme"

# Options for the chosen theme
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/helendduncan/rtd_basic",
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        }
    ],
    "secondary_sidebar_items": ["page-toc", "edit-this-page", "sourcelink"],
    "use_edit_page_button": True,
    "header_links_before_dropdown": 6
}

# Location of favicon
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["overrides.css"]
html_js_files = ["toggle.js"]


# -- Options for MyST  --------------------------------------------------------

# MyST extensions to enable
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "substitution",
]

# Allow MyST to generate anchors for section titles
myst_heading_anchors = 4

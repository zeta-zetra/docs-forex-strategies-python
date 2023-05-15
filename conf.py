# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project   = 'Forex Strategies'
copyright = '2023, Zetra'
author    = 'Zetra'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_favicon"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

favicons = [
    "favicon-16x16.png",
    "favicon-32x32.png",
    "favicon.ico",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_js_files = ["js/google_analytics.js", "js/google_tag.js"]

html_title = "Forex Strategies"

html_logo = "_static/images/logo.png"

html_theme_options = {
    
    "home_page_in_toc": True

}
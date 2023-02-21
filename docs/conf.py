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
import platform
import os
import sys
sys.path.insert(0, os.path.abspath('../util/'))
import sphinx_video

# -- Project information -----------------------------------------------------

project = 'ODK'
copyright = '2023 Get ODK Inc. Licensed under CC BY 4.0.'
author = 'ODK'

# The full version, including alpha/beta/rc tags
# release = 'v1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'sphinxcontrib.spelling',
    'sphinx_design',
    'sphinx_copybutton',
    'sphinx_video',
    'sphinxcontrib.youtube',
    'sphinx_tabs.tabs'
]

# If using Apple Silicon, set env variable (assumes brew install of enchant)
if 'arm' in platform.processor():
    os.environ['PYENCHANT_LIBRARY_PATH'] = '/opt/homebrew/lib/libenchant-2.dylib' 

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

html_title = 'ODK Docs'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ['_static']

html_css_files = [
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.2/css/all.min.css',
    'css/custom.css',
]

html_js_files = [
    ('https://helper.getodk.org/script.js', {'defer': 'defer', 'data-site': 'PBSTMJFG'}),
    'js/custom.js',
]

html_theme_options = {
    'light_css_variables': {
        'color-brand-primary': '#009ECC',
        'color-brand-content': '#009ECC',
        'color-announcement-background': '#1a1c1e',
        'color-announcement-text': '#ffffffcc',
    },
    'dark_css_variables': {
        'color-brand-primary': '#009ECC',
        'color-brand-content': '#009ECC',
        'color-announcement-background': '#f8f9fb',
        'color-announcement-text': 'black',
    },
    'announcement': '<b>Looking to save time?</b> Try <a href="https://getodk.org/#pricing" onclick="fathom.trackGoal("SMIXEGNN", 0);">ODK Cloud</a>, the official managed hosting service from the creators of ODK.',
    'sidebar_hide_name': True,
}
html_show_sphinx = True

html_copy_source = False

html_favicon = '_static/img/odk-favicon.ico'
html_logo = '_static/img/odk-logo.svg'

spelling_word_list_filename='spelling_wordlist.txt'

# Smart (q)uotes, (D)ashes, and (e)llipses
smartquotes = True
smartquotes_action = 'De'

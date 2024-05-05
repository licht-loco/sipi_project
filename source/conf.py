import os
import sys

# Добавить корневую директорию проекта в PYTHONPATH
sys.path.insert(0, os.path.abspath('../'))
# -- Project information -----------------------------------------------------
project = 'schedule_bot'
copyright = '2024'
author = 'licht'
release = '1.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ru'

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']

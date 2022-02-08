# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Expresso'
copyright = '2022, STI/GEGOV'
author = 'GEGOV'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_style = 'css/expressotheme.css'

html_static_path = ['']
html_logo = 'logo-expresso-branca.svg'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'style_nav_header_background': '#0B7675',
}
# -- Options for EPUB output
epub_show_urls = 'footnote'

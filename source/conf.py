# -*- coding: utf-8 -*-
#
# Mixxx documentation build configuration file, created by
# sphinx-quickstart on Wed Dec 11 12:10:20 2013.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import sphinx_rtd_theme

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.graphviz",
    "sphinxcontrib.rsvgconverter",
    "sphinx_rtd_theme",
    "sphinx_multiversion",
    "sphinx_mixxx",
]

todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = {
    ".rst": "restructuredtext",
}

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = u"Mixxx"
copyright = u"2011-2020, The Mixxx Development Team"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "2.4"
# The full version, including alpha/beta/rc tags.
release = "2.4.0"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = "en"

supported_languages = {
    "ca": "Català",
    "cs": "Čeština",
    "de": "Deutsch",
    "de-DE": "Deutsch (Deutschland)",
    "en": "English",
    "en-GB": "English (UK)",
    "es": "Español",
    "es-ES": "Español (España)",
    "es-MX": "Español (Mexico)",
    "fi": "Suomi",
    "fr": "Français",
    "gl": "Galego",
    "id": "Bahasa Indonesia",
    "it": "Italiano",
    "ja-JP": "日本語",
    "kn": "ಕನ್ನಡ",
    "nl": "Nederlands",
    "pl": "Polszczyzna",
    "pt": "Português",
    "pt-BR": "Português (Brasil)",
    "ro": "Română",
    "ru": "Русский",
    "ru-RU": "Русский (Росси́я)",
    "sl": "Slovenščina",
    "sq": "Shqip",
    "sr": "Српски Језик",
    "tr": "Türkçe",
    "zh-CN": "中文 (中国)",
    "zh-TW": "中文 (臺灣)",
}

smv_tag_whitelist = r"^$"
smv_branch_whitelist = r"^(main|(\d+)\.(\d+))$"
smv_remote_whitelist = r"^origin$"
smv_released_pattern = r"^.*/(?!2\.3)(\d+)\.(\d+)$"
smv_latest_version = r"2.2"
smv_outputdir_format = "{config.version}/{config.language}"

# Directories in which to search for additional message catalogs (see language),
# relative to the source directory. The directories on this path are searched
# by the standard gettext module.
locale_dirs = [
    "locale",
]

# If true, a document`s text domain is its docname if it is a top-level project
# file and its very base directory otherwise. By default, the document
# markup/code.rst ends up in the markup text domain. With this option set to False,
# it is markup/code.
gettext_compact = False

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Enable "Edit on GitHub" links.
html_context = {
    "display_github": True,
    "github_user": "mixxxdj",
    "github_repo": "manual",
    "github_version": "manual-2.2.x",
    "conf_py_path": "/source/",
    "language": language,
    "supported_languages": list(
        sorted(supported_languages.items(), key=lambda x: x[1])
    ),
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ["themes"]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Mixxx User Manual"

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/mixxx-icon-logo-symbolic.svg"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    "css/mixxx.css",
    "css/widget-sidebar.css",
]

html_js_files = [
    "js/widget-sidebar.js",
]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%b %d, %Y"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    "**": [
        "download.html",
        "languages.html",
        "versioning.html",
    ],
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "Mixxxdoc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
    # Remove blank duplex printing pages from generated PDF
    # http://stackoverflow.com/questions/5422997
    "classoptions": ",openany,oneside",
    "babel": "\\usepackage[english]{babel}",
}
latex_use_xindy = False

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        "index",
        "Mixxx-Manual.tex",
        u"Mixxx User Manual",
        u"The Mixxx Development Team",
        "manual",
        True,
    ),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "_static/mixxx_logo_color_medium.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        "index",
        "mixxx",
        u"Mixxx User Manual",
        [u"The Mixxx Development Team"],
        1,
    )
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "Mixxx",
        u"Mixxx User Manual",
        u"The Mixxx Development Team",
        "Mixxx",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u"Mixxx User Manual"
epub_author = u"The Mixxx Development Team"
epub_publisher = u"The Mixxx Development Team"
epub_copyright = u"2011-2020, The Mixxx Development Team"

# The basename for the epub file. It defaults to the project name.
# epub_basename = u'Mixxx'

# The HTML theme for the epub output. Since the default themes are not optimized
# for small screen space, using the same theme for HTML and epub output is
# usually not wise. This defaults to 'epub', a theme designed to save visual
# space.
# epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
# epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
# epub_identifier = ''

# A unique identification for the text.
# epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
# epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
# epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_post_files = []

# A list of files that should not be packed into the epub file.
# epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
# epub_tocdepth = 3

# Allow duplicate toc entries.
# epub_tocdup = True

# Choose between 'default' and 'includehidden'.
# epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
# epub_fix_images = False

# Scale large images.
# epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# epub_show_urls = 'inline'

# If false, no index is generated.
# epub_use_index = True

# Ignore links to GitHub Pull Requests to avoid "429 Client Error" due to
# GitHub's rate limiting
linkcheck_ignore = [r"^https://github.com/mixxxdj/mixxx/pull/\d+$"]

# Avoid freezing during linkcheck
linkcheck_timeout = 5

import pages_demo

#sys.path.insert(0, os.path.abspath('../quants_models'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
]

#nitpicky = True

project = pages_demo.__name__
release = pages_demo.__version__

today_fmt = "%d %B, %y"

html_theme = "sphinxdoc"

#default_role = 'math'
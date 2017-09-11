**Templates and Themes**
========================  

**Templates**
--------------

.. docs-tech-guide:

**Templates** contain variables, which are replaced with values when the template is evaluated, tags, which control the logic of the template and blocks which are used for template inheritance. Refer to `the official Sphinx doc <http://www.sphinx-doc.org/en/stable/templating.html>`_ for furthur information. 

Sphinx's basic theme consists of base templates and child templates. The base template contains all the common elements of your site. It contains blocks that are defined for different sections of the html that are overidden by the child templates.

For example lets take a template call named layout.html .Here the {% block %} tags define four blocks that child templates can fill in. All the block tag does is tell the template engine that a child template may override those portions of the template.

**Base Template**
~~~~~~~~~~~~~~~~~~

.. code-block:: html
	
	<!doctype html>
		<html>
  		<head>
    		{% block head %}
    		<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    		<title>{% block title %}{% endblock %} - My Webpage</title>
    		{% endblock %}
  		</head>
  		<body>
    		<div id="content">{% block content %}{% endblock %}</div>
    		<div id="footer">
      		{% block footer %}
      		&copy; Copyright 2010 by <a href="http://domain.invalid/">you</a>.
      		{% endblock %}
    		</div>
  		</body>
		</html>


**Child Template**
~~~~~~~~~~~~~~~~~~~
.. code-block:: python

	{% extends "structure.html" %}
		{% block title %}Index{% endblock %}
		{% block head %}
  		{{ super() }}
  		<style type="text/css">
    		.important { color: #336699; }
  		</style>
		{% endblock %}
		{% block content %}
  		<h1>Index</h1>
  		<p class="important">
    		Welcome on my awesome homepage.
		{% endblock %}


The {% extends %} tag will help extend to another template. Caution: extends must be mentioned in the first column so that the child template can identify its template. Furthurmore, the blocks belonging to the parent can be rendered in the child template using {{ super() }}.
For more information on blocks, you may refer to `this <http://www.sphinx-doc.org/en/stable/templating.html>`_.

**Themes**
----------

**Theme** is basically a collection of HTML Templates,stylesheet(s) and other static files. It helps in customising the appearance of the 		Website according to user preferences. For more information, you may refer to the `Sphinx Official Documentation on Themes <http://www.sphinx-doc.org/en/1.5.1/theming.html#using-a-theme>`_ .

**Template Overriding to customise themes**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To change the theme, override the template by copying the relevant template file, and then working on it. In your doc, you use a theme be it the default one or a custom one. Refer to `sphinx-better-theme readthedocs documentation <http://sphinx-better-theme.readthedocs.io/en/latest/guide.html>`_ for more information.

**Template Extention**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We need to keep in mind the order in which Sphinx searches for templates:
First, in the user’s templates_path directories.Then, in the selected theme.Then, in its base theme, its base’s base theme, etc.

**About 'Read the Docs' Theme**
--------------------------------------------

Read the docs is part of  Sphinx's official documentation `as described here <http://docs.readthedocs.io/en/latest/theme.html>`_. 

You may find the original template files in the following location in your virtualenv directory '/odk/odkenv/lib/python3.5/site-packages/sphinx_rtd_theme/'.

You can refer to the latest changes in the 'read the docs' theme ` here <http://ericholscher.com/blog/2013/nov/4/new-theme-read-the-docs/>`_.

**Custom.css and Custom.js**
-----------------------------

**Custom.css**
~~~~~~~~~~~~~~~

In order to extend the theme used by Sphinx and ReadTheDocs with your own custom styles, you will have to add the given lines in the **conf.py** file.

.. code-block:: python

	def setup(app):
	    app.add_stylesheet('css/custom.css')  # may also be an URL

and then  putting the file into the **_static/css/** folder.

**Custom.js**
~~~~~~~~~~~~~~

This can be done with a template:

Create a folder called templates in the Sphinx project directory.
In conf.py, add

.. code-block:: python

	templates_path = ["templates"]

In the templates directory, create a file called layout.html with the following contents:

.. code-block:: python

	{% extends "!layout.html" %}
	{%- block extrahead %} 
	 <script type="text/javascript">
  	     MathJax.Hub.Config({
  	         "HTML-CSS": {
  	             scale: 90
  	         }
  	     });
  	</script>      
	{% endblock %}

The <script> element will be included in the <head> of every generated HTML page.The extrahead template block is empty by default. Now yoy can replace extrahead with title, footer, etc according to how to how you wish to customise your theme.

**JINJA**
----------

Jinja2 is a template engine for Python.  You can use it when rendering data to web pages.  For every link you visit, it shows the data with the formatting.

Learn to code in Jinja by referring to the  `Jinja Documentation <http://jinja.pocoo.org/docs/2.9/>`_ . 

**Sphinx Development**
----------------------

More on Sphinx Development:
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `Sphinx & Read the Docs <https://www.youtube.com/watch?v=oJsUvBQyHBs&t=483s>`_
* `Quickstart to Sphinx <https://pythonhosted.org/an_example_pypi_project/sphinx.html>`_

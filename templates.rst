***********************
Templates and Themes
***********************

Templates
==============

.. docs-tech-guide:

**Templates** contain:

- **Variables**: They are replaced with values when the template is evaluated.

- **Tags**: They control the logic of the template

- **Blocks**: They are used for template inheritance.

You may refer to `the official Sphinx docs <http://www.sphinx-doc.org/en/stable/templating.html>`_ for furthur information. 

Sphinx's basic theme consists of:

1. **Base templates** : The base template contains all the common elements of your site. It contains blocks that are defined for different sections of the html.


2. **Child templates**: The blocks in the base template are overidden by the child templates.

Template Extention and blocks
----------------------------------
As explained above, the *blocks* in the base template can be overriden or extended by a new template file(child template) by calling **{% extend %}** and then defining the blocks that you wish to override. 

.. warning::

	The template that the child template extends has to be specified at the beginning of the code.

For furthur information on the **types of blocks** kindly refer to  *Working with the builtin templates* section in the  `original Sphinx Documentation <http://www.sphinx-doc.org/en/stable/templating.html>`_ .

Themes
=======

**Theme** is basically a collection of:
 
	1. HTML Templates
	2. stylesheet(s) 
	3. other static files

**Importance of Themes**:  It helps in customising the appearance of the Website according to user specifications.

For more information, you may refer to the `Sphinx Official Documentation on Themes <http://www.sphinx-doc.org/en/1.5.1/theming.html#using-a-theme>`_ .

About 'Read the Docs' Theme
============================

*ReadTheDocs* is part of  Sphinx's official documentation as described `here <http://docs.readthedocs.io/en/latest/theme.html>`_. 
You may find the original template files in the following location in your virtualenv directory:
 
.. code-block:: rst

	/{your_virtualenv_directory}/lib/python3.5/site-packages/sphinx_rtd_theme/.

Customizing Read The Docs theme
===============================

Overriding a html page
-----------------------

In order to override the html template,

**Step 1:** Go to _templates dir

**Step 2:** Create a file with a name same as that of the one you wish to override.

In this template, you have access to the pagename (relative doc path of each file). Knowing that, you can make some conditional check in this template to detect if this is a file you want to override & then override it. If it is not a file which needs to be overridden, simply fallback on the default behavior. For example:

.. code-block:: python

	{% extends "layout.html" %}
	{% block body %}
    	{% if pagename == 'index' %}
        	{% include 'custom/index.html' %}
    	{% else %}
        	{{ body }}
    	{% endif %}
	{% endblock %}

Adding your custom CSS
----------------------

In order to extend the theme used by Sphinx and ReadTheDocs with your own custom styles, you will have to add the given lines to the **conf.py** file.

.. code-block:: python

	def setup(app):
    	app.add_stylesheet('css/custom.css')  # may also be an URL


and then put your custom css file into the **_static/css/** folder.

.. note::
	Templates with the same name in the templates_path override templates supplied by the selected theme.
	

Adding your custom JS
---------------------

This can be done using a template:

**Step 1**: Create a folder called templates in the Sphinx project directory.

**Step 2**: In conf.py, verify that

.. code-block:: python

	templates_path = ["_templates"]

Sphinx will look for templates in the folders of templates_path first, and if it can’t find the template it’s looking for there, it falls back to the selected theme’s templates.

**Step 3**:In the templates directory, create a file called **layout.html** with the following contents:

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

-The **<script>** element will be included in the **<head>** of every generated HTML page.

-The extrahead template block is empty by default.

**Step 4**:  Now you can replace extrahead with title, footer, etc according your specifications  .

Jinga
=======

Jinja2 is a template engine for Python.  You can use it when rendering data to web pages.  For every link you visit, it shows the data with the formatting.

Learn to code in Jinja by referring to the  `Jinja Documentation <http://jinja.pocoo.org/docs/2.9/>`_ . 

References
============

More on Sphinx Development:
----------------------------

* `Sphinx & Read the Docs <https://www.youtube.com/watch?v=oJsUvBQyHBs&t=483s>`_
* `Quickstart to Sphinx <https://pythonhosted.org/an_example_pypi_project/sphinx.html>`_

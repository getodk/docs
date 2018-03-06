Docs Developer Guide
=======================

This document is for contributors working on the design, templating, deployment, or development of the ODK Docs website.

.. _tech-overview:

Tech Overview
----------------

ODK Docs uses:

- Sphinx_, a static-site generator written in Python_

  Sphinx uses:

  - Docutils_ for parsing reStructuredText_
  - Jinja_ for templating

- sphinx_rtd_theme_, a Sphinx theme/template

  sphinx_rtd_theme uses:

  - JQuery_, a JavaScript library

- Proselint_ for style testing
- git_ and GitHub_ for version control
- CircleCI_ for testing and deployment
- `Amazon S3`_ for hosting


.. _sphinx: http://www.sphinx-doc.org/
.. _python: https://www.python.org/
.. _docutils: http://docutils.sourceforge.net/
.. _restructuredtext: http://docutils.sourceforge.net/rst.html
.. _jinja: http://jinja.pocoo.org/
.. _sphinx_rtd_theme: https://github.com/rtfd/sphinx_rtd_theme
.. _proselint: http://proselint.com/
.. _git: https://git-scm.com/
.. _github: https://github.com/opendatakit/docs
.. _circleci: https://circleci.com/
.. _Amazon S3: https://aws.amazon.com/s3/


.. _custom-html:

Custom HTML templating
-------------------------

ODK Docs uses the sphinx_rtd_theme_,
with some minor customizations.

ODK-specific versions of HTML/Jinja templates
are in :file:`_templates`.
Any file in that directory
will override the file of the same name
in the sphinx_rtd_theme source.

So, to customize a portion of the HTML template,
copy the source file from sphinx_rtd_theme
and then edit it.

Please commit the copied file unchanged before editing,
so that it is easy to track what you have changed.

.. _custom-js:

Custom JavaScript
-------------------

Custom JavaScript should be added in :file:`src/_static/js/custom.js`.
Comment your code with an explanation of what the JS accomplishes,
and a reference to the issue number you are working on.

The ODK Docs template includes JQuery_,
so you can use it in your custom JS.

.. _JQuery: https://jquery.com/

.. _custom-css:

Custom CSS
------------

Custom CSS should be added in :file:`src/_static/css/custom.css`.
Comment your code with an explanation of what the CSS accomplishes
and a reference to the issue number you are working on.

For example:

.. code-block:: css

  /* Example CSS PR #xyx */

  div[class^='example'] {
    color: black;
  }

It is helpful to keep the CSS file organized.
There are several sections in the :file:`custom.css` file:

- Styling for rst roles and directives
- Responsive CSS
- Styling for JS implementation
- Utility classes

Each of these sections are enclosed in start and end comments.
Add your code to the relevant section.
If you don't find any section relevant,
add a new section and add your code there.

For example:

.. code-block:: css

  /* New section starts */

  /* Example CSS PR #xyx */

  div[class^='example'] {
    color: black;
  }

  /* New section ends */

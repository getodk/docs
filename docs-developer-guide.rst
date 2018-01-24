Docs Developer Guide
=======================

This document is for contributors working on the design, templating, deployment, or development of the ODK Docs website.

.. warning:: This page is a work in progress.

.. _custom-css:

Custom CSS
------------

You can add custom styling in :file:`_static/css/custom.css`. Whenever you add any custom styling, add short comments describing the changes made and the PR number in which the changes were made.

For example:

.. code-block:: css

  /* Example css PR #xyx */

  div[class^='example'] {
    color: black;
  }

There are various sections in the :file:`custom.css` file:

- Styling for rst roles and directives
- Responsive css
- Styling for JS implementation
- Utility classes

Each of these sections are enclosed between start and end comments. Make sure you add your code to the relevant section. If you don't find any section relevant, add a new section and add your code there.

For example:

.. code-block:: css

  /* New section starts */

  /* Example css PR #xyx */

  div[class^='example'] {
    color: black;
  }
  
  /* New section ends */ 

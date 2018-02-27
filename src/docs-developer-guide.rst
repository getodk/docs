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

.. _style-tests:

Style Guide checks
--------------------

Proselint_  is used for style testing the docs.
Apart from the built-in tests in proselint,
custom checks are added for style guide testing.
Following a `literate programming <https://en.wikipedia.org/wiki/Literate_programming>`_. model,
style checks are defined in :doc:`docs-style-guide.rst <docs-style-guide>`.
After each style rule,
you can define a python code-block
containing the code for style testing.
When the style-test script is run,
these python code-blocks are parsed to
generate a testing script.

.. _proselint-checks:

Proselint dependent checks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In most of the custom checks,
a new function is written
that calls one of the built-in proselint functions as a return value.

All the checks use a decorator :py:func:`memoize`
to cache the check for faster execution.

.. py:function:: memoize

  Use :py:data:`@memoize` above function definition to cache the result.

Proselint provides several functions for defining style tests:

.. py:function:: existence_check(text, list, err, msg, ignore_case=True, \
                                 str=False, max_errors=float("inf"), offset=0, \
                                 require_padding=True, dotall=False, \
                                 excluded_topics=None, join=False)

  To check for existence of a regex pattern(s) in the text.
  The parameters :py:data:`offset`, :py:data:`excluded_topics` and :py:data:`join`
  are not needed for style guide testing.

  :param str text: Text to be checked
  :param list list: List of regex expressions
  :param str err: Name of the test
  :param str msg: Error or warning message
  :param bool ignore_case: For using :py:data:`re.IGNORECASE`
  :param bool str: For using :py:data:`re.UNICODE`
  :param float max_errors: Maximum number of errors to be generated
  :param bool require_padding: To use padding with the specified regex (It is better to set it as **False** and specify the regex accordingly)
  :param bool dotall: For using :py:data:`re.DOTALL`
  :return: The error list consisting of error tuples: :py:const:`[(start, end, err, msg, replacement)]`.
  :rtype: list

.. py:function:: preferred_forms_check(text, list, err, msg, ignore_case=True, \
                                       offset=0, max_errors=float("inf"))

  To suggest a preferred form of the word used.
  The parameter :py:data:`offset`
  is not needed for style guide testing.


  :param str text: Text to be checked
  :param list list: list of comparison (words or regex): :py:const:`[correct form , incorrect form]`
  :param str err: Name of the test
  :param str msg: Error or warning message
  :param bool ignore_case: For using :py:data:`re.IGNORECASE`
  :param float max_errors: Maximum number of errors to be generated
  :return: The error list consisting of error tuples: :py:const:`[(start, end, err, msg, replacement)]`.
  :rtype: list


.. py:function:: consistency_check(text, word_pairs, err, msg, offset=0)

   To check for consistency for the given word pairs.
   The parameters :py:data:`offset`
   is not needed for style guide testing.

   :param str text: Text to be checked
   :param list word_pairs: Word pairs to be checked for consistency
   :param str err: Name of the test
   :param str msg: Error or warning message
   :return: The error list consisting of error tuples: :py:const:`[(start, end, err, msg, replacement)]`.
   :rtype: list

.. note::

  The checker functions are used by the
  built-in proselint function :py:func:`lint`
  to generate an error list of different format.
  The returned list finally is: :py:const:`[(check, message, line, column, start, end, end - start, "warning", replacements)]`

.. seealso:: `Proselint source code <https://github.com/amperser/proselint/blob/master/proselint/tools.py>`_

.. rubric:: Example Usage

.. code-block:: python

  @memoize
  def example(text):
      """Example check."""
      err = "style-guide.example"
      msg = "A demonstration for writing checks."
      regex = "[\.\?!](example)"

      return existence_check(text, [regex], err, msg, ignore_case=False, 
                         require_padding=False)

When you define code-blocks which
use built-in proselint testing,
specify the class **style-checks**.

.. code-block:: rst

  .. code-block:: python
    :class: style-checks

The generated file after parsing code
for style checks is :file:`style-checks.py`.


If the test is too large
to be defined in the file :file:`docs-style-guide.rst`,
you can use a snippet from the test
(as :ref:`here <american-spelling>`).
The code-blocks for such snippets
should specify the class **proselint-extra-checks**.
Define the complete test
in the file :file:`/style-guide/proselint-extra-checks.py`.

.. _independent-checks:

Independent checks
~~~~~~~~~~~~~~~~~~~

Apart from the checks, which are to be run through proselint,
you can add extra checks to be run independently.
They are not enabled in :file:`proselintrc` as well.
For example, the checks for finding quote marks and section labels
do not use any built-in functions to obtain an error list.

.. rubric:: Example Usage

.. code-block:: python

  def check_quotes(text):
      """Avoid using straight quotes."""
      err = "style-guide.check-quote"
      msg = "Avoid using quote marks."
      regex = r"\"[a-zA-z0-9 ]{1,15}\""

      errors = []

      for matchobj in re.finditer(regex, text):
          start = matchobj.start()+1
          end = matchobj.end()
          (row, col) = line_and_column(text, start)
          extent = matchobj.end()-matchobj.start()
          errors += [(err, msg, row, col, start, end,
                           extent, "warning", "None")]

      return errors

The code-blocks for extra checks
should specify the class **extra-checks**.
The generated file after parsing code
for extra checks is :file:`extra-checks.py`.

.. note::

  Built-in proselint function :py:func:`line_and_column` is used with extra checks to obtain the row and column of the matched text.

  .. py:function:: line_and_column(text, start)

    To find the line number and column of a position in a string.

    :param str text: Text to be searched for
    :param int start: Starting position of matched pattern
    :return: Tuple containing row and column number
    :rtype: tuple

.. _classify-checks:

Error vs warning
~~~~~~~~~~~~~~~~~~

- Warnings are intended to provide guidance to authors.
- Errors enforce "hard" rules, and raising an error will stop the build.

You can classify the result of a check
as an error if you are sure
that no false positives would be produced.
The checks classified as errors should return a replacement
for fixing the errors.
Proselint dependent checks which use the function
:py:func:`preferred_forms_check` or :py:func:`consistency_check`
always return a preferred form.
If you create an independent check
which generates an error
make sure to return a replacement in the error list.

To generate an error from a check,
specify the check name in the list of errors
in the function :py:func:`get_errlist`
in the file :file:`style-test.py`.

.. _exclude-checks:

Excluding built-in proselint checks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To exclude an built-in proselint check,
specify the check name in the check list
in the function :py:func:`exclude_checks`
in the file :file:`style-test.py`.

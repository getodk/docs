.. spelling:word-list::
    lang
    OutOfMemoryError

Troubleshooting Collect
========================

If you experience unexpected behavior in Collect, we strongly encourage you to post to `the forum <https://forum.getodk.org/>`_. Not only will this likely help you address your short-term need, it may also help the development team make improvements to the application that benefit all users. We consider reporting issues a very important contribution to the project, thank you!

Here are some known issues and how to address them.

Fatal Exception: java.lang.OutOfMemoryError
-------------------------------------------

This most commonly occurs when opening a form in ODK Collect. It means Collect needs more memory than it has access to and usually includes details like:

  Failed to allocate a 24 byte allocation with 2858136 free bytes and 2791KB until OOM, target footprint 536870912, growth limit 536870912; giving up on allocation because <1% of heap free after GC.

This generally occurs with forms that have a lot of complex :doc:`logic <form-logic>`, many :ref:`repeat instances <repeats>`, or 60k+ elements in a choice list, Entity List or attached data file. It may also occur with simple forms if many applications are open on a device or if a device has 1 GB or less of RAM. It's particularly likely to happen the first time that a form or form update is opened. We generally recommend devices with at least 4 GB of RAM for complex forms.

Sometimes this error is related to a temporary state and can be resolved by restarting the device, `closing Collect <https://support.google.com/android/answer/9079646?hl=en#zippy=%2Cclose-apps>`_ or closing other applications.

If that doesn't help, consider simplifying the form. For example, could you remove some choices from your choice list or attached document? Could you split a form with a lot of logic into two separate forms filled in at different times? Could you limit the number of repeats created in a single submission?

We also encourage you to share your form and device information `on the forum <https://forum.getodk.org/>`_.

.. _troubleshoot-field-repeated:

XPath evaluation: type mismatch - This field is repeated
---------------------------------------------------------

This error is usually followed by a list of the repeated fields expressed as :ref:`XPath paths <xpath-paths>`:

.. code-block:: xml

  /data/repeat[1]/description[1];/data/repeat[2]/description[1]

And the hint:

.. code-block:: java

  You may need to use the indexed-repeat() function to specify which value you want

This error points to a form design issue. If you get the error while filling out a form, please talk to the person who asked you to fill that form out.

If you are the person who built the form, you will need to change the form design to fix the issue. To understand and fix this error, start by looking at the fields listed to identify which part of the field is repeated. If the fields start with ``/data``, the issue has to do with :ref:`repeats <troubleshoot-repeated-field-repeats>`. If the fields start with ``instance('<some name>')``, the issue has to do with :ref:`looking up a value in a dataset <troubleshoot-repeated-field-dataset>`.

.. warning::

  The web form preview will not show this error. Instead, it will default to always using the first repeated value. This is usually not the desired behavior and can be more difficult to identify. We recommend using ODK Collect to test forms with repeats.

.. _troubleshoot-repeated-field-repeats:

Field in repeat used as single value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider this error:

.. code-block:: xml

  XPath evaluation: type mismatch
  This field is repeated:

  /data/repeat[1]/description[1];/data/repeat[2]/description[1]

Look at the repeated fields in the error and notice ``/data/repeat[1]`` and ``/data/repeat[2]``. This means that there is a repeat with name ``repeat`` in the form. There's an attempt to access the ``description`` field inside that repeat and to use it as a single value, for example in a ``calculate``. If there are more than one ``repeat`` instances added, you will get this crash. In your XLSForm, look for a reference to ``${description}`` outside of ``repeat`` to identify the source of the issue.

Here are some possible fixes depending on what you're trying to do:

* If you're trying to do something with the ``description`` of each repeat instance, you likely can move ``${description}`` inside the repeat instead of using it outside the repeat.
* If you're trying to use the ``description`` of each repeat instance in another repeat, you can use the :func:`indexed-repeat` function with the :func:`position` function in that second repeat.
* If you're trying to do something with the ``description`` of all of the repeat instances, you could use a function like :func:`join` from outside the repeat.

You can reproduce this error yourself using `this form definition <https://docs.google.com/spreadsheets/d/1GK8CNawKlDiAx9M4y3df_7gtMQPHshdQ9Bc0fUENzU8/edit?gid=1068911091#gid=1068911091>`__. Start by selecting ``Blue`` to skip the first part of the form. When you get to the repeat, start by adding a single repeat instance and notice that the form works as expected. Then, go back and add another repeat instances, navigate forward, and see this crash.

.. tip::

  Whenever you have a form with a repeat, make sure to test it with 0, 1 and multiple repeat instances. This can help you catch this kind of issue before you send it out to be used.

.. _troubleshoot-repeated-field-dataset:

Multiple values from a dataset used as a single value
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider this error:

.. code-block:: xml

  XPath evaluation: type mismatch
  This field is repeated:

  instance(my_list)/root/item[1]/label[1];instance(my_list)/root/item[3]/label[1]

Look at the repeated fields in the error and notice ``instance(my_list)/root/item[1]`` and ``instance(my_list)/root/item[3]``. This means that there is a list with name ``my_list`` and that there was an attempt to read the ``label`` of the first and third items in that list.

You can experience this error yourself by using `this form definition <https://docs.google.com/spreadsheets/d/1GK8CNawKlDiAx9M4y3df_7gtMQPHshdQ9Bc0fUENzU8/edit?gid=1068911091#gid=1068911091>`__. Start by selecting ``Blue`` and go to the next screen to see that the single blue item was correctly identified. Then go back to the first question and select ``Red``. Go to the next screen and you will see the crash above. The expression that causes the crash is ``instance('my_list')/root/item[color=${color}]/label`` because multiple items match the ``color=${color}`` expression when you select ``Red`` as the color.

Here are some possible fixes depending on your needs:

* Ensure uniqueness of the property to filter on. In the form above, you could make sure that each color is only used once in the ``things`` list. There's no built-in way to enforce this restriction in ODK but you could use a spreadsheet constraint to do so. If you're using an Entity List, you could use a constraint in your registration form.
* Use a different item property to filter on. In the form above, if you do want multiple items to have the same ``color``, the form structure doesn't make sense. Maybe it should start by showing a list of items first instead and then any other :ref:`lookup expressions <referencing-values-in-datasets>` could filter by ``name`` which is required to be unique.
* Aggregate all of the values. For example, you could use a function like :func:`join` or :func:`count`.

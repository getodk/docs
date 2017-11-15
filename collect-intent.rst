***************************
External App Integrations
***************************

:doc:`collect-guide` enables rich integrations with external Android applications. It can both launch external applications to get data from them and be launched by custom apps to perform certain actions.


.. note::
  - `ODK Counter <https://github.com/opendatakit/counter>`_ demonstrates how to build an external application to pass data to ODK Collect. It an app which is intended to be used from ODK Collect as a counter.
  - `ODK Collect Intents Tester <https://github.com/grzesiek2010/collectTester>`_ demonstrates how to open ODK Collect activities directly from an external app.

.. _launch-apps-single-field:

Launching external apps to populate single fields
===================================================

ODK Collect can launch external applications to populate string, integer or numeric fields using the ``ex:intentString`` appearance. A ``value`` parameter that holds the current value for that field is passed to the application. Since v1.4.3, additional parameters can be specified. The names of these parameters are user defined and there are no reserved names. 

XLSForm
~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label, appearance

  integer, counter, Click launch to start the counter app, "ex:org.opendatakit.counter(form_id='counter-form', form_name='Counter Form', question_id='1', question_name='Counter')"

XForm XML
~~~~~~~~~~~

.. code-block:: xml

  <input appearance="ex:org.opendatakit.counter(form_id='counter-form', form_name='Counter Form', question_id='1', question_name='Counter')" ref="/counter/counter">
      <label>Click launch to start the counter app</label>
  </input>

In the examples above, the parameter specified are ``form_id``, ``form_name``, ``question_id`` and ``question_name``. Any number of extra parameters can be specified. The parameter values can be:

  - An xpath expression to an other field.
  - A string literal defined in single quotes.
  - A raw number (integer or decimal)
  - Any JavaRosa function.

.. _launch-apps-multiple-fields:

Launching external apps to populate multiple fields
=====================================================

Since v1.4.3, a ``field-list`` group can have an ``intent`` attribute that allows an external application to populate it. This functionality is not available in XLSForm and requires editing a form's raw XML representation.

.. code-block:: xml

  <group ref="/externaltest/consented" appearance="field-list" 
          intent="org.myapp.COLLECT(uuid=/externaltest/meta/instanceID, 
                                    deviceid=/externaltest/deviceid)">
    <label>Please populate these:</label>
    <input ref="/externaltest/consented/textFieldInGroup">
      <label>A text</label>
    </input>
    <input ref="/externaltest/consented/integerFieldInGroup">
      <label>An integer</label>
    </input>
    <input ref="/externaltest/consented/decimalFieldInGroup">
      <label>A decimal</label>
    </input>
  </group>

The ``intent`` attribute is only used when the group has an ``appearance`` of ``field-list``. The format and the functionality of the ``intent`` value is the same as above. If bundle of values returned by the external application contains values whose keys match the type and the name of the sub-fields, then these values overwrite the current values of those sub-fields.

The external app is launched with the parameters that are defined in the intent string plus the values of all the sub-fields that are either text, decimal, or integer. Any other sub-field is invisible to the external app.

.. _launch-collect:

Launching ODK Collect from External Apps
==========================================

:doc:`collect-guide` supports several intents which allow it to be launched by external applications. You can open a specific form or lists of empty forms, saved forms, finalized forms or sent forms. 

This section describes how to launch ODK Collect and open its activities from an external app. The code samples go in your custom Android application.

.. _about-intents:

Understanding Intents
~~~~~~~~~~~~~~~~~~~~~~~

An Intent is a messaging object you can use to request an action from another app component. 

For more details on intents, you can refer to `these Android docs <https://developer.android.com/guide/components/intents-filters.html>`_.

.. _launch-activity:

Launching Collect activities from external application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To start one of ODK Collect's activities:

1. Create a new intent using an appropriate action.
2. Set the type of the created intent.
3. Start an activity using the intent.

.. _form-instance-list:

Launching the form list or instance list activity
"""""""""""""""""""""""""""""""""""""""""""""""""""
 
.. code-block:: java
 	
  Intent intent = new Intent(Intent.ACTION_VIEW);
  intent.setType("vnd.android.cursor.dir/vnd.odk.form");
  startActivity(intent);
 
This displays a list of forms and allows the user to select one and fill it.
 
Similarly for an instance of the form: 
 
.. code-block:: java
 
  Intent intent = new Intent(Intent.ACTION_VIEW);
  intent.setType("vnd.android.cursor.dir/vnd.odk.instance");
  startActivity(intent);

This displays a list of saved forms and allows the user to select one and edit it.

.. _get-uri: 	
 
Getting the URI of a form or instance chosen by the user
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: java
 
  Intent intent = new Intent(Intent.ACTION_PICK);
  intent.setType("vnd.android.cursor.dir/vnd.odk.form");

.. code-block:: java
 
  static final int PICK_FORM_REQUEST = 1;  // The request code
  startActivityForResult(intent, PICK_FORM_REQUEST);
 
To get the result, override ``onActivityResultMethod`` in the followig way:

.. code-block:: java

  @Override
  protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    // Check which request we're responding to
    if (requestCode == PICK_FORM_REQUEST) {
      // Make sure the request was successful
      if (resultCode == RESULT_OK) {
        // The Intent's data URI identifies which form was selected.
        Uri formUri = data.getData();
        // Do something with the form here
      }
    }
  }

For an instance, change the intent type:
 
.. code-block:: java
 
  intent.setType("vnd.android.cursor.dir/vnd.odk.instance");

.. _use-form-uri:

Using a URI to edit a form or instance
""""""""""""""""""""""""""""""""""""""""
 
If the URI of a form or instance is known, it can be viewed or edited. For example, a URI received in ``onActivityResult()`` as described above can be used.
 
.. code-block:: java
 
  Intent intent = new Intent(Intent.ACTION_EDIT);
  intent.setData("content://org.odk.collect.android.provider.odk.forms/forms/2");
  startActivity(intent);
 
The same thing can be done with a specific instance.
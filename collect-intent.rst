External App Integrations
===========================

:doc:`collect-guide` enables rich integrations with external Android applications. It can both be launched externally to perform certain actions and launch external applications to get data from them.


.. note::

  - `ODK Collect Intents Tester <https://github.com/grzesiek2010/collectTester>`_ demonstrates how to open ODK Collect activities directly from an external app.
  - `ODK Counter <https://github.com/opendatakit/counter>`_ demonstrates how to build an external application to pass data to ODK Collect. It an app which is intended to be used from ODK Collect as a counter.

.. _launch-collect:

Launching ODK Collect from External Apps
------------------------------------------

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

.. _launch-apps:

Launch External Apps from ODK Collect
---------------------------------------

ODK Collect can launch 3rd party apps to populate string, integer or numeric fields. Beginning with ODK Collect 1.4.3, an external app can populate a group of fields. Also beginning with ODK Collect 1.4.3, any number of additional values, beyond the current value(s) of the field(s) being updated, can be passed to the 3rd party app.

- A text/decimal/integer field with an **ex:intentString** appearance can specify extra parameters that are passed to the external app, in addition to the ``value`` parameter that holds the current value for that field. The names of the parameters are user defined and there are no reserved names. 

.. code-block:: xml

  <input appearance="ex:org.myapp.COLLECT(started= /externaltest/starttime ,
                                          constant='----', randomNumber=random())" 
           ref="/externaltest/textField" >
      <label>Click launch to see an external-fetched string</label>
  </input>

Any number of extra parameters can be specified. The parameter values can be four different things:

  - An xpath expression to an other field.
  - A string literal defined in single quotes.
  - A raw number (integer or decimal)
  - Any JavaRosa function.


- A ``field-list`` group can also have an ``intent`` attribute.

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

  - This intent attribute is only used when the group has an ``appearance`` of ``field-list``.
  - The format and the functionality of the ``intent`` value is the same as above.
  - The external app is launched with the parameters that are defined in the intent string plus the values of all the sub-fields that are either text, decimal, or integer.
  - Any other sub-field is invisible to the external app.
  - If the returned bundle of values contains values whose keys match the type and the name of the sub-fields, then these values overwrite the current values of those sub-fields.

.. seealso::

  The source code for example of an external application that collects and returns a single field value is provided, here: `BreathCounter <https://github.com/opendatakit/breathcounter>`_. The project includes the form definition (.xml) file that works with the application.


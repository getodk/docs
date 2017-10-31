Using ODK Collect with External Apps
======================================

.. _launch-collect:

Launching ODK Collect from External Apps
------------------------------------------

:doc:`collect-guide` allows us to open several of its activities from another app. You can open a specific form or lists of empty forms, saved forms, finalized forms or sent forms. You can also build your own app that interacts with ODK Collect through intents. On the other side, you can also open other apps from ODK Collect.

This doc describes how to launch ODK Collect and open its activities directly from an external app.

.. _about-intents:

Understanding Intents
~~~~~~~~~~~~~~~~~~~~~~~

An Intent is a messaging object you can use to request an action from another app component. 

For example:
  
- In ODK Collect App, go to :guilabel:`General Settings`.

.. image:: /img/collect-intent/general-settings.png
   :alt: Image showing general settings option.
   :class: device-screen-vertical

- Choose :menuselection:`Server` in the menu and enter a URL for your Aggregate server. 

.. image:: /img/collect-intent/server.png
   :alt: Image showing server option.
   :class: device-screen-vertical

.. image:: /img/collect-intent/server-url.png
   :alt: Image showing server url.
   :class: device-screen-vertical

- After the URL data has been entered, it is passed on to other activities, like :guilabel:`Get Blank Form` where the forms pertaining to the url are fetched.

.. image:: /img/collect-intent/get-blank-form.png
   :alt: Image showing connection to server made.
   :class: device-screen-vertical

So, this is when intents come into action. Intents help in passing the data fetched from the url to the activity :guilabel:`Get Blank Form`, thereby establishing a communication between the two main activities.

For more details on intents, you can refer to `these Android docs <https://developer.android.com/guide/components/intents-filters.html>`_.

.. _use-intent:

Using Collect's Intent
~~~~~~~~~~~~~~~~~~~~~~~~~

Each screen of an Android app is called an activity. ODK Collect has several activities and sub-activities. These activities are able to communicate with each other using intents.

If you want to start ODK Collect's activity you need to:

1. Create a new intent using an appropriate action.
2. Set the type of created intent.
3. Start an activity using the intent.

.. _edit-form:

Navigating user to choose and edit a form/instance 
""""""""""""""""""""""""""""""""""""""""""""""""""""
 
.. code-block:: java
 	
  Intent intent = new Intent(android.intent.action.EDIT);
  intent.setData(org.odk.collect.android.provider.FormsProviderAPI.FormsColumns.CONTENT_URI);
 
This will allow user to choose the form and go on filling it .
 
Similarly for an instance of the form : 
 
.. code-block:: java
 
  Intent intent = new Intent(android.intent.action.EDIT);
  intent.setData(org.odk.collect.android.provider.InstanceProviderAPI.InstanceColumns.CONTENT_URI);

.. _get-uri: 	
 
Getting the URI of the form/instance chosen by user
"""""""""""""""""""""""""""""""""""""""""""""""""""""

.. _start-activity:

Starting Activity For Result
''''''''''''''''''''''''''''''

.. code-block:: java
 
  Intent intent = new Intent(android.intent.action.PICK);
  intent.setData(org.odk.collect.android.provider.FormsProviderAPI.FormsColumns.CONTENT_URI);
 
.. code-block:: java
 
  static final int PICK_FORM_REQUEST = 1;  // The request code
  startActivityForResult(intent, PICK_FORM_REQUEST);

.. _get-result:

Getting result
''''''''''''''''
 
To get the result, override ``onActivityResultMethod`` in the followig way:

.. code-block:: java

  @Override
  protected void onActivityResult(int requestCode, int resultCode, Intent formUri) {
     // Check which request we're responding to
    if (requestCode == PICK_FORM_REQUEST) {
        // Make sure the request was successful
	    if (resultCode == RESULT_OK) {
 	      // The user picked a contact.
 	      // The Intent's data Uri identifies which form was selected.
 	      // Do something with the form here
 	    }
	}	
  }
 

Similarly for an instance, change the URI to that of the instance :
 
.. code-block:: java
 
  intent.setData(org.odk.collect.android.provider.InstanceProviderAPI.InstanceColumns.CONTENT_URI);

.. _use-form-uri:

Use form's URI to edit/view form
""""""""""""""""""""""""""""""""""
 
The formURI in the ``onActivityResult()`` method, allows us to view/edit the particular form by:
 
.. code-block:: java
 
  Intent intent = new Intent(android.intent.action.EDIT);
  intent.setData(formUri);
 
If we want to view the form, the action can be changed to :
 
.. code-block:: java
 
  Intent intent = new Intent(android.intent.action.VIEW);
 
Similar things can be done for an Instance.
 
.. note::

  - `ODK Collect Intents Tester app <https://github.com/grzesiek2010/collectTester>`_ is for testing the ODK Collect app and presenting how to open activities of ODK Collect directly from an external app.
  - `ODK Counter <https://github.com/opendatakit/counter>`_ is an example of integrating with Collect through external apps. It an app which is intended to be used from ODK Collect as a counter. 

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


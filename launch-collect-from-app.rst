Launching ODK Collect from External Apps
==========================================

.. seealso::
  
  :doc:`launch-apps-from-collect`

:doc:`collect-intro` supports several intents which allow it to be launched by external applications. You can open a specific form or lists of empty forms, saved forms, finalized forms or sent forms. 

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

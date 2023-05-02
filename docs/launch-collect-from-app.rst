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

.. _get-forms: 	
 
Getting the list of forms and instances:
"""""""""""""""""""""""""""""""""""""""""""

Using `Content providers <https://developer.android.com/guide/topics/providers/content-providers>`_ ODK Collect shares the list of forms and instances with other apps.

To fetch the list of forms call:

.. code-block:: java
 
  Uri uri = "content://org.odk.collect.android.provider.odk.forms/forms"
  getContentResolver().query(uri, null, null, null, null);

Similarly for the list of instances:

.. code-block:: java
 
  Uri uri = "content://org.odk.collect.android.provider.odk.instances/instances"
  getContentResolver().query(uri, null, null, null, null);

You can also get an individual (or filtered list) form/instance by adding selection criteria. For example, if you want to get a list of instances with a given ``jrFormId`` you can use:

.. code-block:: java
 
  Uri uri = "content://org.odk.collect.android.provider.odk.instances/instances"
  getContentResolver().query(uri, null, "jrFormId=?", new String[]{"all-widgets"}, null);

This will return a `Cursor <https://developer.android.com/reference/android/database/Cursor>`_ with the list of forms/instances. You can iterate such a cursor and read the data stored in it: 

.. code-block:: java
 
        if (cursor != null) {
            try {
                while (cursor.moveToNext()) {
                    int id = cursor.getInt(cursor.getColumnIndex(BaseColumns._ID));
                    String formName = cursor.getString(cursor.getColumnIndex(DISPLAY_NAME));

                    // Collect data from other columns and store it in a list for example
                }
            } finally {
                cursor.close();
            }
        }

The data stored in a cursor is different for forms and instances. The list of columns used to share forms is defined in `DatabaseFormColumns <https://github.com/getodk/collect/blob/master/collect_app/src/main/java/org/odk/collect/android/database/forms/DatabaseFormColumns.kt>`_. For instances it is: `DatabaseInstanceColumns <https://github.com/getodk/collect/blob/master/collect_app/src/main/java/org/odk/collect/android/database/instances/DatabaseInstanceColumns.kt>`_. 

.. _get-uri: 	
 
Getting the URI of a form or instance chosen by the user
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: java
 
  Intent intent = new Intent(Intent.ACTION_PICK);
  intent.setType("vnd.android.cursor.dir/vnd.odk.form");

.. code-block:: java
 
  static final int PICK_FORM_REQUEST = 1;  // The request code
  startActivityForResult(intent, PICK_FORM_REQUEST);
 
To get the result, override ``onActivityResultMethod`` in the following way:

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

If the URI of a form or instance is not known, it can be generated by appending the id (received in a cursor after fetching the list of forms/instances as described above) to ``content://org.odk.collect.android.provider.odk.forms/forms/`` in the case of forms and ``content://org.odk.collect.android.provider.odk.instances/instances/`` in the case of instances.
 
.. code-block:: java
 
  Intent intent = new Intent(Intent.ACTION_EDIT);
  intent.setData("content://org.odk.collect.android.provider.odk.forms/forms/2");
  startActivityForResult(intent);

.. note::
  The ``Form EDIT`` action returns an instance URI, so after saving such a form it should be returned in intent data (example: ``content://org.odk.collect.android.provider.odk.instances/instances/1``).  
 
The same thing can be done with a specific instance.

.. warning::
  Launching Collect activities using their names is not supported because those names can change at any time.

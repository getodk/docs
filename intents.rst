Using Collect's Intent
========================

Navigating User to edit a form/instance after choosing :
-----------------------------------------------------------

.. code-block:: java
	
	Intent intent = new Intent(android.intent.action.EDIT);
	intent.setData(org.odk.collect.android.provider.FormsProviderAPI.FormsColumns.CONTENT_URI);

This will allow user to choose the form and go on filling it .

Similarly for an instance of the form : 

.. code-block:: java

	Intent intent = new Intent(android.intent.action.EDIT);
	intent.setData(org.odk.collect.android.provider.InstanceProviderAPI.InstanceColumns.CONTENT_URI);

Apart from this , we also need to put in a mode, which will allow to differentiate between editing or viewing form . So we need to put in an extra here , which goes like :

For Editing Saved Instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: java

	intent.putExtra												    (org.odk.collect.android.utilities.ApplicationConstants.BundleKeys.FORM_MODES,org.odk.collect.android.utilities.ApplicationConstants.FormModes.EDIT_SAVED);


For Viewing Sent Form
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: java

	intent.putExtra	(org.odk.collect.android.utilities.ApplicationConstants.BundleKeys.FORM_MODES,org.odk.collect.android.utilities.ApplicationConstants.FormModes.VIEW_SENT);


Getting the URI of the form/instance chosen by USER :
--------------------------------------------------------

Starting Activity For Result
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

.. code-block:: java

	Intent intent = new Intent(android.intent.action.PICK);
	intent.setData(org.odk.collect.android.provider.FormsProviderAPI.FormsColumns.CONTENT_URI);

.. code-block:: java

	static final int PICK_FORM_REQUEST = 1;  // The request code
	startActivityForResult(intent, PICK_FORM_REQUEST);

To get the result , simply override onActivityResultMethod like this :
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


Same thing can be done for an instance by simply changing the uri to that of the instance :

.. code-block:: java

	intent.setData(org.odk.collect.android.provider.InstanceProviderAPI.InstanceColumns.CONTENT_URI);




searching s

Using a particular form's uri returned previously to launch for edit/view:
-----------------------------------------------------------------------------


Consider formUri in the onActivityResult() method , this simply allow us to view/edit the particular form by :

.. code-block:: java

	Intent intent = new Intent(android.intent.action.EDIT);
	intent.setData(formUri);

If we want to view the form, the action can be changed to :

.. code-block:: java

	Intent intent = new Intent(android.intent.action.VIEW);

Similar things can be done for an Instance.


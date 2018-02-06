Metadata Scheme
==================

This document details the metadata scheme for OpenRosa-compliant XForms. This metadata is used to ensure that critical or extremely useful data pertaining to the XForms and submissions made by client devices is captured and stored.

There are two types of metadata in a form submission. 

 - Form metadata — Data about the identity and version of the XForm used to create the data being submitted. 
 - Submission metadata — Data about the submission itself.

.. _blank-form-metadata:
 
Blank Form Metadata
-----------------------

A blank form must have two pieces of identifying metadata. These are provided as attributes in the top-level element inside ``model/instance``.

.. The following block is `none` because the lexer won't handle incomplete xml.

.. code-block:: none

  <model>
  .
  .
  .
    <instance>
      <form-name id="opendatakit.org:all-widgets" version="2.1.30"
      .
      .
      .
      </form-name>
    </instance>
  </model>

      
Two attributes are required. One provides the unique identity of the form, the other provides the current version number.

.. _form-identity:

Form Identity
~~~~~~~~~~~~~~~~

One of:

- ``id``
- ``xmlns``  
  
These values should be in the form of ``scheme:value``. 

If specified, the id value takes precedence over any explicit ``xmlns`` declaration. 

For ``id``, the implementor's registered domain name should be used as part of the scheme (for example:``opendatakit.org:widgetForm``). 

Compliant systems MUST support ``id`` or ``xmlns`` lengths up to 249 chars; ideally, servers SHOULD be able to support arbitrary lengths.

.. _form-version:

Version
~~~~~~~~~~

A string value indicating the version number of the form. 

- MUST support a string value (not a number), to indicate an increment. 
- SHOULD support any string schema. 
- MUST support arbitrary strings up to 249 characters
- SHOULD support arbitrary-length strings

The value of ``version`` MUST be incremented when any part of the form changes. 

If ``version`` is not present, it is handled as NULL. 

.. _completed-form-metadata:

Completed Form Metadata
--------------------------

In a completed form, metadata is provided in a ``<meta>`` element inside the ``<model>`` element.

.. code-block:: xml

  <model>
  .
  .
  .
    <meta>
      <instanceID>
        uuid:ca90905c-a2db-11e7-abc4-cec278b6b50a
      </instanceID>
      <userID>
        openid:http://www.google.com/profiles/adam.michael.wood
      </userID>
    </meta>
    
.. _metadata-fields:

Fields
~~~~~~~~

The only **required** element in the form submission metadata is ``<instanceID>``, which must be a universally unique string identifying this specific submission.

Optional fields:

- ``<timeStart>`` ---  An `ISO 8601 timestamp <https://en.wikipedia.org/wiki/ISO_8601>`_ of when form entry started.
- ``<timeEnd>`` --- An `ISO 8601 timestamp <https://en.wikipedia.org/wiki/ISO_8601>`_ of when form entry ended.
- ``<userID>`` --- A unique identifier of the submitting user.
- ``<deviceID>`` --- A unique identifier of device used to generate the submission.
- ``<deprecatedID>`` --- the ``<instanceID>`` of the submission for which this is a revision. Server software can use this field to unify multiple revisions to a submission into a consolidated submission record.

.. _id-field-formatting:

ID field formatting
""""""""""""""""""""""

ID fields (``<instanceID>``, ``<userID>``, etc.) must follow the format ``scheme:id``. 

.. _recommended-id-schemes:

Recommended ID schemes
''''''''''''''''''''''''

``instanceID``, ``deprecatedID``
  uuid
  
``userID``
  mailto
  
  openid
  
``deviceID``
  mac
  
  uuid
  
If you implement a custom ID scheme, it should be prefixed with your domain name, to ensure uniqueness.

.. code-block:: xml

  <instanceID>opendatakit.org:123456789</instanceID>
  
.. _id-constraints:

ID Field Constraints
"""""""""""""""""""""""

- The combined scheme:value keypair MUST be no longer than 249 characters (ie, so that varchar(249) can be used). 
  
  - A `robust <https://en.wikipedia.org/wiki/Robustness_principle>`_ Server SHOULD be able to support an arbitrary length ID, however.
  
- Only ONE of each type of ID element can be included in a form submitted to the server. That is, only one ``deviceID``, one ``userID``, one ``instanceID``, and one ``deprecatedID``.

  -  Each ID element MUST have one and only one scheme:value pair.

.. _defining-expected-metadata:  
  
Defining expected submission metadata in the blank form
------------------------------------------------------------

The blank form **MUST** specify which of the metadata fields are expected when the completed form is submitted. This is done within a ``<meta>`` element having the namespace ``http://openrosa.org/xforms``. The ``<meta>`` appears inside the child node of the Primary Instance (the first instance element inside ``<model>``).

.. code-block:: xml

  <model>
    <instance>
      <data xmlns:jr="http://openrosa.org/xforms"
            id="example.org:myFormId"
            version="1" >
        <jr:meta>
          <jr:timeStart/>
	  <jr:timeEnd/>
	  <jr:instanceID/>
	  </jr:meta>

	  
.. _metadata-examples:

Examples
------------

.. _blank-form-metadata-example:

Blank form metadata
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

  <h:head>
    <h:title>Metablock example</h:title>
    <model>
      <instance>
	<data xmlns:jr="http://openrosa.org/xforms"
	      xmlns="http://example.org/meta"
	      version="1" >
	  <jr:meta>
	    <jr:deviceID/>
	    <jr:timeStart/>
	    <jr:timeEnd/>
	    <jr:instanceID/>
	  </jr:meta>
	  .
	  .
	  .
	</data>
      </instance>
      .
      .
      .
    </model>
  </h:head>

.. _form-submission-metadata-example:

Form submission metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: xml

  <?xml version='1.0'?>
    <data version="1" 
          xmlns:jr="http://openrosa.org/xforms"         
	  xmlns="http://example.org/meta">
      <jr:meta>
        <jr:deviceID>uuid:38DN0236SAKWJOJNQB3XJI9RW</jr:deviceID>
        <jr:timeStart>2010-08-12T04:08:29.765-5:00</jr:timeStart>
        <jr:timeEnd>2010-08-12T04:10:23.062-5:00</jr:timeEnd>
        <jr:instanceID>uuid.dimagi.org:GEPSJLOGH13TY8L77066GEJJW</jr:instanceID>
        <jr:userID>chwid.dimagi.org:Akende</jr:userID>
      </jr:meta>
      .
      .
      .
    </data>

Metadata Schema
==================

This document details the metadata scheme to be used in an :terms:`XForm` intended for use with OpenRosa compliant servers. This metadata is used to ensure that critical or extremely useful data pertaining to the XForms and submissions made by client devices is captured and stored.

There are two types of metadata in a form submission. 

 - Form metadata — Data about the identity and version of the XForm used to create the data being submitted. 
 - Submission metadata — Data about the submission itself.


Blank Form Metadata
-----------------------

A blank form must have two pieces of identifying metadata. These are provided as attributes in the top-level element inside ``model/instance``.

.. code-block:: xml

  <model>
  .
  .
  .
    <instance>
      <form-name id="opendatakit.org:all-widgets" version="2.1.30"
      .
      .
      .

Two attributes are required. One provides the unique identity of the form, the other provides the current version number.

Form Identity
~~~~~~~~~~~~~~~~

One of:

- ``id``
- ``xmlns``  
  
These values should be in the form of ``scheme:value``. 

If specified, the id value takes precedence over any explicit ``xmlns`` declaration. 

For ``id``, the implementor's registered domain name should be used as part of the scheme (for example:``opendatakit.org:widgetForm``). 

Compliant systems MUST support ``id`` or ``xmlns`` lengths up to 249 chars; ideally, servers SHOULD be able to support arbitrary lengths.

Version
~~~~~~~~~~

A string value indicating the version number of the form. 

- MUST support a string value (not a number), to indicate an increment. 
- SHOULD support any string schema. 
- MUST support arbitrary strings up to 249 characters
- SHOULD support arbitrary-length strings

The value of ``version`` MUST be incremented when any part of the form changes. 

If ``version`` is not present, it is handled as NULL. 


Completed Form Metadata
--------------------------

In a completed form, metadata is provided in a ``<metadata>`` element inside the ``<model>`` element.

.. code-block:: xml

  <model>
  .
  .
  .
    <metadata>
      <instanceID>
        uuid:ca90905c-a2db-11e7-abc4-cec278b6b50a
      </instanceID>
      <userID>
        openid:http://www.google.com/profiles/adam.michael.wood
      </userID>
    </metadata>
    
Fields
~~~~~~~~

The only **required** element in the form submission metadata is ``<instanceID>``, which must be a universally unique string identifying this specific submission.

Optional fields:

- ``<timeStart>`` ---  A timestamp of when form entry started.
- ``<timeEnd>`` --- A timestamp of when form entry ended.
- ``<userID>`` --- A unique identifier of the submitting user.
- ``<deviceID>`` --- The ID of the specific device used to generate the submission.
- ``<deprecatedID>`` --- the ``<instanceID>`` of the submission for which this is a revision. Server software can use this field to unify multiple revisions to a submission into a consolidated submission record.

ID field formatting
""""""""""""""""""""""

ID fields (``<instanceID>``, ``<userID>``, etc.) must follow the format ``scheme:id``. 

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
  

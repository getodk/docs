Launching External Apps from Collect Forms
====================================================

.. seealso::

  :doc:`launch-collect-from-app`
	
.. _launch-apps-single-field:

Launching external apps to populate single fields
------------------------------------------------------

ODK Collect can launch external applications to populate string, integer or decimal fields using the ``ex:intentString`` appearance. A ``value`` parameter that holds the current value for that field is passed to the application. Since v1.4.3, additional parameters can be specified. The names of these parameters are user defined and ``value`` is the only reserved name. 

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

In the examples above, the parameters specified are ``form_id``, ``form_name``, ``question_id`` and ``question_name``. Any number of extra parameters can be specified. The parameter values can be:

  - XPath expressions referring to other fields and including function calls
  - String literals defined in single quotes
  - Raw integers or decimals

.. _launch-apps-multiple-fields:

Launching external apps to populate multiple fields
-------------------------------------------------------

Since v1.4.3, a ``field-list`` group can have an ``intent`` attribute that allows an external application to populate it. 

XLSForm
~~~~~~~~~

.. csv-table:: survey
  :header: type, name, label, appearance, body::intent

  begin_group, mygroup, Fields to populate, field-list, "org.mycompany.myapp(my_text='Some text', uuid=/myform/meta/instanceID)"
  text, sometext, Some text
  integer, someinteger, Some integer
  end_group                                        

.. code-block:: xml

  <group ref="/myform/mygroup" appearance="field-list" 
          intent="org.mycompany.myapp(my_text='Some text', 
                                      uuid=/myform/meta/instanceID)">
    <label>Fields to populate</label>
    <input ref="/myform/mygroup/sometext">
      <label>Some text</label>
    </input>
    <input ref="/myform/mygroup/someinteger">
      <label>Some integer</label>
    </input>
  </group>

The ``intent`` attribute is only used when the group has an ``appearance`` of ``field-list``. The format and the functionality of the ``intent`` value is the same as above. If bundle of values returned by the external application contains values whose keys match the type and the name of the sub-fields, then these values overwrite the current values of those sub-fields.

The external app is launched with the parameters that are defined in the intent string plus the values of all the sub-fields that are either text, decimal, or integer. Any other sub-field is invisible to the external app.

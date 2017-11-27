***************************
External App Integrations
***************************

:doc:`collect-intro` enables rich integrations with external Android applications. It can both launch external applications to get data from them and be launched by custom apps to perform certain actions.


.. note::
  - `ODK Counter <https://github.com/opendatakit/counter>`_ demonstrates how to build an external application to pass data to ODK Collect. It an app which is intended to be used from ODK Collect as a counter.
  - `ODK Collect Intents Tester <https://github.com/grzesiek2010/collectTester>`_ demonstrates how to open ODK Collect activities directly from an external app.

.. _launch-apps-single-field:

Launching external apps to populate single fields
===================================================

ODK Collect can launch external applications to populate string, integer or decimal fields using the ``ex:intentString`` appearance. A ``value`` parameter that holds the current value for that field is passed to the application. Since v1.4.3, additional parameters can be specified. The names of these parameters are user defined and there are no reserved names. 

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


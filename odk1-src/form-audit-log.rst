.. spelling::

  timestamp

Logging enumerator behavior
=============================

Collect can log the behavior of enumerators as they navigate through a form. This log has many uses including discovering:

- questions that take a long time to answer

- how enumerators typically navigate through a form

- enumerators who take a particularly long or short time to answer

This information can inform form design and training.

.. admonition:: Aggregate 1.5.0+ required

  If a version of Aggregate lower than 1.5.0 is used, **audit files will not be saved on the server**.

.. contents:: :depth: 1
  :local:

.. _enabling-audit-logging:

Enabling audit logging
-----------------------

To enable logging for a form, add a row of :th:`type` :tc:`audit` and :th:`name` :tc:`audit` in an XLSForm:

.. csv-table:: survey
  :header: type, name, label

  audit, audit, 

A form may contain at most one row of :th:`type` :tc:`audit`.

.. _viewing-audit-logs:

Viewing audit logs
-------------------

Audit logs can be reviewed in Aggregate and downloaded for further analysis using Briefcase.

In Aggregate 1.5.0+, audit logs can be viewed by clicking on the media icon in the :tc:`meta audit` column on the Submissions page:

.. image:: /img/form-audit-log/audit-media-icon.png
  :alt: The Aggregate submissions page with a form that has an audit log. The media icon in the meta audit column is circled.

This displays a popup with the audit contents:

.. image:: /img/form-audit-log/audit-example.png
  :alt: An example audit log in Aggregate.

If more sophisticated analysis of the logs is required, they can be downloaded along with their submissions using :ref:`Briefcase <pull-from-aggregate>`.

.. _audit-log-structure:

Log structure
---------------

If a form includes an audit, Collect will create an ``audit.csv`` file as the form is filled out. The ``audit.csv`` file has the following structure:

.. csv-table:: audit.csv
  :header: event, node, start, end

  question, /data/name, 1523403169208, 1523403170733

Values in the ``event`` column represent a particular user action such as opening a form, saving a form or displaying a question. Possible event types are described in the :ref:`audit-event-types` section.

Values in the ``node`` column represent the node in the form that the event refers to, if applicable.

Values in the ``start`` and ``end`` columns are timestamps represented as the number of milliseconds since midnight, January 1, 1970 UTC. This is known as epoch time and provides a standard way of representing date/time even across timezones. The :ref:`audit-timestamps` section contains more information about timestamps.

.. _audit-event-types:

Event types
--------------

The event column of the audit log can have the following values:

+-------------------+------------------------------------------------------------------+-------+----------------+
|      Event        |                           Description                            | Node? |  Timestamps?   |
+===================+==================================================================+=======+================+
| form start        | Start filling in the form                                        | No    | ``start`` only |
+-------------------+------------------------------------------------------------------+-------+----------------+
| question          | View a question                                                  | Yes   | Yes            |
+-------------------+------------------------------------------------------------------+-------+----------------+
| group questions   | View multiple questions on one screen (``field-list``)           | Yes   | Yes            |
+-------------------+------------------------------------------------------------------+-------+----------------+
| jump              | View the jump screen                                             | No    | ``start`` only |
+-------------------+------------------------------------------------------------------+-------+----------------+
| add repeat        | Add a repeat                                                     | Yes   | Yes            |
+-------------------+------------------------------------------------------------------+-------+----------------+
| delete repeat     | Delete a repeat                                                  | Yes   | Yes            |
+-------------------+------------------------------------------------------------------+-------+----------------+
| end screen        | View the end screen                                              | No    | Yes            |
+-------------------+------------------------------------------------------------------+-------+----------------+
| form save         | Save the form                                                    | No    | ``start`` only |
+-------------------+------------------------------------------------------------------+-------+----------------+
| form exit         | Exit the form                                                    | No    | ``start`` only |
+-------------------+------------------------------------------------------------------+-------+----------------+
| form resume       | Resume the form                                                  | No    | ``start`` only |
+-------------------+------------------------------------------------------------------+-------+----------------+
| form finalize     | Finalize the form                                                | No    | ``start`` only |
+-------------------+------------------------------------------------------------------+-------+----------------+
| save error        | Error trying to save                                             | No    | ``start`` only |
+-------------------+------------------------------------------------------------------+-------+----------------+
| finalize error    | Error trying to finalize the form (probably encryption related)  | No    | ``start`` only |
+-------------------+------------------------------------------------------------------+-------+----------------+
| constraint error  | Constraint or required error on finalize                         | No    | ``start`` only |
+-------------------+------------------------------------------------------------------+-------+----------------+

.. _audit-timestamps:

Timestamps
-----------

Device time can be changed by the user unless Android access controls are put in place. To reduce the ways that audits can be manipulated by modifying device time, clock time is collected once at form launch and all following times are computed relative to that initial reading. This means that while the actual time may potentially be inaccurate, the time elapsed within and between screens is always accurate within one form editing session.

Using epoch time makes it easy to compute elapsed time by subtracting start from end. For example, given the following log:

.. csv-table:: audit.csv
  :header: event, node, start, end

  form start, , 1488761807863, 
  question, /data/name, 1488761807868, 1488761809157

The enumerator spent ``1488761809157 - 1488761807868 = 1289`` milliseconds on the screen showing the ``/data/name`` question. This corresponds to ``1289 / 1000 = 1.289`` seconds.

To convert from epoch time to time in UTC in most common spreadsheet programs, divide the epoch time by 86400000 ms per day and add 25569 days between January 1, 1900 (what most spreadsheet programs use as "day zero") and January 1, 1970. For example, to convert the timestamp ``1488761807868``:

.. code-block:: xml

  (1488761807868 / 86400000) + 25569 = 42800.03944

When the cell is set to type ``date time`` in common spreadsheet programs, it will show ``3/6/2017 0:56:48 UTC``.


.. _known-audit-limitations: 

Known limitations
-------------------

If the device is turned off while a form is being filled, Collect will not record a log entry for the screen that was shown at the time of device shutdown. Events before and after the shutdown will be logged.
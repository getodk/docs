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

In Aggregate 1.5.0+, audit logs can be viewed by clicking on the media icon in the :th:`meta audit` column on the Submissions page:

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

Values in the :th:`event` column represent a particular user action such as opening a form, saving a form or displaying a question. Possible event types are described in the :ref:`audit-event-types` section.

Values in the :th:`node` column represent the node in the form that the event refers to, if applicable.

Values in the :th:`start` and :th:`end` columns are timestamps represented as the number of milliseconds since midnight, January 1, 1970 UTC. This is known as epoch time and provides a standard way of representing date/time even across timezones. The :ref:`audit-timestamps` section contains more information about timestamps.

.. _audit-event-types:

Event types
--------------

The event column of the audit log can have the following values:

+-------------------+------------------------------------------------------------------+-------+-----------------+
|      Event        |                           Description                            | Node? |  Timestamps?    |
+===================+==================================================================+=======+=================+
| form start        | Start filling in the form                                        | No    | :th:`start` only|
+-------------------+------------------------------------------------------------------+-------+-----------------+
| question          | View a question                                                  | Yes   | Yes             |
+-------------------+------------------------------------------------------------------+-------+-----------------+
| group questions   | View multiple questions on one screen (``field-list``)           | Yes   | Yes             |
+-------------------+------------------------------------------------------------------+-------+-----------------+
| jump              | View the jump screen                                             | No    | :th:`start` only|
+-------------------+------------------------------------------------------------------+-------+-----------------+
| add repeat        | Add a repeat                                                     | Yes   | Yes             |
+-------------------+------------------------------------------------------------------+-------+-----------------+
| delete repeat     | Delete a repeat                                                  | Yes   | Yes             |
+-------------------+------------------------------------------------------------------+-------+-----------------+
| end screen        | View the end screen                                              | No    | Yes             |
+-------------------+------------------------------------------------------------------+-------+-----------------+
| form save         | Save the form                                                    | No    | :th:`start` only|
+-------------------+------------------------------------------------------------------+-------+-----------------+
| form exit         | Exit the form                                                    | No    | :th:`start` only|
+-------------------+------------------------------------------------------------------+-------+-----------------+
| form resume       | Resume the form                                                  | No    | :th:`start` only|
+-------------------+------------------------------------------------------------------+-------+-----------------+
| form finalize     | Finalize the form                                                | No    | :th:`start` only|
+-------------------+------------------------------------------------------------------+-------+-----------------+
| save error        | Error trying to save                                             | No    | :th:`start` only|
+-------------------+------------------------------------------------------------------+-------+-----------------+
| finalize error    | Error trying to finalize the form (probably encryption related)  | No    | :th:`start` only|
+-------------------+------------------------------------------------------------------+-------+-----------------+
| constraint error  | Constraint or required error on finalize                         | No    | :th:`start` only|
+-------------------+------------------------------------------------------------------+-------+-----------------+

.. _audit-timestamps:

Timestamps
-----------

If we relied entirely on the time reported by the device for timestamps, users or the network could change the device time and manipulate the correctness of the audit log. For this reason, only use device time for the form start timestamp. All subsequent event timestamps are the result of elapsed time, which users cannot change, added to the form start timestamp. This means that while the timestamps themselves may potentially be inaccurate, the time elapsed within and between the timestamps are always accurate within one form editing session.

Using epoch time makes it easy to compute elapsed time by subtracting start from end. For example, given the following log:

.. csv-table:: audit.csv
  :header: event, node, start, end

  form start, , 1488761807863, 
  question, /data/name, 1488761807868, 1488761809157

The enumerator spent ``1488761809157 - 1488761807868 = 1289`` milliseconds on the screen showing the ``/data/name`` question. This corresponds to ``1289 / 1000 = 1.289`` seconds.

To convert from epoch time to time in UTC in most common spreadsheet programs, divide the epoch time by 86400000 ms per day and add 25569 days between January 1, 1900 (what most spreadsheet programs use as "day zero") and January 1, 1970. For example, to convert the timestamp ``1488761807868``:

.. code-block:: xml

  (1488761807868 / 86400000) + 25569 = 42800.03944

When the cell is set to type :th:`date time` in common spreadsheet programs, it will show ``3/6/2017 0:56:48 UTC``. A common workflow if device time is needed in a human-readable format will be to add a column for the calculation above and change that column's type to :th:`date time`.


.. _known-audit-limitations: 

Known limitations
-------------------

If the device is turned off while a form is being filled, Collect will not record a log entry for the screen that was shown at the time of device shutdown. Events before and after the shutdown will be logged.
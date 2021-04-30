.. spelling::

  abc

Increasing Aggregate Field Length
====================================

.. warning::
  ODK Aggregate is no longer being updated. Please use :doc:`ODK Central <central-intro>` instead.

By default, Aggregate's datastore layer limits text values to 255 characters or less. If a submission includes a value longer than 255 characters, those additional characters **are not saved in the database** and no warning is shown. That means there is a risk of data loss when using question types that save long text values such as :ref:`geotrace <geotrace-widget>`, :ref:`geoshape <geoshape-widget>` or :ref:`select multiple <multi-select-widget>`. This limitation exists for performance reasons, particularly for older versions of MySQL.

It is possible to set the desired database field length for a particular question. This value can go up to about 16000 UTF-8 characters but the datastore storage efficiency may get worse as the value increases. If you go over 16000 characters, be sure to do an end-to-end test to ensure the performance is acceptable.

.. tip::

	Each geopoint is roughly 50 characters, so a geotrace or geoshape with a length of 16000 will store about 320 points.

In an XLSForm, the database field length is set from the ``bind::odk:length`` column. On form upload, Aggregate will adjust the database field length of questions that have a whole number in that column. Other questions will get a default length of 255.

.. rubric:: XLSForm

.. csv-table:: survey
  :header: type, name, label, bind::odk:length

  select_multiple opt_abc, multi, Select multi, 500
  geoshape, shape, Select an area, 1000

.. csv-table:: choices
  :header: list_name, name, label

  opt_abc, a, A
  opt_abc, b, B
  opt_abc, c, C
Briefcase and Aggregate
=========================

:doc:`ODK Briefcase <briefcase-intro>` and
:doc:`ODK Aggregate <aggregate-intro>` have
complementary and overlapping features.
For some deployments,
it makes sense to use one or the other.
In other case,
it makes sense to use them together.

This page compares Briefcase and Aggregate,
and explains their differences.

.. _briefcase-points:

Briefcase
-------------

.. include:: incl/briefcase-features.rst

.. note::

  Briefcase cannot be used to Push forms directly to Collect. However, this is not needed as you can :ref:`do this with adb <loading-blank-forms-with-adb>`.

.. _aggregate-points:

Aggregate
------------

With Aggregate you can:

- Host blank form definitions to be downloaded by Collect.
- Accept finalized form instances from Collect.
- Review and visualize submitted form data.
- Export submitted form data to :term:`CSV`, :term:`KML`, and :term:`JSON`.
- Publish data to Google Sheets or JSON servers.


.. _briefcase-aggregate-differences:

Notable Differences
----------------------

- Aggregate supports export to KML and JSON. Briefcase does not.
- Aggregate can host blank form definitions for Collect users to download over the internet. Briefcase cannot.
- Aggregate can receive form data from Collect over the internet. Briefcase cannot.
- When moving forms from Collect to Aggregate, form instances are ignored if they have not been :formstate:`finalized`. When using Briefcase, all form instances are transferred.
- Aggregate supports simple visualizations. Briefcase does not.
- Briefcase has a command line interface (CLI), while Aggregate does not. In addition to using Briefcase from a terminal, the CLI can also be scripted. No comparable scripting interface exists for Aggregate.
- Briefcase is a small and simple desktop application requiring very little setup and no maintenance. Aggregate is a full-fledged server backed by an enterprise database.

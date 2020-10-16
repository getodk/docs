Central and Briefcase
=========================

:doc:`briefcase-intro` is a desktop application which provides access to the Central API from graphical and command-line interfaces. It can make it easier for non-developers to automate some aspects of data management. In particular, it is useful for migrating data from another ODK-compatible server to Central.

Briefcase was created to provide features that the older ODK server, Aggregate, did not have. With Central, we encourage users to either :doc:`use data exports from the Central interface <central-submissions>` or to write scripts to interact directly with the :doc:`Central API <central-api>`. If you find yourself reaching for Briefcase a lot with Central, we would like to hear about what features you use it for `on the forum <https://forum.getodk.org/c/support/6>`_.

.. warning::

  Pulling and pushing media files is memory intensive. If you get a “Success with errors” status from Briefcase, we recommend increasing your Central server memory. If increasing memory is not an option, you can also :ref:`add swap <central-install-digital-ocean-swap>`.

Migrating from another ODK-compatible server to Central
--------------------------------------------------------

In most contexts where an existing ODK-compatible server is in use, we recommend completing ongoing data collection projects before switching to Central. However, some long-running studies may want to make the switch before project completion. There may also be some contexts where storing data from past data collection projects in Central makes sense.

ODK Briefcase can be used to perform a migration of both blank forms and form submissions to Central. Please be aware of the following limitations:

* The submission date for all records will be the date that they were migrated to Central, not the date that they were submitted to the original server.
* The submitter for all records will be the user that performs the migration. You may want to create a special user for this purpose and name it something like “Aggregate Migration”.
* Briefcase only keeps track of the latest published form version. For forms that have multiple form versions on the source server, Briefcase will upload the same form definition with different version identifiers. :ref:`Learn more <briefcase-push-to-central>`.
* Migrating multi-version forms where one of the versions is blank is not currently supported automatically. If you need this, we recommend first manually uploading the form definition with a blank version and publishing it. Then you can proceed as normal.


.. _briefcase-push-to-central:

Pushing forms with multiple versions to Central
------------------------------------------------

.. note::

  Briefcase v1.18+ must be used for both the initial pull and the push.

.. warning::

  Pushing multi-version forms where one of the versions is blank is not currently supported. If you need this, we recommend first manually uploading the form definition with a blank version and publishing it. Then you can proceed as normal.

Briefcase only keeps track of the latest published form version. Central only accepts submissions if it knows about the form version that it was created with. To address this, Briefcase v1.18+ inspects submissions as they are pulled and identifies all of the form versions that are referenced in submissions. On push, Briefcase first pushes and publishes the form definition with versions other than the published one. These are pushed in alphanumerical order. Then it pushes and publishes the form definition with the current version.

Because Briefcase only knows about the latest form version, it can't push the real older versions. Instead, it pushes the same form definition with different declared versions. This will generally be acceptable because currently, the only thing that can be done with older form versions in Central is to download them. If you’d like to have access to historical edits of the form, you may want to manually upload all of the actual definitions before you push submissions. Be sure to upload the form versions from oldest to newest because the last published definition will be the active one.

If you have pulled submissions with a Briefcase version prior to v1.18, Briefcase will not know what versions submissions correspond to. It will push and publish the active form version and any submissions corresponding to that form version will succeed. However, any submissions corresponding to other form versions will fail. If you let the push complete, you can then retry and Briefcase will create the missing form versions and push the corresponding submissions.

If you end up in a state where the published version is not the correct one, re-upload the form definition that you would like to have published and give it a new version name.

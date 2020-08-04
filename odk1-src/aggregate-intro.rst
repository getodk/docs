ODK Aggregate
===================

.. warning::
  Aggregate is no longer actively developed. Please use :doc:`ODK Central <central-intro>` instead.

.. _aggregate-introduction:

:dfn:`ODK Aggregate` is the original ODK server. We now encourage using :doc:`ODK Central <central-intro>` which has been developed to address many of the challenges reported by Aggregate users. However, we know that switching may not be immediately practical so we intend to continue providing this documentation.

Aggregate is an open source Java application that
stores, analyzes, and presents :doc:`XForm <form-design-intro>` survey data collected using :doc:`collect-intro` or other :doc:`OpenRosa-compliant applications <openrosa>`. It supports a wide range of data types, and is designed to work well in any hosting environment.

With Aggregate, data collection teams can:

- :doc:`Host <aggregate-forms>` blank :doc:`XForms <form-design-intro>` used by ODK Collect or other OpenRosa clients
- :doc:`Store and manage XForm submission data <aggregate-data>`
- Visualize collected data using :doc:`maps <aggregate-visualize>` and :ref:`simple graphs <visualize-submissions>`
- :doc:`Export and publish data in a variety of formats <aggregate-data-access>`

Aggregate can be hosted on cloud providers such as :doc:`DigitalOcean <aggregate-digital-ocean>`, and :doc:`Amazon Web Services <aggregate-aws>`, or :doc:`your own local or cloud server <aggregate-tomcat>`.
There's also a :doc:`pre-configured virtual machine image <aggregate-vm>`
that is ready to deploy on any computer.

.. image:: /img/aggregate-intro/aggregate-form-data.*
  :alt: A screenshot of ODK Aggregate. A table view showing data collected using a form.

.. image:: /img/aggregate-intro/aggregate-pie-chart.*
  :alt: A screenshot of ODK Aggregate. A pie chart visualizing data collected using a form.

.. _aggregate-learn-more:

Learn more about ODK Aggregate
--------------------------------

- :doc:`aggregate-setup`
- :doc:`aggregate-use`
- :doc:`getting-started`


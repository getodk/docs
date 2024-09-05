.. spelling:word-list::
    lang
    OutOfMemoryError

Troubleshooting Collect
========================

If you experience unexpected behavior in Collect, we strongly encourage you to post to `the forum <https://forum.getodk.org/>`_. Not only will this likely help you address your short-term need, it may also help the development team make improvements to the application that benefit all users. We consider reporting issues a very important contribution to the project, thank you!

Here are some known issues and how to address them.

Fatal Exception: java.lang.OutOfMemoryError
-------------------------------------------

This means Collect needs more memory than it has access to. The error usually includes details like:

  Failed to allocate a 24 byte allocation with 2858136 free bytes and 2791KB until OOM, target footprint 536870912, growth limit 536870912; giving up on allocation because <1% of heap free after GC.

This generally occurs with forms that have a lot of complex :doc:`logic <form-logic>`, many :ref:`repeat instances <repeats>`, or 60k+ elements in a choice list, Entity List or attached data file. It may also occur with simple forms if many applications are open on a device or if a device has 1 GB or less of RAM. It's particularly likely to happen the first time that a form or form update is opened. We generally recommend devices with at least 4 GB of RAM for complex forms.

Sometimes this error is related to a temporary state and can be resolved by restarting the device, `closing Collect <https://support.google.com/android/answer/9079646?hl=en#zippy=%2Cclose-apps>`_ or closing other applications.

If that doesn't help, consider simplifying the form. For example, could you remove some choices from your choice list or attached document? Could you split a form with a lot of logic into two separate forms filled in at different times? Could you limit the number of repeats created in a single submission?

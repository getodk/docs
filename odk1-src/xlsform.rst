XLSForm
=======

.. _xlsform-introduction:

:dfn:`XLSForm` is a tool to simplify the creation of forms. Forms designed with Excel can be converted to *XForms* that can be used with ODK tools.

To design your form, refer to the `XLSForm form design documentation <http://xlsform.org/>`_. Once the form has been designed, use `XLSForm Online <https://opendatakit.org/xlsform>`_, `XLSForm Offline <https://github.com/opendatakit/xlsform-offline/releases/latest>`_, or if you are comfortable on the command line, :ref:`pyxform <running-pyxform>`.

.. tip::

  Forms do not have to be uploaded to :ref:`Aggregate <aggregate-introduction>` before they are used. They can be manually added to :ref:`Collect <collect-introduction>`. Place them in the :file:`/odk/forms` folder on your Android device’s SD card.


XLSForm Online
--------------

We recommend starting with XLSForm Online because it is always up-to-date and allows you to preview what the form will look like.

Use `XLSForm Online <https://opendatakit.org/xlsform>`_

.. _xlsform-offline:

XLSForm Offline
---------------

XLSForm Offline is a great option for users who do not have a reliable connection or may need to design forms offline.

Download `XLSForm Offline <https://github.com/opendatakit/xlsform-offline/releases/latest>`_.

.. tip::

  There is a validation option in the XLSForm Offline that requires Java. To enable this option, download and install `Java <http://java.com/en/download>`_ and ensure Java is in your PATH. See `How do I set or change the PATH <http://java.com/en/download/help/path.xml>`_ for more.

.. note::

  Your anti-virus may report that XLSForm Offline has a virus. This is a false positive that is triggered because virus writers sometimes use the same components we use. You can confirm the safety of XLSForm Offline by using the free and unbiased `VirusTotal <https://www.virustotal.com>`_. You may also use `XLSForm Online <https://opendatakit.org/xlsform>`_ as an alternative.

  On macOS 10.7 or later, you may get a dialog on startup warning you that the XLSForm Offline is from an unidentified developer. Control-click or right click the icon of the app to bypass this dialog. See `About Gatekeeper <https://support.apple.com/en-us/HT202491>`_ for more.

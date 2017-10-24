Intro to Forms in ODK
========================

Forms used in the ODK ecosystem are XML documents following the `ODK XForms specification <https://opendatakit.github.io/xforms-spec/>`_, a subset of the `W3C XForms specification <https://www.w3.org/TR/xforms/>`_. Most ODK tools use the `ODK Javarosa <https://github.com/opendatakit/javarosa>`_ library to render forms. Form transfer between ODK components is governed by the :doc:`openrosa` API.

Because of the complexity of the XForms format, we do not recommend "hand-coding" XForms. The recommended process is:

- Begin with one of the :ref:`compliant-build-tools`.
- :ref:`Edit the XML only if neccessary <>`.
- Use :doc:`validate` to check that form is well-formed and fully compliant.


.. _compliant-build-tools:

JavaRosa-compliant build tools
---------------------------------

Most ODK users design their forms in Excel, following the `XLSForm <http://xlsform.org/>`_ specification. To convert XLSForms to XForms, you can use:

- `ODK's online XLSForm converter <http://opendatakit.org/xiframe/>`_
- `XLSForm Offline for Mac or Windows <https://gumroad.com/l/xlsform-offline>`_
- - `XLSForm for Windows <https://opendatakit.org/downloads/download-info/xlsform-for-windows/>`_
- `Pyxform, a Python XLSForm conversion library <https://github.com/uw-ictd/pyxform>`_

For simple forms, `ODK Build <https://opendatakit.org/use/build/>`_ is an online drag-and-drop form designer.

.. _other-xform-build-tools:

Other XForm build tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These tools product XForms that *may not* strictly comply with the JavaRosa library. 

- `Kobo <http://www.kobotoolbox.org/>`_
- `Enketo <https://enketo.org/>`_
- `purcforms <https://code.google.com/archive/p/purcforms/>`_


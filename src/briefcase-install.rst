:orphan:

Setting Up ODK Briefcase
===================================

.. warning::
  ODK Briefcase is no longer being updated. If you're using Briefcase for CSV exports, data decryption, or automation, use :doc:`ODK Central <central-intro>` instead.

.. admonition:: Before you begin...

  We verify Briefcase with Java 11. We recommend installing `OpenJDK 11 LTS <https://adoptopenjdk.net/>`_ from AdoptOpenJDK.

#. Download the ODK Briefcase JAR file from `GitHub <https://github.com/getodk/briefcase/releases/latest>`_.

	Some browsers may warn that JAR files might harm your computer. Do not worry, Briefcase when downloaded from our GitHub page is safe.

#. Double-click the downloaded JAR file or, from the command line, run :code:`java -jar {path/to/ODK-Briefcase-vX.Y.Z.jar}`

	macOS will warn that Briefcase is from an unidentified developer. This is normal and expected. Follow `these instructions from Apple <https://support.apple.com/kb/ph25088?locale=en_US>`_ to open the file.

#. Follow the instructions to start using Briefcase

  .. image:: img/briefcase-install/welcome.png

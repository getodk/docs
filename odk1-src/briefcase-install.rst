Setting Up ODK Briefcase
===================================

.. admonition:: Before you begin...

  You should be able to run Briefcase with Java 8 or higher, but we recommend using `Java 11 LTS <https://www.oracle.com/technetwork/java/javase/downloads/index.html>`_.

#. Download `ODK Briefcase <https://github.com/opendatakit/briefcase/releases/latest>`_.

   You may wish to move the Briefcase file to your desktop, your Applications directory, or another location.

#. Open the file.

   - Double click the file icon.
   - Or, from the command line:

     .. code-block:: console

       $ java -jar {path/to/Briefcase}

#. Set your local **Briefcase Storage** location.

   .. _briefcase_storage:

   The first time you open Briefcase, you will need to select a directory for storing forms and submission data. A new directory called :file:`ODK Briefcase Storage` will be created under the directory you select.

   .. note::

     We will refer to the term `Briefcase Storage` from now on to indicate the location of the :file:`ODK Briefcase Storage` directory

   .. tip::

     You can change the Briefcase Storage location later, from the :guilabel:`Settings` tab.

Setting Up ODK Briefcase
===================================

.. note:: 

  The ODK Briefcase file available for download is an executable Java application. Once downloaded, it can be run directly and does not need to be "installed."

.. admonition:: Before you begin...

  Make sure `Oracle Java 8 <https://java.com/en/download/>`_ or higher is `installed on your system <https://www.java.com/en/download/help/download_options.xml>`_.

  We require Oracle's Java because OpenJDK has encryption shortcomings.
  
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

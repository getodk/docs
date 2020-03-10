Installing Application Designer
====================================

.. _app-designer-install:

Download the |app_designer_link| zip file.

.. |app_designer_link| raw:: html

  <a href="https://github.com/opendatakit/app-designer/releases/latest" target="_blank">Application Designer</a>

Unzip the file you downloaded and move the resulting folder to somewhere other than your :file:`Downloads` directory; such as your :file:`Documents` folder.

To open Application Designer, navigate to the location of your unzipped folder in :program:`cmd`, and type: 

.. code-block:: console

   $ grunt

This command runs the script contained in :file:`Gruntfile.js`, so be sure it is in the current directory.  

.. admonition:: Windows Users Tip

  You will be opening a :program:`cmd` window and changing your current directory (using the :program:`cd` command) into this directory every time you use this tool. It is therefore useful to create a shortcut that opens a :program:`cmd` window directly into this directory:

    #. Open a file browser and navigate to the unzipped directory containing a number of files and directories, including a :file:`Gruntfile.js`.
    #. Click into the top location bar that displays the nested list of folders to this folder.
    #. Copy this path to the cut-and-paste buffer.
    #. Now, move down to the list of files, right-click.
    #. Select :guilabel:`New...`, :guilabel:`Shortcut`.
    #. Type :program:`cmd` for the location of the item.
    #. Click :guilabel:`Next`, and then :guilabel:`Finish`.
    #. Select this newly-created :program:`cmd.exe` shortcut and right-click.
    #. Select :guilabel:`Properties`.
    #. Click on the :guilabel:`Start in` text box, delete its contents, and paste the path to this folder.
    #. Click :guilabel:`OK` to accept the change.
    #. Double-click the :program:`cmd.exe` shortcut to open a :program:`cmd` window.
    #. Confirm that it opens in the intended directory (you should see the full path to that directory displayed to the left of the blinking cursor).


.. admonition:: MacOSX Users Tip

  :program:`Terminal` will open a new :program:`terminal` window if you drag a folder (or pathname) onto the :program:`Terminal` application icon, and you can also drag a folder to the tab bar of an existing window to create a new tab in that folder.

You have now completed the installation of the ODK-X Application Designer software.

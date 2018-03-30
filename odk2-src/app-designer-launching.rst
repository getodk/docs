Launching the Application Designer
=====================================

.. _app-designer-launching:

The ODK Application Designer is both

  #. a workspace containing the cohesive interacting set of forms and files you have created and
  #. a set of tools used for that development.

.. tip::

  We recommend unzipping and creating a new :file:`Application Designer` directory for each new set of ODK Survey forms, ODK Scan forms, and ODK Tables files that are not intended to be deployed as a cohesive unit. If you need to have several of these sets of forms and files co-resident on the same Android device, you would create different application names for each set. The standard set up uses the default application name (appropriately entitled ``default``). To create a new application name, create a folder with that name next to your default app and make sure it is stored on the device in the opendatakit folder.  The underlying ODK 2 tools will then keep each of these sets of forms and files isolated from each other.

To launch the application designer, open the :program:`cmd` shortcut or :program:`Terminal` window onto the directory containing :file:`Gruntfile.js` (the unzipped :file:`ODK Application Designer` directory) and type:

.. code-block:: console

  $ grunt

This should automatically open :program:`Chrome` and display the **Preview** tab. When you need to stop the server, return to the :program:`cmd` or :program:`terminal` window where you typed the :program:`grunt` command and press :kbd:`Ctrl+c`. This will stop the process.

.. warning::

  If you have Parallels or other virtualization software running, it might try to open :program:`Chrome` in this system by default. If so, you should still be able to navigate to http://localhost:8000/index.html.

.. warning::

  If the :program:`Chrome` browser does not open, try opening it yourself and browsing to http://localhost:8000/index.html.

.. warning::
  If the page never times-out, but never loads (it remains blank or constantly spinning), then stop :program:`grunt` and try this command instead:

  .. code-block:: console

    $ grunt --verbose connect:livereload:keepalive

  This will start :program:`grunt`, but disable the file-change detection mechanisms that automatically reload an HTML page when it or any JavaScript file it uses has been modified. Others have reported that uninstalling :program:`npm` and :program:`node`, and then re-installing them may correct the issue.


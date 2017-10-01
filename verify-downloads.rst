Verifying Downloads
=====================

The `downloads page <https://opendatakit.org/downloads/>`_ now has a `link <https://opendatakit.org/wp-content/uploads/sha256_signatures.txt>`_ to a file listing the SHA256 hashes for all download files.

The long hash strings in that file can be used to confirm that the file you download is not truncated, incomplete or altered.

.. image:: /img/download-verify/sha256-signatures.png
   :alt: Image showing file which contains SHA256 hashes for all downloads.

Verifying on Linux and Mac
---------------------------

- Open a terminal window.
- Navigate to the folder containing the file you downloaded. ( cd "path/to/file" )
- Then type `sha256sum "filename"` on the terminal.
  
   .. code-block:: console

     $ cd path/to/file
     $ sha256sum "filename"

.. image:: /img/download-verify/terminal-verify.*
   :alt: Image showing process of verifying downloads in Linux.  



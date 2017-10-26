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
- Then type :command:`sha256sum "filename"` on the terminal.

   .. code-block:: console

     $ cd path/to/file
     $ sha256sum "filename"

.. image:: /img/download-verify/terminal-verify.*
   :alt: Image showing process of verifying downloads in Linux.


Verifying on Windows
---------------------

- Open a cmd window.
- Navigate to the folder containing the file you downloaded ( cd "path/to/file" ).
- Then type :command:`certUtil -hashfile "filename" SHA256` on your command prompt.

  .. code-block:: doscon

     > cd path/to/file
     > certUtil -hashfile "filename" SHA256

.. image:: /img/download-verify/cmd-verify.*
   :alt: Image showing process of verifying downloads in Windows.

If the downloaded file is not corrupted, the long hash string printed by these tools will match the one listed for that file in the `link <https://opendatakit.org/wp-content/uploads/sha256_signatures.txt>`_ at the top of our `downloads page <https://opendatakit.org/downloads/>`_.

To check this :-

- Copy the SHA256 hash displayed on your terminal or cmd.

.. image:: /img/download-verify/copy-signature.*
   :alt: Image showing copying SHA256 signature.

- Then open the `link <https://opendatakit.org/wp-content/uploads/sha256_signatures.txt>`_ which contains the list of all SHA256 hashes for the downloaded files.

- Press Ctrl+F in the window and paste the copied signature in the box which opens on the top right corner. You will get a single result highlighted if the signature is found.

.. figure:: /img/download-verify/verified.*
   :alt: Image showing single search result found in the file.

   Match for hash found

.. figure:: /img/download-verify/not-verified.*
   :alt: Image showing no matches found for the hash.

   No match found for the hash

.. tip::

   - In Linux terminal, the name of the downloaded file is also printed along with the hash. Be careful not to copy it.
   - When you get a match, also check that the name of the file in the list aside the hash is the same as that of your downloaded file.  

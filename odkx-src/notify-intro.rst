ODK-X Notify
=================

.. _notify-intro:

:dfn:`ODK-X Notify` has 2 components:

- Desktop application(Skunkworks-Parrot) 
- Mobile application(Skunkworks-Bat)

:program:`Skunkworks-Parrot` is the desktop application, written in Java, that provides a user interface for writing messages, creating user groups to receive them, and sending those messages via the Firebase Cloud Messaging. 

:program:`Skunkworks-Bat` is the Android application that receives these messages via Firebase, checks the user credentials to see if the user is in the group that should receive this message, and displays the message to the user. 


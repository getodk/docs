Best practices for ODK Collect
================================

.. _create-shortcut:

Creating Android desktop shortcut to launch specific form
------------------------------------------------------------

1. Click on :guilabel:`Apps` button at the bottom of the screen.

.. image:: /img/collect-best-practices/apps.png
   :alt: Image showing Apps button.
   :class: device-screen-vertical

2. :gesture:`Touch and hold` on an empty space on the Home screen and then click on :guilabel:`Widgets` button at the bottom of the screen.

.. image:: /img/collect-best-practices/widgets.png
   :alt: Image showing Widgets button.
   :class: device-screen-vertical

3. Find the :guilabel:`ODK Form` widget and then :gesture:`touch and hold` it.

.. image:: /img/collect-best-practices/odk-form.png
   :alt: Image showing ODK Form widget.
   :class: device-screen-vertical

4. A menu pops up listing all the available forms. Select the form you wish to create a shortcut for.

.. image:: /img/collect-best-practices/form-list.png
   :alt: Image showing form list.
   :class: device-screen-vertical

5. Shortcut for the selected form will appear on your home screen. You can move the shortcut to the desired position by :gesture:`drag and drop`.

.. image:: /img/collect-best-practices/form-shortcut.png
   :alt: Image showing form shortcut.
   :class: device-screen-vertical

.. note::

  To delete the shortcut, hold and press it. A :guilabel:`Remove` button will appear on the top right corner. :gesture:`Drag and drop` the shortcut to the :guilabel:`Remove` button. The shortcut will be removed.

  .. image:: /img/collect-best-practices/remove.png
     :alt: Image showing Remove button.
     :class: device-screen-vertical

.. tip::

   If you are unable to find :guilabel:`Widgets` option:

   1. Click on :guilabel:`Apps` and then click on three dots at the top right corner of your screen.

   .. image:: /img/collect-best-practices/home-screen.png
      :alt: Image showing three dots on home screen.
      :class: device-screen-vertical

   |

   2. Click on :guilabel:`Help` option in the dropdown.

   .. image:: /img/collect-best-practices/help.png
      :alt: Image showing Help option.
      :class: device-screen-vertical
   
   |

   3. Click on :menuselection:`Adding Items` option in the menu which appears.

   .. image:: /img/collect-best-practices/add-items.png
      :alt: Image showing Adding Items option.
      :class: device-screen-vertical

   |

   4. Information about adding widgets will be displayed. You can then follow it or try it to find the :guilabel:`Widgets` button.

   .. image:: /img/collect-best-practices/help-describe.png
      :alt: Image showing guidelines on adding a widget.
      :class: device-screen-vertical

.. _location-tips:

Tips on Location
------------------

When you need to specify location in any survey form, you may get a warning message which says: **Sorry, location providers are disabled** and a screen will open asking you to enable location providers.

.. image:: /img/collect-best-practices/example-form.png
   :alt: Image showing form with a question to specify location.
   :class: device-screen-vertical

.. image:: /img/collect-best-practices/warning-message.png
   :alt: Image showing warning message.
   :class: device-screen-vertical

.. _location-providers:

Enable/Disable location providers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   

To turn your device's location providers on/off:

1. Open your device's Settings app.

.. image:: /img/collect-best-practices/settings.png
   :alt: Image showing Settings app.
   :class: device-screen-vertical

2. :gesture:`Tap` :guilabel:`Location`. 

.. image:: /img/collect-best-practices/location.png
   :alt: Image showing Location option.
   :class: device-screen-vertical

.. tip::

  If you don't see "Location",  :gesture:`tap` :guilabel:`Security & Location` and then :guilabel:`Location`.

3. Turn Location on or off.

.. figure:: /img/collect-best-practices/location-off.png
   :alt: Image showing Location off.
   :class: device-screen-vertical

   Location providers disabled.

.. figure:: /img/collect-best-practices/location-on.png
   :alt: Image showing Location on.
   :class: device-screen-vertical

   Location providers enabled.   

.. _location-mode:

Change location mode   
~~~~~~~~~~~~~~~~~~~~~~~

You can also choose your location mode based on accuracy, speed, and battery use. Android can help improve location accuracy by triangulating your location off nearby Wi-Fi access points or cell towers. Combined with data available from your ailing GPS signal, turning on Wi-Fi will greatly improve location accuracy under most conditions.

In the Location section, :gesture:`tap` on :guilabel:`Mode`. 

.. image:: /img/collect-best-practices/mode.png
   :alt: Image showing Mode option.
   :class: device-screen-vertical

Then pick:

  - **High accuracy**: This mode uses GPS, Wi-Fi, mobile networks, and other sensors to get the highest-accuracy location. It uses Google's Location service to help estimate your device's location faster and more accurately.
 
  - **Power saving** or **Battery saving**: This mode uses sources that use less battery, like Wi-Fi and mobile networks. It uses Google's Location service to help estimate your device's location faster and more accurately.

  - **GPS only** or **Device only**: This mode uses only GPS. It doesn’t use Google's Location service to provide location information. It can estimate your device's location slower and use more battery.

.. image:: /img/collect-best-practices/accuracy-mode.png
   :alt: Image showing different accuracy modes.
   :class: device-screen-vertical

.. _improve-accuracy:

Improve location accuracy
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also improve accuracy of location.

:gesture:`Tap` on :guilabel:`Improve accuracy` in Location section.

.. image:: /img/collect-best-practices/improve-accuracy.png
   :alt: Image showing Improve-accuracy option.
   :class: device-screen-vertical

Then enable:

- **Wi-Fi scanning**: Allow apps and services to scan for Wi-Fi networks automatically, even when Wi-Fi is turned off.
- **Bluetooth scanning**: Allow apps and services to scan for and connect to nearby devices automatically via Bluetooth, even when Bluetooth is turned off.

.. image:: /img/collect-best-practices/improve-accuracy-mode.png
   :alt: Image showing Wi-Fi scanning and Bluetooth scanning options.
   :class: device-screen-vertical

.. note::

  Google has added Bluetooth scanning support to further improve location accuracy with  Android 6.0 Marshmallow.

For more details on location services, see `this guide <https://support.google.com/nexus/answer/3467281?hl=en>`_.


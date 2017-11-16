Improving Location Performance
==================================
	
When you need to specify location in any survey form, you may get a warning message which says: **Sorry, location providers are disabled** and a screen will open asking you to enable location providers.

.. image:: /img/collect-best-practices/example-form.png
   :alt: Image showing form with a question to specify location.
   :class: device-screen-vertical

.. image:: /img/collect-best-practices/warning-message.png
   :alt: Image showing warning message.
   :class: device-screen-vertical

.. _location-providers:

Enable/Disable location providers
-----------------------------------

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
-------------------------

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
----------------------------

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

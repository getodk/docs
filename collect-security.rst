Android security recommendations
==================================

.. _data-encrypt:

Turn on data encryption
--------------------------

Turning on Android-level data encryption means when the device is locked, no one can see the data. Unlocking your encrypted device decrypts your data. Encryption can add protection in case your device is stolen. It's an easier alternative to using encrypted forms that offer most of the benefits. 

.. tip::

  Encryption takes an hour or more to complete. Before you start, ensure that battery is charged and keep the device plugged in until encryption is complete. Make sure your data is backed up, just in case something goes wrong.

.. warning::

  - Interrupting encryption process may lead to loss of some or all of your data. 
  - The process is irreversible. The device cannot be decrypted once the encryption is setup and you will have to wipe out all the data for decryption or removing encryption.

.. note::

  For devices running any version older than 4, you’ll need to either upgrade your operating system or consult the manufacturer’s instructions.

For devices running Android version 4 or later:

1. Open your device's Settings app.

   .. image:: /img/collect-best-practices/settings.png
      :alt: Image showing Settings app.
      :class: device-screen-vertical

2. :gesture:`Tap` :guilabel:`Lock screen` in the :guilabel:`Device` section. Then :gesture:`tap` on :guilabel:`Screen lock` and create a pin or password.

   .. image:: /img/collect-best-practices/lock-screen.png
      :alt: Image showing Lock screen option in the Device section.
      :class: device-screen-vertical

   .. image:: /img/collect-best-practices/screen-lock.png
      :alt: Image showing Screen lock option.
      :class: device-screen-vertical

   .. image:: /img/collect-best-practices/pin-or-password.png
      :alt: Image showing Pin and Password options.
      :class: device-screen-vertical   

   .. note::

      Encryption cannot be performed until you have setup either a PIN or a password lock. Pattern lock is not allowed with encryption.

   .. tip::

     Setting a strong passcode is imperative to protect your Android phone. The longer the passcode (or alphanumeric password), the tougher it will be for an attacker to gain access to your device. 
     Even a lock screen won't necessarily prevent a thief or hacker from getting access to your data. You can use apps that destroy all the data after few failed attempts to unlock the device. For more details, see `this <https://www.techrepublic.com/blog/five-apps/five-apps-to-wipe-data-from-your-android-phone/>`__.

3. :gesture:`Tap` :guilabel:`Security` in the :guilabel:`System` section.

   .. image:: /img/collect-best-practices/security.png
      :alt: Image showing Security option in the System section.
      :class: device-screen-vertical

4. Go to :guilabel:`Encryption` section. Now select :guilabel:`Encrypt device` to start encryption. Follow the onscreen instructions. During encryption, your device might restart several times.

   .. image:: /img/collect-best-practices/encrypt-device.png
      :alt: Image showing Encrypt device option in the Encryption section.
      :class: device-screen-vertical

   .. note::

     On some phones, you’ll need to choose :guilabel:`Storage`, then :menuselection:`Storage encryption` or :menuselection:`Storage --> Lock screen and security --> Other security settings` to find the :guilabel:`Encrypt device` option

.. note::

  If you are using SD card for storage, you can encrypt that too by choosing :guilabel:`Encrypt SD card` in the :guilabel:`Encryption` section. This not only encrypts the contents of the SD card, but it also means that the card cannot be used on another device unless it is wiped.
  
  .. image:: /img/collect-best-practices/encrypt-sdcard.png
     :alt: Image showing Encrypt SD card option in the Encryption section.
     :class: device-screen-vertical


.. tip::

  You should also ensure that device debugging (via adb) is disabled when collecting data, as that can enable users to pull data from the device after it has been successfully booted (when the sdcard encryption key is entered). i.e., if the debugging interface is enabled, someone could steal the device, connect it to a laptop, and pull data off it as long as it has not been shut down as they don't need to successfully unlock the device's lock screen to gain access.  

For more details on encryption, see `this <https://docs.microsoft.com/en-us/intune-user-help/encrypt-your-device-android>`__.  

.. _play-store-password:

Adjust Google Play to require a password for every purchase
-------------------------------------------------------------

You can set up Google Play to require a password for every purchase, which makes sure that anything you buy is done so with your consent. This can prevent enumerators from installing apps which can bypass certain specified requirements.

1. Open the Play store app, :gesture:`tap` on the left-hand slide-out menu, and then choose :guilabel:`Settings`.

   .. image:: /img/collect-best-practices/play-store.png
      :alt: Image showing Play store app.
      :class: device-screen-vertical

   .. image:: /img/collect-best-practices/play-store-menu.png
      :alt: Image showing three horizontal bars. Tap on them to display slide-out menu.
      :class: device-screen-vertical

   .. image:: /img/collect-best-practices/play-store-settings.png
      :alt: Image showing Settings option in menu.
      :class: device-screen-vertical

2. Look for :guilabel:`Require password for purchases` and :gesture:`tap` on it. You'll be asked to input your password.

   .. image:: /img/collect-best-practices/require-authentication.png
      :alt: Image showing Require password for purchases option.
      :class: device-screen-vertical

   .. image:: /img/collect-best-practices/enter-password.png
      :alt: Image showing box where you will need to input a password.
      :class: device-screen-vertical   

3. Choose the password input frequency as :guilabel:`For all purchases through Google Play on this device`.

   .. image:: /img/collect-best-practices/authenticate-option.png
      :alt: Image showing options for password input frequency: For all purchases through Google Play on this device, Every 30 minutes, Never.
      :class: device-screen-vertical

.. note::

  The password will not be set for free downloads. If you want to lock free downloads as well, use an app locking app like `AppLock <https://play.google.com/store/apps/details?id=com.domobile.applock>`_.


.. _disable-backup:

Disable cloud-based backup
-------------------------------

Though storing your data in the cloud is good for backing it up, law enforcement can demand that Google turn over your data. The best way to keep your Android phone from sending your personal data to its servers is to turn off backup. The downside is if you lose your phone, you may lose your data. Remember, you always have the option to manually back-up to your personal computer.

To disable backup:

1. Go to Settings app.

   .. image:: /img/collect-best-practices/settings.png
      :alt: Image showing Settings app.
      :class: device-screen-vertical

2. Then :gesture:`tap` :guilabel:`Backup & Reset` in :guilabel:`Personalisation` section.

   .. image:: /img/collect-best-practices/backup-reset.png
      :alt: Image showing Backup and reset option in the Personalisation section.
      :class: device-screen-vertical

3. Now switch off the option to :guilabel:`Back up my data`. 

   .. image:: /img/collect-best-practices/backup-data.png
      :alt: Image showing Back up my data option.
      :class: device-screen-vertical

   .. image:: /img/collect-best-practices/backup-off.png
      :alt: Image showing Backup turned off.
      :class: device-screen-vertical   

.. _limit-google-now:

Limit who can use Google Now
-------------------------------

Google Now is your own intelligence assistant by bringing information to you when you need it but that gives Google a lot of access to your data to know what to dig up. The best way to use it is by turning it off from the lock screen, so only you with your passcode can use the feature and get access to your personal data. The steps to do this are as follows:

1. Open the Google app, :gesture:`tap` on the left-hand slide-out menu, and then choose :guilabel:`Settings`.

   .. image:: /img/collect-best-practices/google-app.png
      :alt: Image showing Google app.
      :class: device-screen-vertical   

   .. image:: /img/collect-best-practices/google-menu.png
      :alt: Image showing Google app menu.
      :class: device-screen-vertical   

   .. image:: /img/collect-best-practices/google-settings.png
      :alt: Image showing Settings option in the slide-out menu.
      :class: device-screen-vertical   

2. :gesture:`Tap` on :guilabel:`Voice` in the :guilabel:`Search` section and then choose :guilabel:`'OK Google' detection`.

   .. image:: /img/collect-best-practices/google-voice.png
      :alt: Image showing Voice option in the Search section.
      :class: device-screen-vertical 

   .. image:: /img/collect-best-practices/ok-google-detect.png
      :alt: Image showing OK Google detection option.
      :class: device-screen-vertical      

3. Turn off the feature :guilabel:`Say "OK Google" any time`.

   .. image:: /img/collect-best-practices/turn-off-ok-google.png
      :alt: Image showing OK Google feature turned off.
      :class: device-screen-vertical   

.. _lower-sleep-timeout:

Lower your phone's sleep timeout
-----------------------------------

Lowering your phone's sleep timeout can prevent opportunistic people from getting access to your unlocked device. The lower the figure, the quicker it locks you out.

1. Start by going to Settings app.

   .. image:: /img/collect-best-practices/settings.png
      :alt: Image showing Settings app.
      :class: device-screen-vertical

2. :gesture:`Tap` on :guilabel:`Display and wallpaper` under the :guilabel:`Device` section.

   .. image:: /img/collect-best-practices/display.png
      :alt: Image showing Display and wallpaper option in the Device section.
      :class: device-screen-vertical

3. :gesture:`Tap` on :guilabel:`Screen timeout` and lower the screen timeout by choosing an appropriate timeout from the list.

   .. image:: /img/collect-best-practices/screen-timeout.png
      :alt: Image showing Screen timeout option.
      :class: device-screen-vertical

   .. image:: /img/collect-best-practices/set-timeout.png
      :alt: Image showing list of timeout to choose from.
      :class: device-screen-vertical

4. Once you've lowered your phone's sleep timeout setting, you need to make sure that your Android device locks and presents the lock screen when it wakes up. :gesture:`Tap` on :guilabel:`Lock screen` in the :guilabel:`Device` section and then :gesture:`tap` on :guilabel:`Lock automatically` option and choose an appropriate timeout again. 

   .. image:: /img/collect-best-practices/lock-screen.png
      :alt: Image showing Lock screen option in the Device section.
      :class: device-screen-vertical

   .. image:: /img/collect-best-practices/lock-automatic.png
      :alt: Image showing Lock automatically option.
      :class: device-screen-vertical   

   .. image:: /img/collect-best-practices/set-lock-automatic.png
      :alt: Image showing list of timeout to choose from.
      :class: device-screen-vertical   

.. _limit-notification:

Limit your lock screen notifications
--------------------------------------

Your lock screen can show a lot about your life. Your Android phone or tablet can limit what's shown on the lock screen in order to prevent others' from seeing your personal content as it comes in.

1. Go to Settings app then :gesture:`Tap` on :guilabel:`Sounds & notifications` under the :guilabel:`Device` section.

   .. image:: /img/collect-best-practices/settings.png
      :alt: Image showing Settings app.
      :class: device-screen-vertical

   .. image:: /img/collect-best-practices/sound-notification.png
      :alt: Image showing Sounds and notifications option in the Device section.
      :class: device-screen-vertical   

2. Scroll down and :gesture:`tap` on :guilabel:`Notifications on lock screen` under the :guilabel:`Notification` section. You can change how notifications are shown when device is locked setting. The most privacy conscious setting is to Hide sensitive notification content so that you know which app is alerting you, without showing its contents.

   .. image:: /img/collect-best-practices/notify-lock-screen.png
      :alt: Image showing Notifications on lock screen option in the Notification section.
      :class: device-screen-vertical

   .. image:: /img/collect-best-practices/notify-options.png
      :alt: Image showing options: Show content, Hide content, Do not show notifications.
      :class: device-screen-vertical   

.. _unauthorized-apps:

Prevent unauthorized apps from installing
---------------------------------------------

Android devices can run third-party content outside of the Google Play app store. This can open up a device to malware attacks.

The easiest way to ensure that only verified and malware-checked apps can be installed on your phone or tablet is:

1. Go to the Settings app and then :gesture:`tap` on :guilabel:`Security` in the :guilabel:`System` section.

   .. image:: /img/collect-best-practices/settings.png
      :alt: Image showing Settings app.
      :class: device-screen-vertical

   .. image:: /img/collect-best-practices/security.png
      :alt: Image showing Security option in the System section.
      :class: device-screen-vertical

2. Make sure that the Unknown sources option is turned off. If this option is turned on, installation of apps from trusted as well as unknown sources will be allowed.

   .. image:: /img/collect-best-practices/unknown-source.png
      :alt: Image showing Unknown sources option turned off.
      :class: device-screen-vertical

.. _android-update:

Make sure you keep Android up-to-date
---------------------------------------

Many Android phone makers will now offer monthly security patches to ensure that any known vulnerabilities will be patched. Install these patches every month. It's one of the best ways to ensure that you won't be attacked by hackers and malware.

1. To periodically check for software updates, go to Settings app.

   .. image:: /img/collect-best-practices/settings.png
      :alt: Image showing Settings app.
      :class: device-screen-vertical

2. Then :gesture:`tap` on :guilabel:`About device` under the :guilabel:`System` section.
   
   .. image:: /img/collect-best-practices/about-device.png
      :alt: Image showing About device option in the System section.
      :class: device-screen-vertical   

   .. image:: /img/collect-best-practices/update-info.png
      :alt: Image showing update information.
      :class: device-screen-vertical


FAQ
==============

.. _what-is-odk:

What is ODK?
~~~~~~~~~~~~~~~~~~

Open Data Kit (ODK) is a free and open source set of tools which help organizations create mobile data collection solutions.

Our `blog <https://opendatakit.org/blog/>`_ and `deployments page <https://opendatakit.org/about/deployments/>`_ have good examples of what others have used ODK for. Our `research page <https://opendatakit.org/about/research/>`_ also has videos and slides that explain ODK.

.. _how-use:

How do I use ODK?
~~~~~~~~~~~~~~~~~~~~

Please read the :doc:`Getting Started Guide <getting-started>` section of our documentation to understand the initial instructions.

Please read through the documentation on our `implementer instructions <https://opendatakit.org/use/>`_ and on the `developer wiki <https://github.com/opendatakit/opendatakit/wiki>`_.

If that doesn't help, search the `ODK forum <https://forum.opendatakit.org/>`_ to see if the issue has been answered.

If you don't find an answer after searching, then post your question to the appropriate category.

.. _what-kinds-question:

What kinds of questions do you answer on the mailing list?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our team only answers questions about the `supported tools <https://opendatakit.org/about/tools/>`_. We generally do not answer form design questions, and instead, refer you to the `form design <https://opendatakit.org/help/form-design/>`_ guide.
You are more than welcome to post any message -- someone else in the community is likely to help.

.. _work-not-expected:

An ODK tool isn't working the way I expected. What do I do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure you are running the latest versions of ODK software. You can find them on our `downloads <https://opendatakit.org/downloads/>`_ page.

Search the `issue tracker <https://github.com/opendatakit/opendatakit/issues>`_ to see if the problem you are having has been reported. If you can't find it, report it there.

Please be precise about the tool you are using, the version of the software, and include all the steps you did so we can reproduce the same problem. If you can get a stack trace, please attach it. If the problem is with a form, please attach it as well. If you are new to filing bug reports, read How to Report Bugs Effectively.

If your issue is urgent, we recommend you `hire help <https://opendatakit.org/help/help-for-hire/>`_ from one of the ODK implementations companies.

.. _how-do-get-stack-trace:

How do I get a stack trace or log after an Android "Force Close"?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See `Collect Troubleshooting <https://github.com/opendatakit/opendatakit/wiki/Collect-Troubleshooting>`_. Capturing an error log is more difficult now that the newer Android operating systems restrict access to the system log stream.
Once you begin capturing a log and have reproduced the crash, please open an issue `here <https://github.com/opendatakit/opendatakit/issues>`_ and attach the captured log file.

.. _request-new-feature:

How do I request a new feature or enhancement?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Search the `issue tracker <https://github.com/opendatakit/opendatakit/issues>`_ to see if the feature you want has been suggested. If you find it, vote for it by adding yourself to receive notifications. If you don't find it, open a new issue (feature request) describing the scenario which you need the feature for.

.. _customize-ODK-solution:

How do I customize or implement an ODK solution?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The core team does not provide code or implementation support beyond what is described on our `implementer site <https://opendatakit.org/>`_ and on the developer site. If you need more support, `hire help <https://opendatakit.org/help/help-for-hire/>`_ from one of the ODK implementations companies.

.. _how-cite-odk:

How should I cite Open Data Kit in a publication?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

People often ask "How do I cite ODK?". Since Open Data Kit is an academic research project, please cite the academic research papers corresponding to the appropriate tool version.

If you are using ODK tools with a version code 1.x cite:
`Open Data Kit: Tools to Build Information Services for Developing Regions <https://opendatakit.org/wp-content/uploads/2010/10/ODK-Paper-ICTD-2010.pdf>`_
Carl Hartung, Yaw Anokwa, Waylon Brunette, Adam Lerer, Clint Tseng, Gaetano Borriello
In ICTD, 2010. http://dl.acm.org/citation.cfm?id=2369236


If you are using ODK tools with a version code 2.x cite:
`Open Data Kit 2.0: Expanding and Refining Information Services for Developing Regions <http://www.hotmobile.org/2013/papers/full/2.pdf>_`
Waylon Brunette, Mitchell Sundt, Nicola Dell, Rohit Chaudhri, Nathan Breit, Gaetano Borriello
In HotMobile, 2013. http://dl.acm.org/citation.cfm?id=2444790

Other publications to cite for individual ODK tools are available on the `Research <https://opendatakit.org/about/research/>`_ page.

.. _other-data-collection-to-consider:

Are there other data collection systems I should consider?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Of course! There are many other data collection systems that might work better for you.
Some of them use ODK in some way:

- `Ona <http://ona.io/>`_;
- `Survey CTO <http://www.surveycto.com/>`_;
- `KoBo Toolbox <http://kobotoolbox.org/>`_;
- `Commcare HQ <http://commcarehq.com/>`_;
- `DoForms <http://doforms.com/>`_;
- `DataWinners <http://datawinners.com/>`_;
- `ViewWorld <http://viewworld.dk/>`_;
- `PhiCollect <http://webfirst.com/phicollect>`_;

While other are ODK compatible:

- `JavaRosa <http://www.dimagi.com/javarosa/>`_;
- `OpenXData <http://www.openxdata.org/>`_;
- `RapidSMS <http://rapidsms.org/>`_;


If you want to find out more, `MobileActive <http://mobileactive.org/>`_ is a great place to learn more about data collection. `Mobile Data Collection Tools - Comparison Matrix <https://docs.google.com/spreadsheet/ccc?key=0Akj5_3vVWZ8tdGk4czI4eHcycGo2Y1NnWmhsUjdBTXc&hl=en_US>`_ and `Mobile-Phone-Based Data Collection Systems Comparison Table <https://docs.google.com/spreadsheet/ccc?key=0ArG7kkc9mE75dEdNNktocmVwT0hNbHVjTXl2ZU1VMXc&hl=en_US>`_, `Mobile and Web Technologies for Social and Economic Development report <https://docs.google.com/spreadsheet/ccc?key=0ArG7kkc9mE75dEdNNktocmVwT0hNbHVjTXl2ZU1VMXc&hl=en_US>`_, `Comparing Mobile Solutions for GIS Data Collection and Display <https://sites.google.com/site/dougbrowningportfolio/Resources/mobile-gis>`_, and `Nomad Mobile Collection Systems Decision Tool <http://humanitarian-nomad.org/?page_id=533>`_ are also good resources.

We also have `peer-reviewed research <https://opendatakit.org/about/research/>`_ and `user stories <https://opendatakit.org/blog>`_ that describe the situations where ODK is likely to be easier to use, less error-prone, more cost-effective and more timely when compared to other data collection systems.


.. _email-members-odk:

Should I email members of the ODK team directly?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Probably not. If you have a private question you cannot post to the list, please send it to contact@opendatakit.org.

.. _what-android-use:

What Android phone/tablet/device should I use?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Android ecosystem changes too rapidly to recommend one device. In general, we recommend you get devices that you can source in-country and run the latest Android OS (even though we support Android OS 1.6+ and higher).
ODK Collect will run on most Android form factors (including tablets and netbooks).

We recommend you spend a little more to get a higher quality device, instead of buying the cheapest phone. If you need a supplier, try:

- `Amazon <amazon.com>`_;
- `Newegg <newegg.com>`_;
- `Ebay <ebay.com>`_;
- `N1 Wireless <n1wireless.com>`_;


For a list of all Android devices, make a search in:

- `Wikipedia <wikipedia.org>`_;
- `GSMArena <gsmarena.com>`_;
- `Phone Scoop <phonescoop.com>`_;

.. _my-messages-delayed:

Why are my messages on the list being delayed?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are a first-time poster (or are not subscribed) to the lists, your emails are moderated. This process can take a few hours, so no need to send multiple messages.

.. _support-xforms:

Do you support XForms?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Not exactly. We support the OpenROSA 1.0 subset of XForms described at https://bitbucket.org/javarosa/javarosa/wiki/xform-jr-compat.

.. _have-api:

Do you have an API?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. We support the OpenROSA 1.0 API as described at https://bitbucket.org/javarosa/javarosa/wiki/OpenRosaAPI.

.. _change-collection-language:

How do I change the language that Collect is using?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The tools understand the text internationalization features of javarosa XForms and can restructure your input so that the question text is grouped into an <itext/> translation block for internationalization. 
Therefore, to support multiple languages you need to `specify the question text in the appropriate language using the tag <https://opendatakit.org/about/research/>`_. To change the language the XForm's questions are being rendered in, simply click the 'Menu' button on the Android while filling out a form and click the 'Change Language' button.

To change the language ODK Collect (version 1.2 and higher) is using to render the  user interface (e.g., button text, instructions) you need to change the phone's language settings. Collect determines its user interface language (not question language) based on the phone's overall settings. For example, in the phone settings, if you set the phone's locale to Espanol, Collect will render its navigation text in Spanish.

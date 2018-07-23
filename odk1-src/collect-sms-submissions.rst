.. spelling::

  Twilio
  fn
  ln

Submitting filled forms via SMS
===================================

.. admonition:: SMS is not reliable

  SMS does not provide a way for users to reliably know that messages have been delivered in a timely manner. It is not uncommon for messages to be dropped. When submitting forms via SMS, consider also submitting forms to a server when Internet connectivity becomes available. Alternately, set up the receiving end to send an SMS confirmation that the enumerator can verify.

Starting in ODK Collect v1.16.0, it is possible to submit filled forms via SMS. This can be useful when Internet connectivity is intermittent or unavailable. To use SMS submissions, you will need to decide where those submissions go. Some options are:

- A phone with a SIM that a person manually looks at periodically.
- A local number through a gateway service such as Twilio. It could, for example, `forward submissions to Google Sheets <https://www.twilio.com/blog/2018/05/receive-sms-messages-google-sheets-apps-script.html>`_.
- A server such as `RapidPro <https://community.rapidpro.io/>`_ configured to receive and interpret messages (can be backed by a SIM or gateway service).

.. _collect-sms-submission-format:

SMS submission format
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A form that asks for a user's first name, last name and age might result in submissions as the following SMS messages:
``my-form fn Sally ln David a 23``
``my-form fn Owen ln Krishnamurti a 22``

In this example, ``my-form`` is a prefix specified in the blank form definition to identify submissions from that form. ``fn``, ``ln`` and ``a`` are short tags that are specified in the blank form to identify first name, last name and age. Each tag is followed by the value for the question. 

Each value in the SMS message is separated by a delimiter. By default this is a single space as in the example above but this can also be configured in the blank form definition.

If the submission exceeds the accepted SMS length (usually 160 characters), the message will be sent as a multipart message. Most SMS applications and gateways support this natively but if you expect to receive long submissions, you should verify that you can receive them effectively.

Media submission is not currently supported over SMS. If a question of a media type (``image``, for example) includes a tag, the media's filename will be sent.

.. _form-sms-submission-configuration:

Configuring SMS submission in a form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To send submissions via SMS, a blank form must specify a ``short_tag`` for at least one question in the form. These tags are short versions of the question names that will be included in the SMS output as described in the :ref:`submission format <collect-sms-submission-format>` section. Only questions that specify a ``short_tag`` in the form definition will be included in SMS submissions. This can be used to quickly send time-sensitive indicators via SMS and to also collect more information for submission when Internet connectivity becomes available. As long as at least one tag is present in the form definition, submissions can be made via SMS.

.. csv-table:: survey
  :header: type, name, short_tag, label 

  text, first_name, fn, What is your first name?
  text, last_name, ln, What is your last name?
  text, favorite_colors, , What are your top 3 favorite colors?
  int, age, a, What is your age?

Optionally, a ``prefix`` can be specified for the form to identify submissions from that form. The prefix value is included once at the beginning of each SMS message. 

.. csv-table:: settings
  :header: prefix

  my-form

Additionally, an optional ``delimiter`` can be specified. This value will be included between each prefix, tag and form value. By default, the delimiter is a single space. If you allow spaces in the form values and expect to process your SMS messages by splitting on delimiters, you should set a delimiter other than space. For example, you could use ``+`` for the following result:

``my-form|fn|Sally Sue|ln|David|a|23``

.. csv-table:: settings
  :header: prefix, delimiter
  
  my-form, |

  If the delimiter value is used in a form answer, a '\' will be added before it. For example:

``my-form fn Sally\ Sue ln David 23``

.. _collect-sms-submission-configuration:

Configuring SMS submission in Collect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SMS submission can be configured for any kind of server. The server URL is used for getting blank forms or can be left blank if forms will be :ref:`manually transfered to your device <loading-forms-directly>`.

From the Server settings, change :guilabel:`Send submissions via` to :guilabel:`SMS`. You will then be able to set a destination phone number.

Now, when enumerators go to the :guilabel:`Fill Blank Form` screen, the forms they select will be sent via SMS.


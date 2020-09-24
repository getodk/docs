.. _central-troubleshooting:

Troubleshooting Central 
=========================

.. _email-failures:

Users aren't receiving Central emails
--------------------------------------

Central uses email as a way to verify user identity when setting or changing passwords. This is security best practice and helps ensure that only the intended user has access to their Central account.

Email sounds like a simple technology but in practice there are many things that can cause message delivery issues. By default, Central is installed with a mail server which can be used without configuration. However, it will not work in every environment. For example:

* Many cloud providers such as Amazon restrict the usage of simple mail servers such as Central's as a spam-prevention strategy
* You can be assigned an IP address that was previously used for sending spam and is therefore blocked by many mail recipients
* Your domain may not be recognized by mail recipients and therefore messages from it may be discarded or marked as spam

To address delivery issues, consider using a dedicated email service such as `Mailgun <https://www.mailgun.com/smtp/>`_. Because Central doesn't send very many emails, using such a service will generally be a cost-effective way of ensuring email delivery. Once you have an account set up, you will need to :ref:`configure Central to use it <central-install-digital-ocean-custom-mail>`.

If you want to directly send emails from your Central installation, the free `mail-tester <https://www.mail-tester.com/>`_ service can help you identify what barriers to email delivery you might have. Create a Central account with the email address that it provides, retrieve your results, and then delete the user. Typically, the first thing you will need to do is :ref:`configure DKIM <central-install-digital-ocean-dkim>` which will provide email recipients confidence that emails were actually sent by your Central server rather than by a spammer pretending to be your server.
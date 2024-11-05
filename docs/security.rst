Security
========

.. warning::

    This document assumes you are using `ODK Cloud <https://getodk.org/#pricing>`_ or an up-to-date :doc:`ODK Central <central-intro>` server. These security considerations do not apply to any other ODK-compatible systems.

Whether you are monitoring elections, documenting crimes, or tracking vaccines, ODK offers industry-leading security to protect the sensitive data you collect. Some of our security features are automatic (e.g., vulnerability scanning), while others (e.g., end-to-end encryption) are configurable so you can strike the balance you need.

When it comes to security, it's important to verify claims. ODK's code is 100% open-source, so you can freely audit that what we say is true. And if you aren't a security expert, we offer easy-to-understand :ref:`hosting considerations <hosting-considerations>` and :ref:`security audit reports <security-audits>` to guide your decision-making.

Threat model
------------

Since ODK's inception in 2008, we have not received any reports of unauthorized access into any servers or devices running ODK software. We also have never had any security breaches of services we maintain (e.g., ODK Cloud).

The security-related issues we get occasional reports of are:

- data collectors attempting to artificially reduce their workload or increase their completion rate by fabricating data, changing settings or sharing credentials
- data leaks from users doing things like downloading data and leaving a copy on a public computer or uploading it to a public service
- users leaving credentials or screenshots containing credentials in public places
- minor deviations from best practices on ODK web properties (e.g., misconfigured DMARC)
- issues from automated scans that don't consider purposeful choices (e.g., session timeouts)

The latter issue requires further discussion. ODK is designed to be usable by users with limited technical capacity and to be flexible to respond to a broad range of needs. These needs can be in tension with security best practices and we try to be deliberate in striking a balance.

For example, our mobile app supports HTTP connections to allow for offline servers (e.g., on a Raspberry Pi). The app also supports Android versions down to 5.1 (from 2014). We believe that these do not present significant risk for our typical users and that users in need of greater security can choose to use HTTPS and modern Android devices.

Because security is often about trade-offs, we work to be transparent about the specific trade-offs we've made so you can evaluate if ODK is a good fit for your project.

Data on mobile (Collect)
~~~~~~~~~~~~~~~~~~~~~~~~
:doc:`ODK Collect <collect-intro>` is used by data collectors to fill out forms designed by project managers. Data collectors are sometimes lightly trained and not always trusted.

Devices typically hold only the data that a specific data collector has collected but may also contain data attachments with sensitive information. This data is stored in clear text in shared storage. In recent versions of Android, on-device access is no longer possible, but some users use `adb <https://developer.android.com/tools/adb/>`_ to connect their computers to their devices to access data for troubleshooting.

The primary threats we consider:

- A malicious actor pulling all data off the device. End-users are responsible for having device biometrics/passcode and locking the screen to mitigate this risk.
- Data collectors sharing their credentials with others, reducing the reliability of collected data. At the same time, creating “group” accounts that are shared between users can be valuable, especially in large-scale contexts. We mitigate this by using a URL-based token for auth rather than a password that can be easily shared orally.
- Data collectors bypassing settings or app functionality to create fake or modified data. There is an admin password that can be set to disable access to many app settings but this depends on project managers making use of it. Data is currently stored in shared storage meaning that data collectors could directly modify submission data.
- Data collectors getting access to full datasets on the server. To mitigate this, we use a completely different and isolated account type for data collectors.

Data on server (Central)
~~~~~~~~~~~~~~~~~~~~~~~~
:doc:`ODK Central <central-intro>` is used by project managers to manages forms, submissions, users and more. Servers can contain large datasets including personally-identifiable information (PII) like GPS locations, photos, phone numbers, and more.

The primary threats we consider:

- Privilege elevation attempts from project viewers or managers who are given limited access. We believe users given access to a limited number or projects or given read-only access are the most likely to be aware of valuable data on a given server and have a desire to access it.
- Opportunistic attempts to infiltrate with the goal of seeing what valuable data might be available. We believe that Central servers are of interest to actors looking to find datasets to sell or to get ransoms from. Central servers may be specifically targeted because the code is open source and can be explored for vulnerabilities.

Hosting considerations
----------------------
.. _hosting-considerations:

There are two ways to get access to an ODK install. You can pay for official managed hosting on `ODK Cloud <https://getodk.org#pricing>`_, or if you are technical, you can self-host the ODK Central server for free on your own infrastructure.

The software is the same either way you choose, but there are important security trade-offs to consider. Below is a security checklist of the various considerations drawn from the OWASP Top 10, NIST Cybersecurity framework, ISO/IEC 27001 guidelines, and more.

.. csv-table::
  :header: Area,ODK Cloud,Self hosting,Notes
  :widths: 20,5,5,70

  Access Control and Firewall,✅,❓,"ODK Cloud runs on hardened infrastructure with isolated CPU, RAM, network, and storage for each customer. ODK Cloud only allows secure HTTPS connections. External SSH or database access are not possible."
  Audit Logging,✅,✅,The ODK server :doc:`logs every action <central-server-audits>`. The ODK mobile app can :doc:`log and geotag actions <form-audit-log>` taken during a form filling session. ODK Cloud adds monitored logging.
  Automated Testing,✅,✅,All ODK code has automated tests.
  Backups & Recovery Plans,✅,❓,ODK Cloud data is continuously backed up and can be restored to a specific moment in time. RPO/RTO guarantees are available.
  Buffer Overflows,✅,✅,All ODK code is written in memory-safe languages. Dependencies are checked for overflow vulnerabilities.
  Code & Container Scanning,✅,✅,All ODK code is scanned for vulnerabilities by GitHub. All containers used in ODK are scanned by Snyk.
  Code Review,✅,✅,All ODK code goes through public code review.
  Cross-Site Request Forgery (CSRF),✅,✅,The ODK server has CSRF protection and has automated testing to confirm.
  Cross-Site scripting (XSS),✅,✅,ODK's developers are familiar with XSS best practices and consider it in code review.
  Database Security,✅,❓,ODK Cloud databases are encrypted at rest and isolated by customer. External database access is not possible.
  "Data Governance, Compliance, Privacy",✅,❓,"ODK Cloud is available in US or EU data centers. Data centers are GDPR compliant and ISO27K and SOC 2 certified. See `Terms of Service <https://getodk.org/tos>`_, `Privacy Policy <https://getodk.org/privacy>`_, and `Data Processing Agreement <https://getodk.org/dpa>`_."
  Denial of Service (DOS),✅,❓,ODK Cloud monitors for attacks and mitigations can be put in place quickly. Automated DDoS protection is available.
  Encryption,✅,✅,The ODK server requires encryption in transit (HTTPS). Additional :doc:`end-to-end encryption <central-encryption>` is available for low-trust environments. ODK Cloud adds encryption at rest.
  Insurance,✅,❓,ODK Cloud is covered by General Liability and Professional Liability policies. Each has $2M/occurrence coverage.
  Maintenance & Updates,✅,❓,ODK Cloud infrastructure automatically updates outdated or vulnerable software.
  Manual Testing,✅,✅,ODK's QA process includes `manual testing <https://forum.getodk.org/t/how-the-qa-team-ensures-odk-is-reliable/49960>`_ both of new features and the full system before releases. Users also contribute manual testing of `betas <https://forum.getodk.org/c/releases/pre-releases/19>`_.
  Password Storage,✅,✅,The ODK server uses BCrypt for password-hashing with a cost factor of 12.
  Penetration Testing,✅,❓,"ODK Cloud has independent :ref:`security audits and penetration tests <security-audits>` that include testing OWASP Top 10 (e.g., broken access control, cryptographic failures, injection attacks, insecure design, misconfiguration)."
  Physical Security,✅,❓,"ODK Cloud data centers have 24-hour security, video surveillance, limited network access, etc."
  Roles & Permissions,✅,✅,"Web Users (e.g., project managers) can only be created with an email address and password resets are only possible through that email. App Users (e.g., data collectors) authenticate with a QR code and are fully isolated from all management functions. See :doc:`Central Users <central-users>` for more."
  Single Sign-On (SSO) & Multi-Factor Auth (MFA),✅,✅,The ODK server offers :ref:`SSO via the OIDC protocol <central-install-digital-ocean-sso>`. MFA can be enabled at the identity provider.
  SQL Injection (SQLi),✅,✅,The ODK server uses Slonik which is designed to prevent vulnerable queries. ODK's developers are familiar with SQLi best practices and consider it in code review.
  SSL Certificates (HTTPS),✅,✅,The ODK server requires HTTPS and uses Let's Encrypt certs with TLS 1.3 and an `A+ rating from SSL Labs <https://www.ssllabs.com/ssltest/analyze.html?d=production.getodk.cloud>`_.
  Uptime Management,✅,❓,"ODK Cloud has had `99.999% uptime <https://status.getodk.org/>`_ across any given 12 month period."

Security audits
---------------
.. _security-audits:

In addition to internal security reviews of every change to ODK, we commission independent white-box penetration tests, source code audits, and reviews of our architecture and processes. After mitigating issues, we publish the results.

.. Below is our latest independent report. - Pen Test and Security Review (`Cure53 <https://cure53.de>`_ , July 2024)

Vulnerability disclosure
------------------------
We welcome any responsible disclosure of vulnerabilities that helps us ensure the security and privacy of our users. 

Please do not report vulnerabilities on the community forum or on GitHub. Instead, report them to security@getodk.org. We will respond in 3 business days, and after fixing the vulnerability, will responsibly disclose it. 

See our `Vulnerability Disclosure Policy <https://getodk.org/vdp>`_ for more on scope, reporting, and disclosure.

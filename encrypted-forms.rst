*****************************
Encrypted Forms
*****************************

Overview 
====================
Encrypted forms provide a mechanism to keep your data private even when using http: for communications (e.g., when you do not have an SSL certificate or https: is not available). Encrypted forms may also enable Google App Engine deployments (and deployments using other web database services, e.g., AWS) to comply with data privacy laws, eliminating the necessity for setting up your own servers to meet those requirements.

Requirements
====================
- ODK Collect 1.2 Release Candidate 1 (RC1) or higher
- ODK Aggregate 1.0.4 Production or higher
- ODK Briefcase 1.0 Production or higher
``</submission>``

Configuration 
====================
*emphasis*

Windows
~~~~~~~~~~~~~~~

macOS
~~~~~~~~~~~~~~~

Uploading Finalized Forms
===========================

.. code-block:: rst

   <h:html xmlns="http://www.w3.org/2002/xforms"
        xmlns:h="http://www.w3.org/1999/xhtml"
	xmlns:orx="http://openrosa.org/xforms/">
 <h:head>
  <h:title>Sample Form</h:title>
  <model>
    <itext>
      <translation lang="English" default="">
        <text id="ask_name">
          <value form="long">Please enter your name:</value>
          <value form="short">Respondent's name</value>
        </text>
      </translation>
    </itext>
    <instance>
      <sample id="sample-v1.0">
        <orx:meta>
           <orx:instanceID/>
        </orx:meta>
        <name/>
      </sample>
    </instance>
    <submission method="form-data-post"
                action="https://my-opendatakit.appspot.com/submission"
                base64RsaPublicKey="MIIBIjANB...JCwIDAQAB" />
    <bind nodeset="/sample/meta/instanceID" type="string" readonly="true()"
          calculate="concat('uuid:', uuid())"/>
    <bind nodeset="/sample/name" type="string" />
  </model>
 </h:head>
 <h:body>
    <input ref="name">
       <label ref="jr:itext('ask_name')"/>
    </input>
 </h:body>
 </h:html>

Creating RSA Key pair
===========================
RSA public-private key pairs are generated using the OpenSSL software package. This is pre-installed on OSX and Linux, but needs to be downloaded and installed on Windows.

1. Install OpenSSL (Windows only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



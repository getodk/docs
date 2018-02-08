ODK JavaRosa
############

.. This introduction was copied from the readme, but not confirmed to be correct

JavaRosa is a Java library for rendering forms that are compliant
with `ODK XForms spec <http://opendatakit.github.io/xforms-spec>`_. It is the heart of many of
the ODK tools. ODK JavaRosa is a fork of `JavaRosa <https://bitbucket.org/javarosa/javarosa/wiki/Home>`_ 1.0
that has been modified to NOT run on J2ME devices. The key differences are:

* Regularly updated to ensure spec compliance
* KoBo additional instance defn. and filter paths
* Remember all bind attributes and any additional attributes on ``<input>``, ``<select>``, ``<group>``, etc. statements
* Numerous enhancements and contributions from SurveyCTO and others
* J2ME sub-projects removed

Architecture
************

Integration Points
******************

This section describes how the different parts of ODK use JavaRosa.

Aggregate
=========

Briefcase
=========

Collect
=======

Validate
========

Two source files in Validate use JavaRosa.

.. We probably won’t include an exhaustive cross reference for all the clients here

FormValidator.java
------------------
::

    core/model/Constants.java
    core/model/FormDef.java
    core/model/FormIndex.java
    core/model/GroupDef.java
    core/model/IFormElement.java
    core/model/SelectChoice.java
    core/model/condition/EvaluationContext.java
    core/model/condition/IFunctionHandler.java
    core/model/data/IAnswerData.java
    core/model/instance/InstanceInitializationFactory.java
    core/model/instance/InvalidReferenceException.java
    core/model/instance/TreeElement.java
    core/model/instance/TreeReference.java
    core/model/utils/IPreloadHandler.java
    core/model/utils/QuestionPreloader.java
    core/services/PropertyManager.java
    core/services/PrototypeManager.java
    form/api/FormEntryCaption.java
    form/api/FormEntryController.java
    form/api/FormEntryModel.java
    form/api/FormEntryPrompt.java
    model/xform/XFormsModule.java
    xform/parse/XFormParseException.java
    xform/util/XFormUtils.java

StubPropertyManager.java
------------------------
::

    core/services/properties/IPropertyRules.java
    core/services/IPropertyManager.java


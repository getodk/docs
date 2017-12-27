Evaluation Logic Architecture
##########################################

JavaRosa uses a Direct Acyclic Graph (DAG) to manage triggerable XPath expressions and their dependencies.
Those expressions can be put in the following attributes of the `bind <https://opendatakit.github.io/xforms-spec/#bindings>`_ section 
in a form:

* ``calculate``
* ``relevant``
* ``required``
* ``readonly``

The ``constraint`` attribute also takes an XPath expression but it is not managed by DAG.
It is represented by ``Constraint`` class and evaluated before an answer is committed into the data model
in the ``FormEntryController.answerQuestion(FormIndex index, IAnswerData data, boolean midSurvey)`` method.

Classes
-------

- ``Triggerable`` --- An abstract class represents such expression, its context and targets which should be updated by this expression. It has two implementations:

    * ``Condition`` --- Represents an expression for ``relevant``, ``required`` and ``readonly`` attributes which always evaluates to ``true`` or ``false``.
    * ``Recalculate``--- Represents an expression for the ``calculate`` attribute and can evaluate to any supported data type.
- ``QuickTriggerable`` --- A ``Triggerable`` class wrapper which provides a shallow comparison of ``Triggerable`` implementations. Once the DAG structure is built, no new ``Triggerable`` instances are created and therefore there is no need for the deep comparison. For the sake of readability, this document will always reference to ``Triggerable`` class even if ``QuickTriggerable`` is actually used in the code. 
- ``IDag`` --- An abstract class represents an interface for the DAG management and triggerable evaluation logic.
- ``LatestDagBase`` --- An abstract implementation of ``IDag`` class which serves as a base for all actual implementation of ``IDag``
- ``Safe2014DagImpl`` --- The only supported ``IDag`` implementation.
- ``FormDef`` -- A form representation along with the data model. This class communicates with ``IDag``.

High level description
-----------------------

Each triggerable expression is evaluated at form load and save. Additionally, if the XPath expression references other node(s),
it is evaluated if any of the referenced nodes are updated. Moreover, it may happen that a referenced node also has a triggerable
expression which references other nodes etc. 
So triggerables may depend on each other. 

Lets check an example:
Assume there are nodes ``nodeA``, ``nodeB`` and ``nodeC`` and:

* ``nodeA`` has a ``calculate`` expression ``tA`` which references the ``nodeB`` value
* ``nodeB`` has a ``calculate`` expression ``tB`` which references the ``nodeC`` value
* ``nodeC`` has no triggerable expressions

So the dependency is ``tC`` > ``tB`` > ``tA``.
When a form is loaded or saved, those triggerables should be evaluated in the following order: ``tC``, ``tB``, ``tA``.
When a value of ``nodeC`` is changed then ``tB`` and ``tA`` must be evaluated. In this order.

Lets change the above so the ``nodeC`` node has a ``relevant`` expression which returns ``true`` if ``nodeA`` has a certain value.
This gives the following dependency ``tA`` > ``tC`` > ``tB`` > ``tA``. Since ``tA`` depends on ``tB`` and ``tB`` depends on ``tC``
it results in an infinite loop. A paradox which cannot be handled.

Direct Acyclic Graph ensures that triggerables are in the topological order. If there are cycles then DAG cannot be constructed
and an exception is thrown.

``Triggerable``
----------------

This class stores the following information:

* The expression to be evaluated.
* A list of target nodes which should be updated with the expression evaluation result.
* The context reference.
* A list of ``Triggerable`` instances - named ``immediateCascades`` - that depend on ``this`` evaluation result and should be evaluated after ``this`` is evaluated.

Note: terms 'triggerable', 'calculation' or 'condition' mean the same - an instance of ``Triggerable`` class - and are used interchangeably in this document.

``FormDef`` and ``IDag`` communication
---------------------------------------

The ``FormDef`` class talks to ``IDag`` through the following methods:

.. code-block:: java

    // Initialization methods:
    addTriggerable(Triggerable t);
    finalizeTriggerables(FormInstance mainInstance, EvaluationContext evalContext);

    // Triggering evaluation methods

    initializeTriggerables(FormInstance mainInstance, EvaluationContext evalContext, TreeReference rootRef, boolean midSurvey);
    deleteRepeatGroup(FormInstance mainInstance, EvaluationContext evalContext, TreeReference ref, TreeElement parentElement, TreeElement deletedElement);
    createRepeatGroup(FormInstance mainInstance, EvaluationContext evalContext, TreeReference ref, TreeElement parentElement, TreeElement createdElement);
    triggerTriggerables(FormInstance mainInstance, EvaluationContext evalContext, TreeReference ref, boolean midSurvey);
    copyItemsetAnswer(FormInstance mainInstance, EvaluationContext evalContext, TreeReference copyRef, TreeElement copyToElement, boolean midSurvey);

    // Validation

    reportDependencyCycles (XFormParserReporter reporter);
    shouldTrustPreviouslyCommittedAnswer();
    validate(FormEntryController formEntryControllerToBeValidated, boolean markCompleted);

    // Serialization methods

    getConditions();
    getRecalculates();

    // Misc

    getEvalBehavior();
    getTriggerableForRepeatGroup(TreeReference ref);
    printTriggerables(String path);

    // Seems to be used only by a FormDef method which isn't used in JavaRosa

    getConditionExpressionForTrueAction(FormInstance mainInstance, TreeElement instanceNode, int action);

Initialization
-----------------

Collecting
~~~~~~~~~~

Triggerables are constructed during the `bind <https://opendatakit.github.io/xforms-spec/#bindings>`_ parsing.
The ``StandardBindAttributesProcessor`` class constructs appropriate ``Triggerable`` implementations based on the bind 
attributes and adds them to the DAG. The bind processor class calls ``FormDef.addTriggerable(Triggerable t)`` 
which calls ``IDag.addTriggerable(Triggerable t)``. 
The DAG code is intentionally hidden from the parsing module and communication is made through the ``FormDef`` class.

Two or more nodes can have the same triggerable expression for a given bind attribute. For example:

.. code-block:: xml

    <instance>
        <data id="dataid">
            <nodeA/>
            <nodeB/>
            <nodeC/>
        </data>
    </instance>
    <bind nodeset="/data/nodeA" calculate="pow(/data/nodeC, 2)" type="int"/>
    <bind nodeset="/data/nodeB" calculate="pow(/data/nodeC, 2)" type="int" />
    <bind nodeset="/data/nodeC" type="int"/>

In the above snippet, both ``nodeA`` and ``nodeB`` have the same ``calculation`` expression which is evaluated
when ``nodeC`` is updated. The ``nodeC`` is the *trigger* of ``nodeA`` and ``nodeB`` calculations.

To avoid storing two separate but equal ``Triggerable`` instances, the ``IDag.addTriggerable(Triggerable t)``
method first checks if a same triggerable has been already added. 
Two ``Triggerable`` instances are considered equal if:

* Both have the same implementation type - ``Recalculate`` never equals ``Condition``.
* Both have the same expressions to be evaluated.
* Both have the same triggers. This is implied by the second bullet as triggers are the nodes referenced in the expressions.

If such triggerable already exists, ``IDag`` does not add a new instance but updates the existing ``Triggerable`` one's context so it points to the 
highest common root. For the above example, the highest common root for ``nodeA`` and ``nodeB`` calculations is ``/data``.
The passed instance ``t`` is ignored and a previously added ``Triggerable`` one is returned and should be used for the further processing.
The context is used later when constructing a DAG structure.

If such triggerable does not exist, it is added to the ``unorderedTriggerables`` list and the ``triggerIndex`` map.
The passed triggerable ``t`` instance is returned.
The list is later used to construct the topologically sorted list ``triggerablesDAG``.
The ``triggerIndex`` maps the triggers to the triggerables.

Each ``Triggerable`` instance comes with a list of targets which should be updated with the evaluation result.
In the above example, ``pow(/data/nodeC, 2)`` calculation have two targets: ``nodeA`` and ``nodeB``.
When a ``Triggerable`` instance is constructed, the targets list cannot be populated because each ``bind`` node
is parsed separately and other targets - if any - for the same triggerable are unknown. Moreover,
the newly constructed ``Triggerable`` may be ignored if another instance that represents the same triggerable
have been already added to the DAG.

.. Actually, the above is not entirely true. I think it can be refactored so the targets are populated during 
.. the bind processing. But a particular attention must be paid to call ``IDag.addTriggerable(Triggerable t)`` before
.. ``Triggerable.addTarget(TreeReference target)`` because  ``IDag.addTriggerable(Triggerable t)` may return a previously added
.. instance and there fore ``t`` is ignored.

The ``targets`` list population is postponed and takes place during the form instance parsing, 
in the ``FormInstanceParser.applyInstanceProperties(FormInstance instance)`` method.

Finalization and constructing the DAG
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once all ``bind`` nodes are parsed and all ``Triggerable`` objects collected, the ``IDag`` can be finalized and
the actual DAG structure can be constructed. The ``finalizeTriggerables(FormInstance mainInstance, EvaluationContext evalContext)``
method is responsible for the finalization. Once it completes, ``triggerablesDAG`` and ``conditionRepeatTargetIndex`` becomes
populated and valid. 

* ``triggerablesDAG`` stands for the topologically ordered list of ``Triggerable`` instances. All evaluation takes place according to the order in this list.
* ``conditionRepeatTargetIndex`` maps a repeat group reference (``TreeReference``) to its ``Condition`` that determines the relevance.  


Triggering
----------

Evaluation of triggerables is triggered when:

* A form is loaded
* A value of a node changes (an answer is committed)
* A repeat group is added
* A repeat group is deleted
* A form instance is finalized

Shared (private/protected) code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Part of the triggering functionality is extracted into a couple of private/protected methods.

.. code-block:: java

    protected Set<QuickTriggerable> doEvaluateTriggerables(
        FormInstance mainInstance, 
        EvaluationContext evalContext, 
        Set<QuickTriggerable> tv, 
        TreeReference anchorRef, 
        Set<QuickTriggerable> alreadyEvaluated) 

This method is responsible for evaluation of given set of ``Triggerable`` instances with the respect to the order in ``triggerablesDAG``.
Triggerables present in the ``alreadyEvaluated`` set are ignored. This argument is useful when triggering calculations
for a group node creation or deletion and will be described later.

.. code-block:: java

    private Set<QuickTriggerable> evaluateTriggerables(
        FormInstance mainInstance, EvaluationContext evalContext,
        Set<QuickTriggerable> tv, TreeReference anchorRef,
        Set<QuickTriggerable> alreadyEvaluated)

This method is called before the above one (``doEvaluateTriggerables``) and is responsible for collecting
calculations that depend on the set of directly triggered conditions (``tv``). 
It takes the set of directly triggered calculations (``tv``) and grabs their dependent calculations
(the ``immediateCascades`` list in the ``Triggerable`` class), then iterates over the dependent calculations and grabs
their dependent conditions etc. till all triggerables to be evaluated are identified. 

A form is loaded
~~~~~~~~~~~~~~~~

After the form is loaded, 
the ``initializeTriggerables(FormInstance mainInstance, EvaluationContext evalContext, TreeReference rootRef, boolean midSurvey)`` 
method is called. It just iterates over the ``triggerablesDAG`` collection and grabs each triggerable which targets
at least one node that is a child of the ``rootRef`` parameter and puts it in the ``applicable`` collection. 
Next, the collection is passed down to the private/protected methods that take care of gathering dependent triggerables
and evaluating them in the correct order. 

When this method is called after the form is loaded,
the root reference is passed and therefore all triggerables in the form should be evaluated. 

A value of a node changes
~~~~~~~~~~~~~~~~~~~~~~~~~

When an answer is committed,
the ``triggerTriggerables(FormInstance mainInstance, EvaluationContext evalContext, TreeReference ref, boolean midSurvey)``
method is called. It finds triggerables that are triggered by the ``ref`` in the ``triggerIndex`` map. 
Those triggerables are passed down to the private/protected methods that take care of gathering dependent triggerables
and evaluating them in the correct order. 

There is a special scenario for 'complex questions'. A complex question is a question that references xml data from a secondary instance.
*To be added later.*

A repeat group is added
~~~~~~~~~~~~~~~~~~~~~~~~

This scenario is a bit more complex and it mixes the two above approaches when the following method is called:

.. code-block:: java

    createRepeatGroup(
        FormInstance mainInstance,
        EvaluationContext evalContext, 
        TreeReference createRef,
        TreeElement parentElement, 
        TreeElement createdElement)

First, calculations that depend on the repeat group reference are triggered.
Next, all calculations defined for the children nodes of the newly created repeat group are evaluated.
Last, the code iterates over the children of the repeat group and for each child triggers its dependent calculations.
For the last phase, conditions evaluated during the first and second steps are ignored (passed as ``alreadyEvaluated`` set).

.. Should an example be here?

A repeat group is deleted
~~~~~~~~~~~~~~~~~~~~~~~~~

When a repeat group is deleted then:

* all of the following repeat groups position changes (is shifted to the left by 1),
* values of the children of the deleted repeat group change (they are gone).

The code evaluates triggerables that depend on the deleted repeat group children and
iterates over the following repeat groups and triggers calculations that depend on their references.

This scenario is handled by the following method:

.. code-block:: java

    deleteRepeatGroup(
        FormInstance mainInstance, 
        EvaluationContext evalContext, 
        TreeReference ref, 
        TreeElement parentElement, 
        TreeElement deletedElement);



A form instance is finalized
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a form is finalized, all triggerables for the relevant and visible nodes are re-evaluated. 
Visible means nodes that have a corresponding input definition in the form ``body``.
Validation takes place in the ``IDag.validate(FormEntryController formEntryControllerToBeValidated, boolean markCompleted)`` method
and uses the API class ``FormEntryController`` to navigate through all relevant questions and re-commit them in order
to trigger the validation. This implicitly triggers calculations dependent on the questions.

This approach is not perfect and there is an open JavaRosa `issue <https://github.com/opendatakit/javarosa/issues/232>`_ for refactoring this.
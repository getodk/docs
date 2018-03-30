.. spelling::

  advanceOnReturn
  popHistoryOnExit
  validateInProgress


ODK Survey Controller Actions
==================================

.. _survey-controller-actions:

The 10 possible controller actions for Survey's controller are:

  * **assign** -- a synchronous assignment statement storing a calculation in a field.
  * **begin_screen** -- push this operation on the navigation history stack and render its screen (this object is both an operation and an instance of a `screen`)
  * **goto_label** -- jump to an operation identified by the given label. This may be a conditional jump. i.e., the 'condition' property, if present, will be a boolean predicate. If it evaluates to false, then skip to the next question; if it evaluates to true or is not present, then execute the 'goto'
  * **do_section** -- push this operation onto the section history stack and mark it as 'advanceOnReturn' then start processing operation 0 in the specified section.
  * **exit_section** -- pop the section history stack (removing the entire navigation history for this section) and if the last operation from the calling section is marked 'advanceOnReturn' then advance to the next operation otherwise execute the operation (unused). This undoes *do_section*.
  * **back_in_history** -- pop the navigation history stack (unwind to the previous rendered screen) or, if this would exit the current section, display the contents screen for that section, or, if there is no previous screen, navigate to the screen specified when the form was initially loaded.
  * **advance** -- either execute **back_in_history** if the current operation is marked 'popHistoryOnExit' or advance to the next operation.
  * **validate** -- if this operation (*validate*) is not yet on the section history stack, push the operation and mark it with 'validateInProgress' (this enables the controller to return to the validate operation and resume the validation check after the user corrects the first invalid field value). Then traverse all fields with the indicated `sweep_name` and verify their compliance. Upon finding a field that fails validation, retrieve the `begin_screen` operation that contains that prompt, set that operation as the new current operation and mark it as 'popHistoryOnExit'. If all fields validate successfully, pop the section history stack (removing the 'validateInProgress' entry) and execute **advance**.
  * **resume** -- pop the history stack (unwind to the previous rendered screen) and render that screen. If popping the history stack would have exited the section, exit the section and advance to the next screen after the 'do_section' command.
  * **save_and_terminate** -- save all changes and close the WebKit.


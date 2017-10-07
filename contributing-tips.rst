Tips for Making Good Contributions
====================================

.. _small-pr:

Smallest meaningful PR
------------------------

A PR should normally address one issue. This makes it easier to review, easier to deploy, and easier to roll back in case of a problem. Additionally, the smaller the PR, the less likely it is to create a merge issue.

The exception is when several issues are closely related or can reasonably be worked on together.  In this case, it should be clear by looking at the conversation on the Github issues that the items are related and will be worked on together. Your PR message should also make it clear which issues are being worked on, and whether the PR closes the issues or not. Mention the PR by number:

  addresses #123

  closes #123


.. _descriptive-pr-names:

Descriptive PR names
----------------------

A PR title should answer the question, "What does this Pull Request do?"

Good PR titles:

- adds a video directive
- makes navigation buttons responsive
- swaps placement of nav buttons and file an issue note

Bad PR titles:

- fix issue
- fix #123
- collect

.. _small-commits:

Small, atomic commits
-----------------------

When working locally, commit often. Don't wait until you have 100 lines of changes across multiple files.

- If you need to copy or move a large section or file, commit that change before also editing it.
- If you have to create a new template file based on an existing template file, copy the file in one commit and then work on the changes. This makes it easier to know what you actually did.
- If writing a new doc, commits after each new section are a good idea.

Commit messages should answer the question, "What does this commit do?"

Small, well-named commits will help you keep track of your own work and make rollbacks and other changes easier to deal with.


.. _discuss-issues:

Discuss issues before working
--------------------------------

Take the time to clarify the needs and scope of an issue before committing to work on it. Especially for coding tasks, make sure you state your understanding and your plan before working.

If you have a question, ask. Don't guess.

.. note::

  Many new contributors don't ask questions because they are worried about appearing under informed. Please set this worry aside.

  **You will never be judged harshly for asking clarifying questions or for seeking more information.**

.. _claim-issues:

Claim issues
--------------

If you decide to work on an issue, let the community know you are working on it by *claiming* the issue.

  @opendatakit-bot claim

Once you've claimed an issue, other people won't work on it. So make sure you're actually going to work on it before claiming it.

Don't claim more than one or two open issues at a time.


.. _wip-pr:

Share work in progress
-------------------------

It can be helpful to share your in-progress work. To mark a PR as a work in progress, append **WIP:** to the beginning of the PR title. We will not merge **WIP** PRs, and we won't do a review on them unless you ask.

If you want a review, comment, opinion, or help on a **WIP** PR, please tag the relevant person in the PR comments.

If you finish the work and want the PR to be merged, you do not need to open a new one. Just edit the PR title.


.. _if-you-get-stuck:

If you get stuck while working
--------------------------------

- Ask for help in the issue comments. Maybe you can get back on track and complete the issue.

  - Asking questions is always better than guessing.

- Submit a **WIP** (work in progress) pull request.

  - If we can see what progress you have made, it is easier to offer help.
  - Even if you don't complete the task, perhaps someone else can pull in your in-progress work and build on it.
  - Sometimes your in-progress work is an improvement over not having it, and so we'll merge in something even if it isn't complete.

- If you really cannot move forward, it is okay to abandon an issue.

.. _abandon-issue:

It is okay to abandon an issue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes you simply cannot complete work you have said you were going to complete. This could happen because you don't have all the required skills or knowledge to complete the work, or because the issue cannot actually be completed as scoped, or because you don't have the time.

Please let the community know in the issue discussion.

  @opendatakit-bot unclaim

This way, everyone knows that someone else can take up the project (or that we need to rethink it).

If you did significant work on a project before abandoning it, consider filing a **WIP** (work in progress) PR, so that others can see what you did and potentially build off of it. (Be sure to mention the issue, so the work is easy to find later.)

.. _issue-takes-long-time:

If an issue takes a long time to complete
-------------------------------------------

For our purposes, a "long time" is a week or more, from when you first announce your intention to work on something until submitting a merge-ready PR.

An issue might take a long time because:

- it is complex and requires lots of hours
- you only have a short period of time each day to work on it
- you are new to the project and are having to learn as you go

The thing that matters is: **Are you actively working on the issue, and making progress, at least a little bit?**

If you are actively working on it, we do not want someone else to jump on and try to work on it at the same time. So please keep the community informed of your work by filing a **WIP** (work in progress) PR and committing to it as you work.

.. _issues-only:

Issues only
----------------

All PRs must be directly connected to open issues. PRs should not represent suggestions, good ideas, or independent initiative.

If you have a good idea, file an issue. If you are curious about whether something should be an issue, chat with one of the core team in the `#docs-code` channel on the `Slack <https://opendatakit.slack.com>`_.

Once you have filed an issue, wait for comment and approval before diving into the work. We do not want surprise PRs.

.. _use-odk:

Actually install and use Open Data Kit or other tools
----------------------------------------------------------

You cannot write effectively about tools you have not used. If you're going to write or edit documentation about any of the apps in the ODK ecosystem, you need to spend some time actually using it.

Before diving into writing documentation, follow the :doc:`getting-started` guide so that you are familiar with the core ODK tools.

This is also true of writing about Sphinx or any of our documentation build tools. Reading existing documentation is not enough to write about something.

.. _do-the-thing:

And actually do the thing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are writing about a specific process (installing an application, for example), you need to actually complete the process yourself. If possible, follow your own instructions *after* writing them to make sure they make sense.

.. _always-build-locally:

Always build locally
----------------------

Before submitting a PR, run the build locally to make sure you do not produce any errors or warnings. **We do not accept PRs that produce errors or warnings.**

It is best to run the build frequently as you work. You'll often catch simple mistakes that are harder to track down later.

.. _no-imposters:

You are not an imposter
--------------------------

`Imposter syndrome <https://en.wikipedia.org/wiki/Impostor_syndrome>`_ is the feeling that you are not good enough or accomplished enough to do the work you are doing.

We all feel this way sometimes, and that's okay. But it is important to realize that **you are not an imposter.**

You can contribute to this community, no matter your background or skills.

- If there is something you don't know how to do, you can ask.

  - If it is issue related, ask on the issue.
  - If it is more general, try the #docs-code channel in the `ODK Developer Slack <http://slack.opendatakit.org>`_.

- If you want to try something even though you aren't sure you can do it, go ahead and try.

Another worry you may have is that something will take you a long time when an "expert" might be able to do it quickly. You may feel, then, you aren't the "right person" for the job. But if you are the only one with the time or desire to work on something, **you are the right person to work on it.** 

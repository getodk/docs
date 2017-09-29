# ODK Docs

![Platform](https://img.shields.io/badge/platform-Sphinx-blue.svg) [![License](https://img.shields.io/badge/license-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/) [![Build status](https://circleci.com/gh/opendatakit/docs.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/opendatakit/docs/) [![Slack status](http://slack.opendatakit.org/badge.svg)](http://slack.opendatakit.org/)

This repo is the source for ODK documentation.

## Current Status — Live! (But still new)

Our new documentation website is live at https://docs.opendatakit.org

This is still a new project, and most of the useful documentation is still at the [old docs on the ODK website](https://opendatakit.org/).

## Building and viewing documentation locally
See the [contribution guide](http://docs.opendatakit.org/contributing) for detailed steps -- no prior experience needed!

Once your environment is set up:
```
sphinx-build -b dirhtml . build
cd build
python -m http.server 8000
```

## What's the plan?

 - Docs are being aggregated, rewritten, edited, and expanded into this repo.
 - The first things we've done are:
    - a __Getting Started__ guide
    - a __Contributors__ guide
 - This repo will be used as a single source for documentation for all ODK components.
    - There are good reasons for separating the docs into individual repos for each component. We may do this in the future. [Please see this ODK Forum thread to discuss whether to keep all the docs together or disaggregate them.](https://forum.opendatakit.org/t/docs-structure-discussion-one-or-many-repos/7080)

## How to contribute?

We are open for new issues and pull requests.

 - Please read the [Contributors Guide](http://docs.opendatakit.org/contributing) before working on the documentation.
 - [Engaging in the forum discussions on documentation.](https://forum.opendatakit.org/c/development/documentation)
 - [Filing GH Issues](https://github.com/opendatakit/docs/issues) for specific documentation artifacts that don't currently exist in any form.
 - [Watch](https://github.com/opendatakit/docs/subscription) and star this repo, to keep up with what we're doing.

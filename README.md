# ODK Docs

![Platform](https://img.shields.io/badge/platform-Sphinx-blue.svg) [![License](https://img.shields.io/badge/license-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/) [![Build status](https://circleci.com/gh/opendatakit/docs.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/opendatakit/docs/) [![Slack status](http://slack.opendatakit.org/badge.svg)](http://slack.opendatakit.org/)

This repo is the source for ODK documentation.

## Current Status — Live! (But still new)

Our documentation website is live at https://docs.opendatakit.org

If you can't find what you are looking for, try the [old docs on the ODK website](https://opendatakit.org/). Also, please [file an issue](https://github.com/opendatakit/docs/issues) so that we know to add the information you are looking for.

## Building and viewing documentation locally

> See the [Contributor Guide](http://docs.opendatakit.org/contributing) for detailed steps --- no prior experience needed!

Firstly, you need to clone this repo and make sure all the requirements are installed:
```bash
$ git clone https://github.com/opendatakit/docs.git
$ cd docs/
$ pip install -r requirements.txt
```
Once your environment is set up, build and run the doc site with:
```bash
$ make odk1
$ cd odk1-build
$ python -m http.server 8000
```

To perform all spell check and style checks before building, use `make odk1-check` instead or `make odk1`.

To build ODK 2 docs, replace `odk1` with `odk2`.

## How to contribute?

We are open for new issues and pull requests.

 - Please read the [Contributors Guide](http://docs.opendatakit.org/contributing) before working on the documentation.
 - Find issues to work on.
    - First time contributors are encouraged to complete a [line edit](https://github.com/opendatakit/docs/issues/96) as a way to get familiar with our contribution process.
	- Issues labelled [easy](https://github.com/opendatakit/docs/labels/easy) do not require much specific technical knowledge.
	- Issues labelled [contributor friendly](https://github.com/opendatakit/docs/labels/contributor%20friendly) are usually self-contained and don't require extensive knowledge of the ODK ecosystem as a whole.
	
You can also...

 - [Discuss the documentation from a user perspective in our forum](https://forum.opendatakit.org/c/development/documentation).
 - [Discuss the documentation from a contributor perspective in our developer Slack](slack.opendatakit.org). (Use the #docs-code channel.)
 - [File an issue](https://github.com/opendatakit/docs/issues) for any needed improvements.
 - [Watch](https://github.com/opendatakit/docs/subscription) and star this repo, to keep up with what we're doing.

## Troubleshooting

### **1. incorrect sphinx version**
#### Error message:
```bash
$ make odk1
...
Extension error:
Could not import extension sphinx_tabs.tabs (exception: No module named 'sphinx_tabs')
make: *** [odk1] Error 1
```
or:
```bash
$ make odk1
...
Configuration error:
There is a programable error in your configuration file:
...
from sphinx.util.compat import Directive
ImportError: cannot import name Directive
```

#### Reason & Fix:
It caused by an incorrect` sphinx` version, and you can fix this by reinstalling `sphinx` using `requirements.txt`.

# ODK Docs

![Platform](https://img.shields.io/badge/platform-Sphinx-blue.svg) [![License](https://img.shields.io/badge/license-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/) [![Build status](https://circleci.com/gh/opendatakit/docs.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/opendatakit/docs/) [![Slack status](http://slack.opendatakit.org/badge.svg)](http://slack.opendatakit.org/)

This repo is the source for ODK documentation.

## Current Status — Live! (But still new)

Our documentation website is live at https://docs.opendatakit.org

If you can't find what you are looking for, try the [old docs on the ODK website](https://opendatakit.org/). Also, please [file an issue](https://github.com/opendatakit/docs/issues) so that we know to add the information you are looking for.

## Building and viewing documentation locally

> See the [Contributor Guide](http://docs.opendatakit.org/contributing) for detailed steps --- no prior experience needed!

We require a Python version at [python3+](https://www.python.org/downloads/), you can also install Python using Virtual Environment or a version management like [pyenv](https://github.com/pyenv/pyenv) . To see your python and [pip](https://pip.pypa.io/en/stable/installing/) version:

```bash
$ python --version
$ pip -V
```

Once you have finished the installation of Python, you need to clone this repo and make sure all the requirements are installed:
```bash
$ git clone https://github.com/opendatakit/docs.git
$ cd docs/
$ pip install -r requirements.txt
```
These requirements including:

> - alabaster==0.7.10
> - Babel==2.4.0
> - docutils>=0.14
> - imagesize==0.7.1
> - Jinja2==2.9.6
> - MarkupSafe==1.0
> - Pygments==2.2.0
> - pytz==2017.2
> - requests==2.14.2
> - six==1.10.0
> - snowballstemmer==1.2.1
> - Sphinx==1.6.6
> - sphinx-rtd-theme==0.2.4
> - sphinxcontrib-websupport==1.0.1
> - sphinxcontrib-spelling
> - typing==3.6.1
> - Pillow==4.3.0
> - proselint
> - blessings
> - gitpython
> - sphinx-tabs==1.1.7

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

### **1. command not found**
#### Error message:
```bash
$ make odk1
rm -rf tmp1-src
rm -rf odk1-build/*
mkdir tmp1-src
cp -rf odk1-src/* tmp1-src
cp -rf shared-src/* tmp1-src
python: sphinx-build: command not found
make: *** [odk1] Error 127
```
#### Reason & Fix:
To build document, make sure you have installed `sphinx` in you current python version already. If you didn't install that, please using our `requirements.txt` file or manually.

### **2. incorrect sphinx version**
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
Configuration error:
There is a programable error in your configuration file:
...
from sphinx.util.compat import Directive
ImportError: cannot import name Directive
```

#### Reason & Fix:
You got an incorrect sphinx version, we need the 1.6.6 version. You can fix this by reinstall sphinx using:

```bash
$ pip install sphinx==1.6.6 
```
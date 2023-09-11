# ODK Docs

![Platform](https://img.shields.io/badge/platform-Sphinx-blue.svg) [![License](https://img.shields.io/badge/license-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/) [![Build status](https://circleci.com/gh/getodk/docs.svg?style=shield)](https://circleci.com/gh/getodk/docs/)

This repo is the source for ODK documentation.

The published documentation is at:

 - https://docs.getodk.org

Please [file an issue](https://github.com/getodk/docs/issues) if you can't find what you are looking for.

## Building and viewing documentation

### Prerequisites

 * Install [Python 3.10+](https://www.python.org/downloads/)
 * Install [git](https://git-scm.com/downloads)
 * Install [Git-LFS](https://git-lfs.github.com/)

We highly recommend you use a virtual environment like [virtualenv](https://virtualenv.pypa.io/en/stable/).

### Cloning the repo

Clone the docs repo and make sure all the requirements are installed:

```bash
$ git clone https://github.com/getodk/docs.git
$ cd docs/
```

If you wish to use virtualenv, now is a good time to set it up:

```bash
$ python -m venv venv
$ source venv/bin/activate
```

You will see `(venv)` next to your prompt to indicate you are working within the docs project. To exit this mode, use the command `deactivate`.

Whether you are using virtualenv or not, you next need to install the dependencies:

```bash
$ pip install -r requirements.txt
```

It can take a long time (>10 minutes) to clone the repo due to the large number of images in the docs. If you get an error such as `Smudge error` or `GitHub's rate limit reached`, run `git checkout -f HEAD` until you get the message `Checking out files: 100% done`.

### Building the docs

Once your environment is set up, build and serve the docs locally with:

```bash
$ make autobuild
```

You can then view the docs in your browser at [http://localhost:8000](http://localhost:8000). The docs will auto-build and refresh as you make changes to the source files.

You can use `make dirhtml` to for a one-time build of the HTML files and `make clean` to clean the build.

## How to contribute?

We are open for new issues and pull requests.

 - Please read the [Contributors Guide](https://docs.getodk.org/contributing) before working on the documentation.
 - Find issues to work on.
    - First time contributors are encouraged to complete a [line edit](https://github.com/getodk/docs/issues/96) as a way to get familiar with our contribution process.
	- Issues labelled [easy](https://github.com/getodk/docs/labels/easy) do not require much specific technical knowledge.
	- Issues labelled [contributor friendly](https://github.com/getodk/docs/labels/contributor%20friendly) are usually self-contained and don't require extensive knowledge of the ODK ecosystem as a whole.

You can also...

 - [Discuss the documentation from a user perspective in our forum](https://forum.getodk.org/c/development/documentation).
 - [Discuss the documentation from a contributor perspective in our developer Slack](slack.getodk.org). (Use the #docs-code channel.)
 - [File an issue](https://github.com/getodk/docs/issues) for any needed improvements.
 - [Watch](https://github.com/getodk/docs/subscription) and star this repo, to keep up with what we're doing.

## Troubleshooting
- If you get an `extension error` or a `configuration error`:
  - Make sure your virtual environment is activated.
  - Type `python --version` to check your current python version (it should be 3.x).
  - Run `pip install -r requirements.txt`.

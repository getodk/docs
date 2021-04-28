# ODK-X Docs

![Platform](https://img.shields.io/badge/platform-Sphinx-blue.svg) [![License](https://img.shields.io/badge/license-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/) [![Build status](https://circleci.com/gh/odk-x/docs.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/odk-x/docs/)  [![Netlify Status](https://api.netlify.com/api/v1/badges/d3788b3e-1abc-431d-a9a3-e5c71b20e053/deploy-status)](https://app.netlify.com/sites/blissful-bohr-7f32fb/deploys)

This repo is the source for ODK-X documentation.

The published documentation is at:

 - https://docs.odk-x.org/

Please [file an issue](https://github.com/odk-x/tool-suite-X/issues) if you can't find what you are looking for.

## Building and viewing documentation locally

There are two options for building and viewing ODK-X docs locally: [using Docker](#docker) or [setting up a local Python/Sphinx environment](#python-environment). We generally recommend starting with the Docker image unless you already have a Sphinx environment set up. The [Contributor Guide](https://docs.odk-x.org/contributing) describes the philosophy behind the docs, style considerations, how to write restructured text, and more.

There are two options to build ODK-X documents 

* [Docker Hosted Build Environment](#docker)
* [Python Build Environment](#python-environment)

The Docker environment is recommended because of the fewer setup steps required and less environmental variable paths that need to be set.

------------------------------------------
## <a name="docker"></a>Using Docker Hosted Build  Environment

[Docker](https://www.docker.com/) is a platform that makes it easier to package applications so that they can work on any computer. This is particularly valuable when setting up development environments that can work very differently based on versions of the tools involved.

### Prerequisites
 * Install Docker
   * Windows and Mac users should follow the instructions in [the get started guide](https://www.docker.com/get-started)
   * Linux users should follow the instructions for their specific distribution: [CentOS](https://docs.docker.com/install/linux/docker-ce/centos/), [Debian](https://docs.docker.com/install/linux/docker-ce/debian/), [Fedora](https://docs.docker.com/install/linux/docker-ce/fedora/), [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/), [Binaries](https://docs.docker.com/install/linux/docker-ce/binaries/)

   More info at the [Docker CE docs page](https://docs.docker.com/install/)
 * Install [git](https://git-scm.com/downloads)
 * Install [Git-LFS](https://git-lfs.github.com/)

### Cloning the repo

Clone the docs repo into a directory you want the ODK-X docs files to be located. For example, navigate to the directory you want the files to be located using the "cd" (Change Directory) command on the command line:.
```
cd <DIRECTORY>
```

Then use git to get a copy of the ODK-X documentation files.

```
git clone https://github.com/odk-x/docs.git
```

It can take a long time (>10 minutes) to clone the repo due to the large number of images in the docs. If you get an error such as `Smudge error` or `GitHub's rate limit reached`, run `git checkout -f HEAD` until you get the message `Checking out files: 100% done`.

After the git clone finishes, use the cd command to change directory to where the cloned files are located. Likely `cd docs`

### Building the Docker image

Next, you need to build the Docker image with all the tools you will be using to work with ODK-X's docs.

```
docker build -t odkx-docs .
```

It can take a long time to build the Docker image, but you only need to do this once.

**Windows users**
 * All commands should be run in an elevated PowerShell window. Right-click on PowerShell and select the "Run as administrator" option. NOTE: when running as an administrator PowerShell will default to the Windows directory. You will need to use the "cd" (Change Directory) command to navigate to a directory that you want the ODK-X documentation files to be located.
 * Ensure Docker is running by checking your system tray. If Docker is not running, launch "Docker for Windows" app and wait until a notification confirms that Docker is running.

### Building and serving the docs locally

Build and serve the docs locally with:
 * Windows: `.\run-task.bat odkx-autobuild`
 * Linux/macOS: `./run-task.sh odkx-autobuild`

Once your terminal shows a "Serving on http://0.0.0.0:8080" message, you can then view the docs in your browser at http://localhost:8080.

Changes you make in the source files will automatically be built and shown in your browser.

Press `Ctrl-C` on your keyboard to stop the build server. It could take a while to effectively stop, and you can always close the terminal window.

If you get a `The name "odkx-docs" is already in use by container` error message, run the following command:

```
docker kill odkx-docs
```

### Other build tasks

You can also use the `run-task` script described above to run just a portion of the build process. See available [build tasks](#tasks) below.

-----------------------------

## <a name="python-environment"></a>Python Environment

### Prerequisites

 * Install [Python 3](https://www.python.org/downloads/)
 * Install [git](https://git-scm.com/downloads)
 * Install [Git-LFS](https://git-lfs.github.com/)

After installing, you should verify that Python was successfully installed and is available on your PATH. To verify Python is installed properly and has been added to your PATH, query the Python version using the following command.
 
	Bash (Linux/Mac)

	$ python3 --version

    PowerShell (Windows)

    > python --version
 
The system should return something like "Python 3.X.X" where X is the other version numbers of your install.

[Here is a website](https://datatofish.com/add-python-to-windows-path/) that explains how to set up Python to be on the Window's PATH. 
 
### (Optional) Setup Python Virtual Environment 
We recommend you use a virtual environment like [virtualenv](https://virtualenv.pypa.io/en/stable/) or a Python version management like [pyenv](https://github.com/pyenv/pyenv) to avoid conflicts with packages. This section can be skipped if you do not have multiple Python projects using pip (package installer for Python). 


- Instructions for setting up virtual environment:

      A `virtual environment`_ is a Python construct
      that lets you download and install tools for a specific project
      without installing them for your entire computer.

      .. _virtual environment: https://docs.python.org/3/tutorial/venv.html

	  #. Create a directory called 'odkx'
		  Create a directory for the documents. We will use the folder 'odkx' as the directory that will contain the ODK-X Docs environment.


			mkdir odkx


		  Next, change the current working directory to 'odkx'


			cd odkx


      #. Create the virtual environment.



		Next, create the virtual environment.

			Bash

				/odkx/ $ python3 -m venv odkxenv

            PowerShell

                /odkx/ > python -m venv odkxenv

      #. Activate the virtual environment.

			Bash

                /odkx/ $ source odkxenv/bin/activate
                (odkxenv) /odkx/ $

			PowerShell

                /odkx/ > .\odkxenv\Scripts\activate
                (odkxenv) /odkx/ >

         The ``(odkxenv)`` before the prompt shows that the virtual environment is active.
         You will need to have this active any time you are working on the docs.

         If the file cannot be found, your activate file may be located under odkxenv/scripts/activate.

         Later, to deactivate the virtual environment:

		  Bash

                  (odkxenv) /odkx/ $ deactivate
                  /odkx/ $

		  PowerShell

                  (odkxenv) /odkx/ > deactivate
                  /odkx/ >


### Cloning the repo

Clone the docs repo and make sure all the requirements are installed:

```bash
$ git clone https://github.com/odk-x/docs.git
$ cd docs/
$ pip install -r requirements.txt
```

It can take a long time (>10 minutes) to clone the repo due to the large number of images in the docs. If you get an error such as `Smudge error` or `GitHub's rate limit reached`, run `git checkout -f HEAD` until you get the message `Checking out files: 100% done`.

### Building the docs

Once your environment is set up, build and serve the docs locally with:

```bash
$ make odkx
$ cd odkx-build
$ python -m http.server 8000
```

You can then view the docs in your browser at [http://localhost:8000/odkx-build/](http://localhost:8000/odkx-build/).

You can also use `make` to run just a portion of the build process. See available [build tasks](#tasks) below.

## <a name="tasks"></a>Build tasks

|             | Build & Serve  |   Build    |   Copy    |   LaTeX    |   Style Check    |   Spell Check    | Check All  |
| ----------- | :------------: | :--------: | :-------: | :--------: | :--------------: | :--------------: | :--------: |
| **Options** | odkx-autobuild | odkx-build | odkx-copy | odkx-latex | odkx-style-check | odkx-spell-check | odkx-check |


## How to contribute?

We are open to new issues and pull requests.

 - Please read the [Contributors Guide](https://docs.odk-x.org/contributing) before working on the documentation.
 - Find issues to work on.
   - Issues labeled [easy win](https://github.com/odk-x/tool-suite-X/labels/easy%20win) do not require much specific technical knowledge.
   - Issues labeled [good first issue](https://github.com/odk-x/tool-suite-X/labels/good%20first%20issue) are usually self-contained and don't require extensive knowledge of the ODK-X ecosystem as a whole.

You can also...

 - [Discuss the documentation from a user perspective in our forum](https://forum.odk-x.org/c/development/documentation).
 - [File an issue](https://github.com/odk-x/tool-suite-X/issues) for any needed improvements.
 - [Watch](https://github.com/odk-x/docs/subscription) and star this repo, to keep up with what we're doing.

## Troubleshooting
- If you get an `extension error` or a `configuration error`:
  - Make sure your virtual environment is activated.
  - Type `python --version` to check your current python version (it should be 3.x).
  - Run `pip install -r requirements.txt`.

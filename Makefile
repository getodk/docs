# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs
BUILDDIR      = docs/_build
SPHINXHOST    = 127.0.0.1

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

.PHONY: autobuild
autobuild:
	sphinx-autobuild -b dirhtml "$(SOURCEDIR)" "$(BUILDDIR)/html" --re-ignore "central-api|_build" --host 0.0.0.0

.PHONY: autobuild-docker
autobuild-docker:
	docker build --tag odk-docs-autobuild . && \
	docker run --publish 8000:8000 --volume ./docs:/docs:rw odk-docs-autobuild

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

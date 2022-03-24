# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS = 
SPHINXBUILD = sphinx-build
SPHINXPROJ = ODK
SRCDIR = src
TMPDIR = tmp
BUILDDIR = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help

.PHONY: help Makefile

autobuild:
	sphinx-autobuild --poll -p 8080 -H 0.0.0.0 src build

clean:
	rm -rf $(TMPDIR)
	rm -rf $(BUILDDIR)

clean-files:
	rm -rf $(TMPDIR)
	rm -rf $(BUILDDIR)/*

copy: clean-files
	mkdir $(TMPDIR)
	cp -rf $(SRCDIR)/* $(TMPDIR)

build: copy
	@$(SPHINXBUILD) -b dirhtml "$(TMPDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

deploy: copy
	@$(SPHINXBUILD) -W -b dirhtml "$(TMPDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

build-all: build

latex: build
	@$(SPHINXBUILD) -b latex "$(TMPDIR)" "$(BUILDDIR)"/latex $(SPHINXOPTS)
	python3 util/resize.py "$(BUILDDIR)"

style-check: build
	python3 style-test.py -r $(TMPDIR)

spell-check: build
	sphinx-build -b spelling $(TMPDIR) $(BUILDDIR)/spelling
	python3 util/check-spelling-output.py $(BUILDDIR)

check: style-check spell-check

check-all: check

test:
	pytest

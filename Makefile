# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
PYTHON = python3
SPHINXOPTS    = 
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = ODKX
ODKX_SRCDIR   = odkx-src
COMPILE_X_SRCDIR = tmpx-src
ODKX_BUILDDIR = odkx-build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help

.PHONY: help Makefile

odkx-autobuild:
	sphinx-autobuild --poll -p 8080 -H 0.0.0.0 odkx-src odkx-build

odkx-clean:
	rm -rf $(COMPILE_X_SRCDIR)
	rm -rf $(ODKX_BUILDDIR)

odkx-clean-files:
	rm -rf $(COMPILE_X_SRCDIR)
	rm -rf $(ODKX_BUILDDIR)/*

clean: odkx-clean

odkx-copy: odkx-clean-files
	mkdir $(COMPILE_X_SRCDIR)
	cp -rf $(ODKX_SRCDIR)/* $(COMPILE_X_SRCDIR)

odkx: odkx-copy
	@$(SPHINXBUILD) -b dirhtml "$(COMPILE_X_SRCDIR)" "$(ODKX_BUILDDIR)" $(SPHINXOPTS)

odkx-deploy: odkx-copy
	@$(SPHINXBUILD) -W -b dirhtml "$(COMPILE_X_SRCDIR)" "$(ODKX_BUILDDIR)" $(SPHINXOPTS)

build-all: odkx

odkx-latex: odkx
	@$(SPHINXBUILD) -b latex "$(COMPILE_X_SRCDIR)" "$(ODKX_BUILDDIR)"/latex $(SPHINXOPTS)
	$(PYTHON) util/resize.py "$(ODKX_BUILDDIR)"

odkx-pdf: odkx-latex
	cd "$(ODKX_BUILDDIR)"/latex && \
	xelatex ODK-X.tex && \
	xelatex ODK-X.tex && \
	mkdir -p ../_downloads && \
	mv ODK-X.pdf ../_downloads/ODK-X-Documentation.pdf

odkx-style-check: odkx
	$(PYTHON) style-test.py -r $(COMPILE_X_SRCDIR)

odkx-spell-check: odkx
	sphinx-build -b spelling $(COMPILE_X_SRCDIR) $(ODKX_BUILDDIR)/spelling
	$(PYTHON) util/check-spelling-output.py $(ODKX_BUILDDIR)

odkx-check: odkx-style-check odkx-spell-check

check-all: odkx-check

test:
	pytest

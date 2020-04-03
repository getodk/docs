# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    = 
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = ODK
ODK1_SRCDIR	  = odk1-src
SHARED_SRCDIR = shared-src
COMPILE1_SRCDIR = tmp1-src
ODK1_BUILDDIR = odk1-build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help

.PHONY: help Makefile

odk1-autobuild:
	sphinx-autobuild --poll -p 8080 -H 0.0.0.0 odk1-src odk1-build

odk1-clean:
	rm -rf $(COMPILE1_SRCDIR)
	rm -rf $(ODK1_BUILDDIR)

odk1-clean-files:
	rm -rf $(COMPILE1_SRCDIR)
	rm -rf $(ODK1_BUILDDIR)/*

clean: odk1-clean

odk1-copy: odk1-clean-files
	mkdir $(COMPILE1_SRCDIR)
	cp -rf $(ODK1_SRCDIR)/* $(COMPILE1_SRCDIR)
	cp -rf $(SHARED_SRCDIR)/* $(COMPILE1_SRCDIR)

odk1: odk1-copy
	@$(SPHINXBUILD) -b dirhtml "$(COMPILE1_SRCDIR)" "$(ODK1_BUILDDIR)" $(SPHINXOPTS)

odk1-deploy: odk1-copy
	@$(SPHINXBUILD) -W -b dirhtml "$(COMPILE1_SRCDIR)" "$(ODK1_BUILDDIR)" $(SPHINXOPTS)

build-all: odk1

odk1-latex: odk1
	@$(SPHINXBUILD) -b latex "$(COMPILE1_SRCDIR)" "$(ODK1_BUILDDIR)"/latex $(SPHINXOPTS)
	python util/resize.py "$(ODK1_BUILDDIR)"

odk1-pdf: odk1-latex
	cd "$(ODK1_BUILDDIR)"/latex && \
	xelatex OpenDataKit.tex && \
	xelatex OpenDataKit.tex && \
	mkdir -p ../_downloads && \
	mv OpenDataKit.pdf ../_downloads/ODK-Documentation.pdf

odk1-style-check: odk1
	python style-test.py -r $(COMPILE1_SRCDIR)

odk1-spell-check: odk1
	sphinx-build -b spelling $(COMPILE1_SRCDIR) $(ODK1_BUILDDIR)/spelling
	python util/check-spelling-output.py $(ODK1_BUILDDIR)

odk1-check: odk1-style-check odk1-spell-check

check-all: odk1-check

odk1-compress: odk1
	pngquant "$(ODK1_BUILDDIR)"/_images/*.png --force --ext .png --verbose

test:
	pytest

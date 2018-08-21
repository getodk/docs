# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    = 
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = OpenDataKit
ODK1_SRCDIR	  = odk1-src
ODK2_SRCDIR   = odk2-src
SHARED_SRCDIR = shared-src
COMPILE1_SRCDIR = tmp1-src
COMPILE2_SRCDIR = tmp2-src
ODK1_BUILDDIR = odk1-build
ODK2_BUILDDIR = odk2-build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help

.PHONY: help Makefile

odk1-clean:
	rm -rf $(COMPILE1_SRCDIR)
	rm -rf $(ODK1_BUILDDIR)

odk2-clean:
	rm -rf $(COMPILE2_SRCDIR)
	rm -rf $(ODK2_BUILDDIR)

odk1-clean-files:
	rm -rf $(COMPILE1_SRCDIR)
	rm -rf $(ODK1_BUILDDIR)/*

odk2-clean-files:
	rm -rf $(COMPILE2_SRCDIR)
	rm -rf $(ODK2_BUILDDIR)/*

clean: odk1-clean odk2-clean

odk1-copy: odk1-clean-files
	mkdir $(COMPILE1_SRCDIR)
	cp -rf $(ODK1_SRCDIR)/* $(COMPILE1_SRCDIR)
	cp -rf $(SHARED_SRCDIR)/* $(COMPILE1_SRCDIR)

odk2-copy: odk2-clean-files
	mkdir $(COMPILE2_SRCDIR)
	cp -rf $(ODK2_SRCDIR)/* $(COMPILE2_SRCDIR)
	cp -rf $(SHARED_SRCDIR)/* $(COMPILE2_SRCDIR)

odk1: odk1-copy
	@$(SPHINXBUILD) -b dirhtml "$(COMPILE1_SRCDIR)" "$(ODK1_BUILDDIR)" $(SPHINXOPTS)

odk2: odk2-copy
	@$(SPHINXBUILD) -b dirhtml "$(COMPILE2_SRCDIR)" "$(ODK2_BUILDDIR)" $(SPHINXOPTS)

odk1-deploy: odk1-copy
	@$(SPHINXBUILD) -W -b dirhtml "$(COMPILE1_SRCDIR)" "$(ODK1_BUILDDIR)" $(SPHINXOPTS)

odk2-deploy: odk2-copy
	@$(SPHINXBUILD) -W -b dirhtml "$(COMPILE2_SRCDIR)" "$(ODK2_BUILDDIR)" $(SPHINXOPTS)

build-all: odk1 odk2

odk1-latex: odk1
	@$(SPHINXBUILD) -b latex "$(COMPILE1_SRCDIR)" "$(ODK1_BUILDDIR)"/latex $(SPHINXOPTS)
	python util/resize.py "$(ODK1_BUILDDIR)"

odk2-latex: odk2
	@$(SPHINXBUILD) -b latex "$(COMPILE2_SRCDIR)" "$(ODK2_BUILDDIR)"/latex $(SPHINXOPTS)
	python util/resize.py "$(ODK2_BUILDDIR)"

odk1-pdf: odk1-latex
	cd "$(ODK1_BUILDDIR)"/latex && \
	xelatex OpenDataKit.tex && \
	xelatex OpenDataKit.tex && \
	mkdir -p ../_downloads && \
	mv OpenDataKit.pdf ../_downloads/ODK-Documentation.pdf

odk2-pdf: odk2-latex
	cd "$(ODK2_BUILDDIR)"/latex && \
	xelatex OpenDataKit2.tex && \
	xelatex OpenDataKit2.tex && \
	mkdir -p ../_downloads && \
	mv OpenDataKit2.pdf ../_downloads/ODK2-Documentation.pdf

odk1-style-check: odk1
	python style-test.py -r $(COMPILE1_SRCDIR)

odk1-spell-check: odk1
	sphinx-build -b spelling $(COMPILE1_SRCDIR) $(ODK1_BUILDDIR)/spelling
	python util/check-spelling-output.py $(ODK1_BUILDDIR)

odk2-style-check: odk2
	python style-test.py -r $(COMPILE2_SRCDIR)

odk2-spell-check: odk2
	sphinx-build -b spelling $(COMPILE2_SRCDIR) $(ODK2_BUILDDIR)/spelling
	python util/check-spelling-output.py $(ODK2_BUILDDIR)

odk1-check: odk1-style-check odk1-spell-check

odk2-check: odk2-style-check odk2-spell-check

check-all: odk1-check odk2-check

test:
	pytest
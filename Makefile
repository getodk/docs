# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    = 
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = OpenDataKit
ODK1_SRCDIR	  = odk1-src
ODKX_SRCDIR   = odkx-src
SHARED_SRCDIR = shared-src
COMPILE1_SRCDIR = tmp1-src
COMPILE_X_SRCDIR = tmpx-src
ODK1_BUILDDIR = odk1-build
ODKX_BUILDDIR = odkx-build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help

.PHONY: help Makefile

odk1-autobuild:
	sphinx-autobuild --poll -p 8080 -H 0.0.0.0 odk1-src odk1-build

odkX-autobuild:
	sphinx-autobuild --poll -p 8080 -H 0.0.0.0 odkX-src odkX-build

odk1-clean:
	rm -rf $(COMPILE1_SRCDIR)
	rm -rf $(ODK1_BUILDDIR)

odkx-clean:
	rm -rf $(COMPILE_X_SRCDIR)
	rm -rf $(ODKX_BUILDDIR)

odk1-clean-files:
	rm -rf $(COMPILE1_SRCDIR)
	rm -rf $(ODK1_BUILDDIR)/*

odkx-clean-files:
	rm -rf $(COMPILE_X_SRCDIR)
	rm -rf $(ODKX_BUILDDIR)/*

clean: odk1-clean odkx-clean

odk1-copy: odk1-clean-files
	mkdir $(COMPILE1_SRCDIR)
	cp -rf $(ODK1_SRCDIR)/* $(COMPILE1_SRCDIR)
	cp -rf $(SHARED_SRCDIR)/* $(COMPILE1_SRCDIR)

odkx-copy: odkx-clean-files
	mkdir $(COMPILE_X_SRCDIR)
	cp -rf $(ODKX_SRCDIR)/* $(COMPILE_X_SRCDIR)
	cp -rf $(SHARED_SRCDIR)/* $(COMPILE_X_SRCDIR)

odk1: odk1-copy
	@$(SPHINXBUILD) -b dirhtml "$(COMPILE1_SRCDIR)" "$(ODK1_BUILDDIR)" $(SPHINXOPTS)

odkx: odkx-copy
	@$(SPHINXBUILD) -b dirhtml "$(COMPILE_X_SRCDIR)" "$(ODKX_BUILDDIR)" $(SPHINXOPTS)

odk1-deploy: odk1-copy
	@$(SPHINXBUILD) -W -b dirhtml "$(COMPILE1_SRCDIR)" "$(ODK1_BUILDDIR)" $(SPHINXOPTS)

odkx-deploy: odkx-copy
	@$(SPHINXBUILD) -W -b dirhtml "$(COMPILE_X_SRCDIR)" "$(ODKX_BUILDDIR)" $(SPHINXOPTS)

build-all: odk1 odkx

odk1-latex: odk1
	@$(SPHINXBUILD) -b latex "$(COMPILE1_SRCDIR)" "$(ODK1_BUILDDIR)"/latex $(SPHINXOPTS)
	python util/resize.py "$(ODK1_BUILDDIR)"

odkx-latex: odkx
	@$(SPHINXBUILD) -b latex "$(COMPILE_X_SRCDIR)" "$(ODKX_BUILDDIR)"/latex $(SPHINXOPTS)
	python util/resize.py "$(ODKX_BUILDDIR)"

odk1-pdf: odk1-latex
	cd "$(ODK1_BUILDDIR)"/latex && \
	xelatex OpenDataKit.tex && \
	xelatex OpenDataKit.tex && \
	mkdir -p ../_downloads && \
	mv OpenDataKit.pdf ../_downloads/ODK-Documentation.pdf

odkx-pdf: odkx-latex
	cd "$(ODKX_BUILDDIR)"/latex && \
	xelatex OpenDataKitX.tex && \
	xelatex OpenDataKitX.tex && \
	mkdir -p ../_downloads && \
	mv OpenDataKitX.pdf ../_downloads/ODK-X-Documentation.pdf

odk1-style-check: odk1
	python style-test.py -r $(COMPILE1_SRCDIR)

odk1-spell-check: odk1
	sphinx-build -b spelling $(COMPILE1_SRCDIR) $(ODK1_BUILDDIR)/spelling
	python util/check-spelling-output.py $(ODK1_BUILDDIR)

odkx-style-check: odkx
	python style-test.py -r $(COMPILE_X_SRCDIR)

odkx-spell-check: odkx
	sphinx-build -b spelling $(COMPILE_X_SRCDIR) $(ODKX_BUILDDIR)/spelling
	python util/check-spelling-output.py $(ODKX_BUILDDIR)

odk1-check: odk1-style-check odk1-spell-check

odkx-check: odkx-style-check odkx-spell-check

check-all: odk1-check odkx-check

test:
	pytest

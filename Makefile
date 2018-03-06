# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = python -msphinx
SPHINXPROJ    = OpenDataKit
SOURCEDIR     = src
BUILDDIR      = _build
TRANSLATED_LANGUAGES = de,id,ja
LANGUAGES     = de,id,ja

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
        @echo "  translations          to build .po files and upload them to transifex"
	@echo "  pull-translations     to fetch translations form transifex for all languages"
	@echo "  pull-translations-%   to fetch translations form transifex for a specific language"
	@echo "  localizedhtml         to build localized html for all languages"
	@echo "  localizedhtml-%       to build localized html for specific language (2 letter code)"

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

translations: pull-translations push-translations
	@echo "Build finished."

pull-translations:
	@echo "Fetching translation files from transifex"
	tx pull --mode=developer -l $(TRANSLATED_LANGUAGES)
	@echo "Translations (.po) retrieved from transifex."

push-translations: clean html
	@echo "Building translation files"
	@make gettext
	@sphinx-intl update -p $(BUILDDIR)/locale -l $(TRANSLATED_LANGUAGES)
	@sphinx-intl update-txconfig-resources --pot-dir $(BUILDDIR)/gettext --transifex-project-name odk-docs
	@echo "Uploading translation files to Transifex"
	tx push -s
	@echo "Build finished. Translation templates (.pot) uploaded to transifex."


localizedhtml: clean
	@echo "Building translated html"
	for LANGUAGE in $(LANGUAGES); do make -e SPHINXOPTS="-D language='$$LANGUAGE'" html/$$LANGUAGE; done

localizedhtml-%:
	make -e SPHINXOPTS="-D language='$*'" html/$*
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html/$*."

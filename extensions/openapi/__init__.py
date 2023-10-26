import yaml
import pathlib
import re
import json
from datetime import date, datetime

# we should use chevron for it is recommended by Mustache but
# Nested partials bug: chevron/issues/100
import pystache

from sphinx.util import logging

from openapi.spec_processor import SpecProcessor 
import openapi.rst_helper

logger = logging.getLogger(__name__)

docDir = "./docs" 
currentDir = str(pathlib.Path(__file__).parent.resolve())
schemas = {}
renderer = pystache.Renderer(search_dirs=currentDir, escape=lambda s: s)

def builder_inited(app):
   main()

def main():
    spec = getYaml()
    writeTopPages(spec)
    processor = SpecProcessor(spec)
    files = processor.getResources(spec)
    for file in files.values():
        # result = ''
        with open(f'{currentDir}/template.mustache', 'r') as f:
          result = renderer.render(f.read(), file.get('data'))

        with open(f'{docDir}/central-api-{file.get("filename")}', 'w') as f:
          f.write(result)

def getYaml():
    with open(docDir + '/_static/api-spec/central.yaml', 'rt', encoding='UTF-8') as stream:
        return yaml.safe_load(stream)


def writeTopPages(spec):
    description = spec.get('info').get('description')
    title = spec.get('info').get('title')
    parts = description.split('## Changelog')

    files = []

    apiPages = []
    for tag in spec.get('tags'):
        if 'x-parent-tag' not in tag:
            apiPages.append('central-api-' + tag.get('name').lower().replace(' ', '-'))

    files.append({
        "filename": "central-api.rst",
        "data": {
            'title': title,
            'description': rst_helper.md2html(parts[0]),
            'hasToc': True,
            'toc': ['central-api-changelog'] + apiPages
        }
    })
    files.append({
        "filename": "central-api-changelog.rst",
        "data": {
            'title': "Changelog",
            'description': rst_helper.md2html(parts[1]),
            'hasToc': False
        }
    })
    for file in files:
        result = ''
        with open(f'{currentDir}/overview.mustache', 'r') as f:
          result = renderer.render(f.read(), file.get('data'))

        with open(f'{docDir}/{file.get("filename")}', 'w') as f:
          f.write(result)

def setup(app):
    logger.info("Converting Central OpenAPI to RST...")
    app.connect('builder-inited', builder_inited)

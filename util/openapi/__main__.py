import yaml
import pathlib
import re
import json
from datetime import date, datetime
# we should use chevron for it is recommended by Mustache but
# Nested partials bug: chevron/issues/100
import pystache

docDir = "./docs" 
currentDir = str(pathlib.Path(__file__).parent.resolve())
schemas = {}
renderer = pystache.Renderer(search_dirs=currentDir)

def main():
    print('GENERATING RST PAGES')
    spec = getYaml()
    writeTopPages(spec)
    global schemas
    schemas = spec.get('components').get('schemas')
    tags = spec.get('tags')
    files = dict()    
    for tag in tags:
        files[tag.get('name')] = {
            "filename": f"{tag.get('name').lower().replace(' ', '-')}.rst",
            "data": {
            'tag': tag.get('name'),
            'tagDescription': md2rs(tag.get('description')),
            'operations': []
            }
        }

    paths = spec.get('paths')
    for endpoint, path in paths.items():
        for method, operation in path.items():
            tag = operation.get("tags")[0]
            print(operation["tags"][0] + ':' + method + ':' + endpoint)
            files.get(tag).get('data').get('operations').append({
                'method': method.upper(),
                'endpoint': endpoint,
                'summary': operation.get('summary'),
                'description': md2rs(operation.get('description')),
                'request': getRequest(operation),
                'responses': getResponses(operation)
                })

        
    for file in files.values():
        result = ''
        with open(f'{currentDir}/template.mustache', 'r') as f:
          result = renderer.render(f.read(), file.get('data'))

        with open(f'{docDir}/central-api-{file.get("filename")}', 'w') as f:
          f.write(result)

def getYaml():
    with open(docDir + '/_static/api-spec/central.yaml', 'rt', encoding='UTF-8') as stream:
        return yaml.safe_load(stream)
    
def repeatChar(char, count):
    result = ''
    for i in range(count):
        result += char
    return result   

def md2rs(text):
    if text == None: return text

    r = formatVariables(text)
    r = formatItalic(r)
    r = formatBold(r)
    r = formatLinks(r)
    r = formatHeadings(r)
    return r

def formatLinks(text):
    return re.sub("\[([^\[]+)\]\(([^\(]*?)\)", "`\g<1> <\g<2>>`__", text)

def formatVariables(text):
    return re.sub("`([^`]+)`", "``\g<1>``\ ", text)

def formatHeadings(text):
    r = re.sub("^## (.*)$", "\g<1>\n" + repeatChar('-', 120), text,0,re.M)
    r = re.sub("^### (.*)$", "\g<1>\n" + repeatChar('^', 120), r,0,re.M)
    return r

def formatBold(text):
    return re.sub("\*\*(.*?)\*\*", "**\g<1>**\ ", text)

def formatItalic(text):
    return re.sub("_([^_]*)_", "*\g<1>*\ ", text)

def getRequest(operation):
    result = {}

    if 'parameters' in operation:
        result['parameters'] = {
        'hasItems': len(operation.get('parameters')) > 0,
        'items': map(lambda p: {
          'name': p.get('name'), 
          'in': p.get('in') if p.get('in') != 'path' else '', 
          'type': p.get('schema').get('type'),
          'example': p.get('example'),
          'description': p.get('description'),
          'hasItems': False
        }, operation.get('parameters'))
      }
        
    if 'requestBody' in operation:
        body = list(operation['requestBody']['content'].values())[0]
        schema = resolveSchema(body.get('schema'))
        example = ''
        if 'example' in body:
            example = body.get('example')
        else:
            example = getExampleValue(schema)

        example = json.dumps(example, indent = 2, default=json_serial)

        result['body'] = {
            'example':  {'lines': example.split('\n')},
            'schema': schema
        }

    return result

# see if this can be done with the resolve schema
def getExampleValue(schema):
    if 'example' in schema and schema['example'] != None:
        return schema['example']

    match schema['type']:
        case 'object':
            result = {}
            for item in schema['items']:
                result[item['name']] = getExampleValue(item)
        case 'array':
            result = [getExampleValue(schema['items'])]
        case 'string':
            result = 'pencil'
        case 'number':
            result = 1
        case 'boolean':
            result = True
        case _:
            raise Exception("type not handled")
    

    return result

def lookupSchema(name):
    global schemas
    if name in schemas:
        return schemas.get(name)
    else:
      return {} # TODO something reasonable should be returned or throw the error

# in case of 'oneOf' it is returning a list otherwise dict
def resolveSchema(schema):
    global schemas

    if schema == None:
        return {
          'hasItems': False
        }
    
    if 'oneOf' in schema:
        result = []
        for s in schema['oneOf']:
          result.append(resolveSchema(s))
        return result

    if 'allOf' in schema:
        result = {
          'name': '', # TODO is it used anywhere?
          'type': 'object',
          'description': md2rs(schema.get('description')),
          'example': schema.get('example'),
          'hasItems': False,
          'items': []
        }
        for s in schema['allOf']:
          result['items'] += resolveSchema(s)['items']

        if len(result['items'])  > 0:
            result['hasItems'] = True
        return result

    schema_type = schema.get('type', 'object')

    if schema_type == 'array':
        if 'items' in schema:
          items=resolveSchema(schema['items'])
        else:
          items=[]

        return {
            'type': 'array',
            'isArray': True,
            'name': schema.get('name'),
            'description': md2rs(schema.get('description')),
            'example': schema.get('example'),
            'hasItems': len(items) > 0,
            'items': items
        }

    if schema_type == 'object':
        if '$ref' in schema:
            return resolveSchema(lookupSchema(schema.get('$ref').replace('#/components/schemas/','')))

        results = []
        for name, prop in schema.get('properties', {}).items():
            prop['name'] = name
            result = resolveSchema(prop)
            results.append(result)
            
        return {
          'name': schema.get('name'),
          'type': schema.get('type'),
          'description': md2rs(schema.get('description')),
          'example': schema.get('example'),
          'hasItems': len(results) > 0,
          'items': results
        }
    
    # Primitives
    return {
        'name': schema.get('name'),
        'type': schema.get('type'),
        'description': md2rs(schema.get('description')),
        'example': schema.get('example'),
        'hasItems': False,
        'items': []
    }



# copied from
# https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable
def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat().replace('000+00:00', 'Z')
    raise TypeError ("Type %s not serializable" % type(obj))

def getResponses(operation):
    result = []

    for code, details in operation.get('responses').items():
      contents = list(details.get('content'))
      if len(contents) == 0: continue
      # we support just one content type for one status code
      contentType = list(details.get('content'))[0]
      if contentType == 'text/csv' or contentType == 'text/html' or contentType == 'application/xml' or contentType == 'text/xml':
          if 'example' in details.get('content').get(contentType):
            example = {'lines': details.get('content').get(contentType).get('example').split('\n')}
          else:
              example = {'lines': ['No Example'] }
          schema = {
              'type': 'string',
              'description': '',
              'hasItems': False,
              'items': []
          }
      else:
          schema = resolveSchema(details.get('content').get(contentType).get('schema'))
          example = ''
          if 'example' in details.get('content').get(contentType):
              example = details.get('content').get(contentType).get('example')
          else:
              example = getExampleValue(schema[0]) if type(schema) == list else getExampleValue(schema)

          example = json.dumps(example, indent = 2, default=json_serial)
          example = {'lines': example.split('\n')}

      result.append({
         'code': code,
         'contentType': contentType,
         'example': example,
         'schemas': schema
      })
    


    result[-1]['last'] = True
    return result

def writeTopPages(spec):
    description = spec.get('info').get('description')
    title = spec.get('info').get('title')
    parts = description.split('## Changelog')

    files = []
    files.append({
        "filename": "central-api.rst",
        "data": {
            'title': title,
            'description': md2rs(parts[0]),
            'hasToc': True,
            'toc': ['central-api-changelog'] + list(map(lambda t: 'central-api-'+t.get('name').lower().replace(' ', '-'), spec.get('tags')))
        }
    })
    files.append({
        "filename": "central-api-changelog.rst",
        "data": {
            'title': "Changelog",
            'description': md2rs(parts[1]),
            'hasToc': False
        }
    })
    for file in files:
        result = ''
        with open(f'{currentDir}/overview.mustache', 'r') as f:
          result = renderer.render(f.read(), file.get('data'))

        with open(f'{docDir}/{file.get("filename")}', 'w') as f:
          f.write(result)

if __name__ == '__main__':
    main()

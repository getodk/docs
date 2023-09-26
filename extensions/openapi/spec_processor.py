import json
from . import rst_helper
from . import json_helper


class SpecProcessor:
    def __init__(self, spec):
        self.spec = spec
        self.schemas = spec.get('components').get('schemas')

    def getResources(self, spec):
      files = dict()    
      tags = spec.get('tags')
      resources = dict()
      for tag in tags:
          if 'x-parent-tag' not in tag:
            files[tag.get('name')] = {
                "filename": f"{tag.get('name').lower().replace(' ', '-')}.rst",
                'data': {
                    "pageHeading": tag.get('name'),
                    'tagDescription': rst_helper.md2html(tag.get('description')),
                    'operations': [],
                    "resources": {}
                }
            }
          else:
            parent = tag.get('x-parent-tag')
            files.get(parent).get('data').get('resources')[tag.get('name')] = {
                'heading': tag.get('name'),
                'resourceDescription': rst_helper.md2html(tag.get('description')),
                'operations': []
            }

            # just for quick lookup of parent tag of the resource
            resources[tag.get('name')] = {
                'parent': parent
            }        

      paths = spec.get('paths')
      for endpoint, path in paths.items():
          for method, operation in path.items():
              tag = operation.get("tags")[0]
              # operation needs to go into a subheading
              if tag in resources:                  
                page = resources.get(tag).get('parent')
                opList = files.get(page).get('data').get('resources').get(tag).get('operations')
              # operation needs to go the top level
              else: 
                page = files.get(tag)
                opList = files.get(tag).get('data').get('operations')

              opList.append({
                  'method': method.upper(),
                  'endpoint': endpoint,
                  'summary': operation.get('summary'),
                  'headingUnderline': (len(operation.get('summary')) + 10) * '^' if tag in resources else (len(operation.get('summary')) + 10) * '-',
                  'description': rst_helper.md2html(operation.get('description')),
                  'request': self.getRequest(operation),
                  'responses': self.getResponses(operation)
                  })
      
      # convert page.resources into a list
      for page in files.values():
        page['data']['resources'] = list(page['data']['resources'].values())

      return files

    def getRequest(self, operation):
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
            schema = self.resolveSchema(body.get('schema'))
            example = ''
            if 'example' in body:
                example = body.get('example')
            else:
                example = self.getExampleValue(schema)

            example = json_helper.getJson(example)

            result['body'] = {
                'example':  {'lines': example.split('\n')},
                'schema': schema
            }

        return result

    def getResponses(self, operation):
        result = []

        for code, details in operation.get('responses').items():
          if details.get('content') is None: continue
          contents = list(details.get('content'))
          if len(contents) == 0: continue

          for contentType, content in details.get('content').items():
            if contentType == 'text/csv' or contentType == 'text/html' or contentType == 'application/xml' or contentType == 'text/xml':
                if 'example' in content:
                    example = {'lines': content.get('example').split('\n')}
                else:
                    example = {'lines': ['No Example'] }
                schema = {
                    'type': 'string',
                    'description': '',
                    'hasItems': False,
                    'items': []
                }
            else:
                schema = self.resolveSchema(content.get('schema'))
                example = ''
                if 'example' in content:
                    example = content.get('example')
                else:
                    example = self.getExampleValue(schema[0]) if type(schema) == list else self.getExampleValue(schema)

                example = json_helper.getJson(example)
                example = {'lines': example.split('\n')}

            result.append({
                'code': code,
                'contentType': contentType,
                'example': example,
                'schemas': schema
            })
        


        result[-1]['last'] = True
        return result
        
    def resolveSchema(self, schema):
        if schema is None:
            return {'hasItems': False}
        
        if 'oneOf' in schema:
            return self._resolveOneOf(schema)
        
        if 'allOf' in schema:
            return self._resolveAllOf(schema)

        schema_type = schema.get('type', 'object')

        if schema_type == 'array':
            return self._resolveArray(schema)

        if schema_type == 'object':
            if '$ref' in schema:
                # return self._resolveRef(schema)
                ref = self._resolveRef(schema)
                if 'name' not in ref or ref['name'] == '' or ref['name'] == None:
                    ref['name'] = schema.get('name')
                return ref
            else:
                return self._resolveObject(schema)

        return self._resolvePrimitive(schema)

    def _resolveOneOf(self, schema):
        result = []
        for s in schema['oneOf']:
            result.append(self.resolveSchema(s))
        return result

    def _resolveAllOf(self, schema):
        result = {
            'name': schema.get('name'),
            'type': 'object',
            'isArray': False,
            'description': rst_helper.md2html(schema.get('description')),
            'example': schema.get('example'),
            'hasItems': False,
            'items': []
        }
        for s in schema['allOf']:
            result['items'] += self.resolveSchema(s)['items']

        if len(result['items']) > 0:
            result['hasItems'] = True

        return result

    def _resolveArray(self, schema):
        if 'items' in schema:
            items = self.resolveSchema(schema['items'])
        else:
            items = []
        return {
            'type': 'array',
            'isArray': True,
            'name': schema.get('name'),
            'description': rst_helper.md2html(schema.get('description')),
            'example': json.dumps(schema.get('example')),
            'hasItems': len(items) > 0,
            'items': items
        }

    def _resolveRef(self, schema):
        return self.resolveSchema(self.lookupSchema(schema.get('$ref').replace('#/components/schemas/','')))

    def _resolveObject(self, schema):
        results = []
        for name, prop in schema.get('properties', {}).items():
            prop['name'] = name
            result = self.resolveSchema(prop)
            results.append(result)
        return {
            'name': schema.get('name'),
            'type': schema.get('type'),
            'description': rst_helper.md2html(schema.get('description')),
            'isArray': False,
            'example': schema.get('example'),
            'hasItems': len(results) > 0,
            'items': results
        }

    def _resolvePrimitive(self, schema):
        if 'enum' in schema:
            return self._resolveEnum(schema)
        return {
            'name': schema.get('name'),
            'type': schema.get('type'),
            'description': rst_helper.md2html(schema.get('description')),
            'isArray': False,
            'example': schema.get('example') if schema.get('type') != 'boolean' else str(schema.get('example')).lower(),
            'hasItems': False,
            'items': []
        }
    
    def _resolveEnum(self, schema):
        return {
            'name': schema.get('name'),
            'type': 'enum',
            'description': rst_helper.md2html(schema.get('description')),
            'example': '',
            'hasItems': True,
            'isArray': False,
            'items': list(map(lambda x: {
                'name': x,
                'type': 'string',
                'description': '',
                'hasItems': False
            }, schema.get('enum')))
        }

    def lookupSchema(self, name):
      if name in self.schemas:
          return self.schemas.get(name)
      else:
        raise Exception(f"Referenced schema {name} not found")

    @staticmethod
    def getExampleValue(schema):
      if 'example' in schema and schema['example'] != None:
          return schema['example']

      match schema['type']:
          case 'object':
              result = {}
              for item in schema['items']:
                  result[item['name']] = SpecProcessor.getExampleValue(item)
          case 'array':
              result = [SpecProcessor.getExampleValue(schema['items'])]
          case 'string':
              result = 'pencil'
          case 'number':
              result = 1
          case 'boolean':
              result = True
          case _:
              raise Exception("type not handled")      

      return result
import unittest
import yaml
import textwrap

from ..src.spec_processor import SpecProcessor
from ..src.json_helper import getJson


class TestSpecProcessor_getExampleValue(unittest.TestCase):

    # @unittest.skip("Not implemented")
    def test_getResources(self):
        with open('./docs/_static/api-spec/central.yaml', 'rt', encoding='UTF-8') as stream:
            spec = yaml.safe_load(stream)

        processor = SpecProcessor(spec)
        result = processor.getResources(spec)
        for pageName, page in result.items():
            # print("\n" + pageName)
            for operation in page.get('data').get('operations'):
                # print("--" + operation.get('method') + " " + operation.get('endpoint'))

                if 'parameters' in operation['request']:
                    requestParameters = operation['request']['parameters']
                    if requestParameters['hasItems']:
                        for parameter in requestParameters['items']:
                            # print("----" + parameter['name'] + "=" + parameter['example'])
                            self.assertTrue(parameter['example'] is not None and len(
                                parameter['example']) > 0, f"Example is empty for request parameter of {pageName} {operation['method']} {operation['endpoint']}")

                if 'body' in operation['request']:
                    requestBody = operation['request']['body']
                    exampleLines = requestBody['example']['lines']
                    # print("----" + " ".join(exampleLines))
                    self.assertTrue(len(exampleLines) > 0 and all(map(lambda e: e is not None or len(
                        e) > 0, exampleLines)), f"Example is empty for request body of {pageName} {operation['method']} {operation['endpoint']}")

                    # if requestBody['schema']:

            for resource in page.get('data').get('resources'):
                #  print("--" + resource.get('heading'))
                for operation in resource.get('operations'):
                    #  print("----" + operation.get('method') + " " + operation.get('endpoint'))

                    if 'parameters' in operation['request']:
                        requestParameters = operation['request']['parameters']
                        if requestParameters['hasItems']:
                            for parameter in requestParameters['items']:
                             #  print("------" + parameter['name'] + "=" + parameter['example'])
                                self.assertTrue(parameter['example'] is not None and len(
                                    parameter['example']) > 0, f"Example is empty for request parameter of {pageName} {operation['method']} {operation['endpoint']}")

                    if 'body' in operation['request']:
                        requestBody = operation['request']['body']
                        exampleLines = requestBody['example']['lines']
                        #  print("----" + " ".join(exampleLines))
                        self.assertTrue(
                            len(exampleLines) > 0 and all(map(lambda e: e is not None or len(e) > 0, exampleLines)),
                            f"Example is empty for request body of {pageName} {operation['method']} {operation['endpoint']}")

                        if requestBody['schema']['type'] == 'object' and not(requestBody['schema']['hasItems']):                            
                            print('object is not defined. ' + resource.get('heading') + " " + operation.get('method') + " " + operation.get('endpoint'))
                    
                    for response in operation['responses']:
                        exampleLines = response['example']['lines']
                        self.assertTrue(
                            len(exampleLines) > 0 and all(map(lambda e: e is not None or len(e) > 0, exampleLines)),
                            f"Example is empty for request body of {pageName} {operation['method']} {operation['endpoint']}")
                        
                        # print(type(response['schemas']))
                        if type(response['schemas']) is dict:
                            schemas = [response['schemas']]
                        else:
                            schemas = response['schemas']

                        for schema in schemas:
                            if 'type' in schema:
                                # print(schema['type'])
                                if schema['type'] == 'array':
                                    if schema['items']['type'] == 'object' and not(schema['items']['hasItems']):
                                        print('object is not defined. ' + resource.get('heading') + " " + operation.get('method') + " " + operation.get('endpoint'))
                                elif schema['type'] == 'object':
                                    if not(schema['hasItems']):
                                        print('object is not defined. ' + resource.get('heading') + " " + operation.get('method') + " " + operation.get('endpoint'))
                        

    def test_getExampleValue_with_valid_example(self):
        schema = {'type': 'string', 'example': 'example string'}
        result = SpecProcessor.getExampleValue(schema)
        self.assertEqual(result, 'example string')

    def test_getExampleValue_without_example(self):
        schema = {'type': 'string'}
        result = SpecProcessor.getExampleValue(schema)
        self.assertEqual(result, 'pencil')

    def test_getExampleValue_object(self):
        schema = {'type': 'object', 'items': [
            {'name': 'color', 'type': 'string'}, {'name': 'price', 'type': 'number'}]}
        result = SpecProcessor.getExampleValue(schema)
        expected = {'color': 'pencil', 'price': 1}
        self.assertEqual(result, expected)

    def test_getExampleValue_array(self):
        schema = {'type': 'array', 'items': {'type': 'number'}}
        result = SpecProcessor.getExampleValue(schema)
        expected = [1]
        self.assertEqual(result, expected)

    def test_getExampleValue_string(self):
        schema = {'type': 'string'}
        result = SpecProcessor.getExampleValue(schema)
        self.assertEqual(result, 'pencil')

    def test_getExampleValue_number(self):
        schema = {'type': 'number'}
        result = SpecProcessor.getExampleValue(schema)
        self.assertEqual(result, 1)

    def test_getExampleValue_boolean(self):
        schema = {'type': 'boolean'}
        result = SpecProcessor.getExampleValue(schema)
        self.assertEqual(result, True)

    def test_getExampleValue_invalid_type(self):
        schema = {'type': 'invalid'}
        with self.assertRaises(Exception):
            SpecProcessor.getExampleValue(schema)


@unittest.skip("Not implemented")
class TestSpecProcessor_resolveSchema(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.processor = SpecProcessor({
            'components': {
                'schemas': {
                    'project': {
                        'type': 'object',
                        'name': 'Project',
                        'description': 'A `Project` object.',
                        'properties': {
                            'name': {
                                'type': 'string',
                                'description': "The name of the project",
                                'example': 'Rural development'
                            },
                            'creatorId': {
                                'type': 'number',
                                'description': "The creator ID of the project",
                                'example': '1'
                            }
                        }
                    },
                    'projectExt': {
                        'type': 'object',
                        'name': 'Project Extended',
                        'description': 'An Extended Project object.',
                        'properties': {
                            'name': {
                                'type': 'string',
                                'description': "The name of the project",
                                'example': 'Rural development'
                            },
                            'creator': {
                                '$ref': '#/components/schemas/actor'
                            }
                        }
                    },
                    'actor': {
                        'type': 'object',
                        'name': 'Actor',
                        'description': 'An `Actor` object represents an actor in the system.',
                        'properties': {
                            'email': {
                                'type': 'string',
                                'description': "The `Actor`'s full email address."
                            },
                            'id': {
                                'type': 'number',
                                'description': "The `Actor`'s unique ID."
                            }
                        }
                    },
                    'actorExt': {
                        'allOf': [{
                            '$ref': '#/components/schemas/actor'
                        },
                            {
                            'type': 'object',
                            'name': 'ActorExtended',
                            'description': 'An Extended Actor',
                            'properties': {
                                'createdAt': {
                                    'type': 'string',
                                    'description': "Creation timestamp of the Actor"
                                }
                            }
                        }]
                    },
                    'status': {
                        'type': 'string',
                        'enum': ['active', 'inactive']
                    },
                }
            }
        })

    def test_resolveSchema_with_none_schema(self):
        schema = None
        expected_result = {'hasItems': False}
        result = self.processor.resolveSchema(schema)
        self.assertEqual(result, expected_result)

    def test_resolveSchema_with_object_schema(self):
        schema = {
            'type': 'object',
            'name': 'User',
            'description': 'A `User` object represents a user in the system.',
            'example': {
                'email': 'john.doe@example.com',
                'password': 'topsecret'
            },
            'properties': {
                'email': {
                    'type': 'string',
                    'description': "The `User`'s full email address.",
                    'example': 'john.doe@example.com'
                },
                'password': {
                    'type': 'string',
                    'description': "The `User`'s password.",
                    'example': 'topsecret'
                }
            }
        }
        expected_result = {
            'name': 'User',
            'type': 'object',
            'description': 'A ``User``\\  object represents a user in the system.',
            'example': {'email': 'john.doe@example.com', 'password': 'topsecret'},
            'hasItems': True,
            'items': [{
                'name': 'email',
                'type': 'string',
                'description':
                "The ``User``\\ 's full email address.",
                'example': 'john.doe@example.com',
                'hasItems': False,
                'items': []
            },
                {
                'name': 'password',
                'type': 'string',
                'description': "The ``User``\\ 's password.",
                'example': 'topsecret',
                'hasItems': False,
                'items': []
            }]
        }
        result = self.processor.resolveSchema(schema)
        self.assertEqual(result, expected_result)

    def test_resolveSchema_primitives(self):
        schema = {
            'name': 'myString',
            'type': 'string',
            'description': 'A string property',
            'example': 'Hello World'
        }
        result = self.processor.resolveSchema(schema)
        expected = {
            'name': 'myString',
            'type': 'string',
            'description': 'A string property',
            'example': 'Hello World',
            'hasItems': False,
            'items': []
        }
        self.assertEqual(result, expected)

    def test_resolveSchema_with_ref_object(self):
        schema = {
            'type': 'object',
            'name': 'Project',
            'description': 'A `User` object represents a user in the system.',
            'properties': {
                'name': {
                    'type': 'string',
                    'description': "The name of the project",
                    'example': 'Rural development'
                },
                'creator': {
                    '$ref': '#/components/schemas/actor'
                }
            }
        }

        expected_result = {
            'name': 'Project',
            'type': 'object',
            'description': 'A ``User``\\  object represents a user in the system.',
            'example': None,
            'hasItems': True,
            'items': [{
                'name': 'name',
                'type': 'string',
                'description': 'The name of the project',
                'example': 'Rural development',
                'hasItems': False,
                'items': []
            },
                {
                'name': 'Actor',
                'type': 'object',
                'description': 'An ``Actor``\\  object represents an actor in the system.',
                'example': None,
                'hasItems': True,
                'items': [{
                    'name': 'email',
                    'type': 'string',
                    'description': "The ``Actor``\\ 's full email address.",
                    'example': None,
                    'hasItems': False,
                    'items': []
                },
                    {
                    'name': 'id',
                    'type': 'number',
                    'description': "The ``Actor``\\ 's unique ID.",
                    'example': None,
                    'hasItems': False,
                    'items': []
                }]
            }
            ]
        }

        result = self.processor.resolveSchema(schema)
        self.assertEqual(result, expected_result)

    def test_resolveSchema_with_oneOf_schema(self):
        schema = {
            'oneOf': [{
                '$ref': '#/components/schemas/project'
            },
                {
                '$ref': '#/components/schemas/projectExt'
            }
            ]}

        expected_result = [
            {
                "name": "Project",
                "type": "object",
                "description": "A ``Project``\\  object.",
                "example": None,
                "hasItems": True,
                "items": [
                    {
                        "name": "name",
                        "type": "string",
                        "description": "The name of the project",
                        "example": "Rural development",
                        "hasItems": False,
                        "items": []
                    },
                    {
                        "name": "creatorId",
                        "type": "number",
                        "description": "The creator ID of the project",
                        "example": "1",
                        "hasItems": False,
                        "items": []
                    }
                ]
            },
            {
                "name": "Project Extended",
                "type": "object",
                "description": "An Extended Project object.",
                "example": None,
                "hasItems": True,
                "items": [
                    {
                        "name": "name",
                        "type": "string",
                        "description": "The name of the project",
                        "example": "Rural development",
                        "hasItems": False,
                        "items": []
                    },
                    {
                        'name': 'Actor',
                        'type': 'object',
                        'description': 'An ``Actor``\\  object represents an actor in the system.',
                        'example': None,
                        'hasItems': True,
                        'items': [{
                            'name': 'email',
                            'type': 'string',
                            'description':
                            "The ``Actor``\\ 's full email address.",
                            'example': None,
                            'hasItems': False,
                            'items': []
                        },
                            {
                            'name': 'id',
                            'type': 'number',
                            'description': "The ``Actor``\\ 's unique ID.",
                            'example': None,
                            'hasItems': False,
                            'items': []
                        }]
                    }
                ]
            }
        ]
        result = self.processor.resolveSchema(schema)
        # print(getJson(result))
        self.assertEqual(result, expected_result)

    @unittest.skip("Not implemented yet")
    def test_resolveSchema_with_allOf_schema(self):
        schema = {
            'allOf': [{
                '$ref': '#/components/schemas/actor'
            },
                {
                'type': 'object',
                'name': 'ActorExtended',
                'description': 'An Extended Actor',
                'properties': {
                    'createdAt': {
                        'type': 'string',
                        'description': "Creation timestamp of the Actor"
                    }
                }
            }]
        }
        expected_result = {
            "name": "",
            "type": "object",
            "description": None,
            "example": None,
            "hasItems": True,
            "items": [
                {
                    "name": "email",
                    "type": "string",
                    "description": "The ``Actor``\\ 's full email address.",
                    "example": None,
                    "hasItems": False,
                    "items": []
                },
                {
                    "name": "id",
                    "type": "number",
                    "description": "The ``Actor``\\ 's unique ID.",
                    "example": None,
                    "hasItems": False,
                    "items": []
                },
                {
                    "name": "createdAt",
                    "type": "string",
                    "description": "Creation timestamp of the Actor",
                    "example": None,
                    "hasItems": False,
                    "items": []
                }
            ]
        }
        result = self.processor.resolveSchema(schema)
        self.assertEqual(result, expected_result)

    @unittest.skip("Not implemented yet")
    def test_resolveSchema_with_array_schema(self):
        schema = {
            'type': 'array',
            'items': {
                'type': 'object',
                'name': 'Action',
                'description': 'An Action',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': "Action name"
                    }
                }
            }
        }

        expected_result = {
            "type": "array",
            "isArray": True,
            "name": None,
            "description": None,
            "example": None,
            "hasItems": True,
            "items": {
                "name": "Action",
                "type": "object",
                "description": "An Action",
                "example": None,
                "hasItems": True,
                "items": [
                    {
                        "name": "name",
                        "type": "string",
                        "description": "Action name",
                        "example": None,
                        "hasItems": False,
                        "items": []
                    }
                ]
            }
        }
        result = self.processor.resolveSchema(schema)
        self.assertEqual(result, expected_result)

    def test_resolveSchema_enum(self):
        schema = {
            'type': 'object',
            'properties': {
                'status': {
                    'type': 'string',
                    'enum': ['active', 'inactive']
                }
            }
        }
        result = self.processor.resolveSchema(schema)

        print(getJson(result))

    def test_resolveSchema_enum2(self):
        schema = {
            'type': 'object',
            'properties': {
                'status': {
                    '$ref': '#/components/schemas/status'
                }
            }
        }
        result = self.processor.resolveSchema(schema)

        print(getJson(result))


if __name__ == '__main__':
    unittest.main()

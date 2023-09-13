import unittest
import yaml
import textwrap

from src.spec_processor import SpecProcessor
from src.json_helper import getJson


class TestSpecProcessor_getExampleValue(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()

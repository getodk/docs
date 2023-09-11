import unittest
import textwrap
from datetime import datetime, date, timezone

from src.json_helper import getJson

class TestGetJson(unittest.TestCase):
    def test_serialize_datetime(self):
        # Test that a datetime object is serialized correctly
        obj = {
          'name': 'test',
          'description': 'lorem ipsum',
          'timestamp': datetime(2022, 5, 5, 12, 0, 0, 100000, tzinfo=timezone.utc),
          'child': {
              'name': 'child',
              'timestamp': datetime(2023, 5, 5, 12, 0, 0, 100000, tzinfo=timezone.utc)
          }
        } 
        expected_result = textwrap.dedent('''\
          {
            "name": "test",
            "description": "lorem ipsum",
            "timestamp": "2022-05-05T12:00:00.100Z",
            "child": {
              "name": "child",
              "timestamp": "2023-05-05T12:00:00.100Z"
            }
          }''')
        result = getJson(obj)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

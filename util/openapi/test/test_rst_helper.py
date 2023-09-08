import unittest
import textwrap
from src.rst_helper import *

class TestMarkdownConversion(unittest.TestCase):

    def test_md2rs(self):
        self.maxDiff = None
        text = textwrap.dedent('''\
          ## This is a heading

          ### This is a subheading

          **Bold text** and _Italic text_.
          [Google](https://www.google.com)''')
        expected_output = textwrap.dedent('''\
          <h2>This is a heading</h2><h3>This is a subheading</h3><p><strong>Bold text</strong> and <em>Italic text</em>.<a href="https://www.google.com">Google</a></p>''')
        self.assertEqual(md2rs(text), expected_output)

if __name__ == '__main__':
    unittest.main()

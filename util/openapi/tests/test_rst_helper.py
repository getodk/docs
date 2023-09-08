import unittest
import textwrap
from ..src.rst_helper import *

class TestMarkdownConversion(unittest.TestCase):
 
    def test_md2rs(self):
        self.maxDiff = None
        text = textwrap.dedent('''\
          ## This is a heading

          ### This is a subheading
          
          **Bold text** and _Italic text_.
          [Google](https://www.google.com)''')
        expected_output = textwrap.dedent('''\
          This is a heading
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

          This is a subheading
          """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
          
          **Bold text**\  and *Italic text*\ .
          `Google <https://www.google.com>`__''')
        self.assertEqual(md2rs(text), expected_output)        

if __name__ == '__main__':
    unittest.main()

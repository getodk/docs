import unittest
import textwrap
from ..src.rst_helper import *

class TestMarkdownConversion(unittest.TestCase):
    
    def test_formatLinks(self):
        self.assertEqual(formatLinks("[Google](https://www.google.com)"), "`Google <https://www.google.com>`__")
        self.assertEqual(formatLinks("[Facebook](https://www.facebook.com)"), "`Facebook <https://www.facebook.com>`__")
        self.assertEqual(formatLinks("[Twitter](https://www.twitter.com)"), "`Twitter <https://www.twitter.com>`__")
    
    def test_formatVariables(self):
        self.assertEqual(formatVariables("`foo`"), "``foo``\ ")
        self.assertEqual(formatVariables("`bar`"), "``bar``\ ")
        self.assertEqual(formatVariables("`baz`"), "``baz``\ ")
        
    def test_formatHeadings(self):
        text = "## This is a heading"
        expected_output = textwrap.dedent('''\
          This is a heading
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^''')
        
        self.assertEqual(formatHeadings(text), expected_output)
        
        text = "### This is a subheading"
        expected_output = textwrap.dedent('''\
          This is a subheading
          """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""''')
        self.assertEqual(formatHeadings(text), expected_output)
    
    def test_formatBold(self):
        self.assertEqual(formatBold("**Hello, world!**"), "**Hello, world!**\ ")
        self.assertEqual(formatBold("**Python** is a popular programming language."), "**Python**\  is a popular programming language.")
        
    def test_formatItalic(self):
        self.assertEqual(formatItalic("_Hello, world!_"), "*Hello, world!*\ ", 'italic')
        self.assertEqual(formatItalic("_Python_ is a popular programming language."), "*Python*\  is a popular programming language.")
    
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

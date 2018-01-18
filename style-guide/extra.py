# -*- coding: utf-8 -*-

"""quote marks and section label check"""

import re

def check_quotes(text):
    """Check straight quotes"""
    err = "style-guide.check-quote"
    msg = "Avoid using quote marks."
    regex = r"\W\"[a-zA-z0-9\s]*\"\W"
    
    errors = []

    for m in re.finditer(regex, text):
          start = m.start()+1
          end = m.end()
          (row, col) = line_and_column(text, start)
          extent = m.end()-m.start()
          errors += [(err, msg, row, col, start, end,
                           extent, "warning", "None")]  

    return errors

def check_curlyquotes(text):
    """Check curly quotes"""
    err = "style-guide.check-curlyquote"
    msg = "Do not use curly quotes. If needed use straight quotes."
    regex = r"\W\“[a-zA-z0-9\s]*\”\W"
    
    errors = []

    for m in re.finditer(regex, text):
          start = m.start()+1
          end = m.end()
          (row, col) = line_and_column(text, start)
          extent = m.end()-m.start()
          errors += [(err, msg, row, col, start, end,
                           extent, "warning", "None")]  

    return errors

def line_and_column(text, position):
    """Return the line number and column of a position in a string."""
    position_counter = 0
    for idx_line, line in enumerate(text.splitlines(True)):
        if (position_counter + len(line.rstrip())) >= position:
            return (idx_line, position - position_counter)
        else:
            position_counter += len(line)    

def check(text):
    """Run checks for quote marks and section labels"""
    text = text.read()
    error = []
    errors = check_quotes(text) + check_curlyquotes(text)    
    errors = sorted(errors, key=lambda e: (e[2], e[3]))
    return errors
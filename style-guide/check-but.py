# -*- coding: utf-8 -*-

"""Paragraph starts with but check."""

from proselint.tools import memoize, existence_check

@memoize
def check_but(text):
    """Don't start a paragraph with but."""
    err = "style-guide.check-but"
    msg = u"No paragraph should start with a 'But'."
    regex = "\n[ ]*\n[ ]*But"

    return existence_check(text, [regex], err, msg, ignore_case=False, 
    	                   require_padding=False)

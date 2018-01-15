# -*- coding: utf-8 -*-

"""ordered list check."""

from proselint.tools import memoize, existence_check

@memoize
def check_quotes(text):
    """Use unordered list if order of steps does not matter."""
    err = "style-guide.order-list"
    msg = "Use unordered list if order of steps does not matter."
    regex = "([0-9]*\.\s[(\x00-\x09)|(\x0B-\x7F)]*\n)+"

    return existence_check(text, [regex], err, msg, max_errors=3, require_padding=False)
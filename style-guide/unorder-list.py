# -*- coding: utf-8 -*-

"""unordered list check."""

from proselint.tools import memoize, existence_check

@memoize
def check_quotes(text):
    """Use ordered list if order of steps matters."""
    err = "style-guide.unorder-list"
    msg = "Use ordered list if order of steps matters."
    regex = "(\-\s[(\x00-\x09)|(\x0B-\x7F)]*\n)+"

    return existence_check(text, [regex], err, msg, max_errors=3, require_padding=False)
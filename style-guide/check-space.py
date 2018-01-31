# -*- coding: utf-8 -*-

"""Missing space check."""

from proselint.tools import memoize, existence_check

@memoize
def check_space(text):
    """Use single space after sentence end."""
    err = "style-guide.check-space"
    msg = "Missing space after period."
    regex = "[\.\?!][A-Z]{2,}"

    return existence_check(text, [regex], err, msg, ignore_case=False, 
    	                   require_padding=False)

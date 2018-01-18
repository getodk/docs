# -*- coding: utf-8 -*-

"""semicolon check."""

from proselint.tools import memoize, existence_check

@memoize
def check_semicolon(text):
    """Avoid using semicolon."""
    err = "style-guide.check-semicolon"
    msg = "Avoid using semicolon."
    regex = ";"

    return existence_check(text, [regex], err, msg, require_padding=False)
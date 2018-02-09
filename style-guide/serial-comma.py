# -*- coding: utf-8 -*-

"""serial comma check."""

from proselint.tools import memoize, existence_check

@memoize
def check_comma(text):
    """Use serial comma after penultimate item."""
    err = "style-guide.serial-comma"
    msg = "Use serial comma after penultimate item."
    regex = "\,\s[a-zA-Z0-9]+\sand\s"

    return existence_check(text, [regex], err, msg, require_padding=False)
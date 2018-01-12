# -*- coding: utf-8 -*-

"""quote marks check."""

from proselint.tools import memoize, existence_check

@memoize
def check_quotes(text):
    """Avoid quote marks."""
    err = "style-guide.check-quotes"
    msg = "Avoid using quote marks."
    regex = "\"[^\"]*\"|\“.*\“"

    return existence_check(text, [regex], err, msg, require_padding=False)
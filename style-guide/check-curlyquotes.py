# -*- coding: utf-8 -*-

"""curly quote marks check."""

from proselint.tools import memoize, existence_check

@memoize
def check_curlyquotes(text):
    """Avoid curly quote marks."""
    err = "style-guide.check-curlyquotes"
    msg = "Don't use curly quote marks. If required use straight quotes."
    regex = "“|“"

    return existence_check(text, [regex], err, msg, require_padding=False)
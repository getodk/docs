# -*- coding: utf-8 -*-
"""Latin abbreviations."""

from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check Latin abbrevaiations."""
    err = "style-guide.latin-abbr"
    msg = "Minimize your use of Latin abbreviations."

    list = [
        "etc.",
        "i.e.",
        "e.g.",
        "viz.",
        "c.f.",
        "n.b.",
    ]

    return existence_check(text, list, err, msg, ignore_case=True)

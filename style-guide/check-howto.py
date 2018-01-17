# -*- coding: utf-8 -*-
"""How to construct."""

from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check how to construct."""
    err = "style-guide.check-howto"
    msg = "Avoid using \"How to\" construction."

    list = [
        "How to",
    ]

    return existence_check(text, list, err, msg, ignore_case=False)

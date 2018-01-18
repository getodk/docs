# -*- coding: utf-8 -*-
"""Filler phrases."""

from proselint.tools import existence_check, memoize


@memoize
def check_filler(text):
    """Check Filler phrases."""
    err = "style-guide.filler-phrase"
    msg = "Avoid using filler phrases like \"to the extent that\"."

    list = [
        "to the extent that",
        "for all intents and purposes",
        "when all is said and done",
        "from the perspective of",
        "point in time",
    ]

    return existence_check(text, list, err, msg, ignore_case=True)

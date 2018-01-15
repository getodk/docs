# -*- coding: utf-8 -*-
"""Unneeded adverbs."""

from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check Unneeded adverbs."""
    err = "style-guide.unneed-adverb"
    msg = "Avoid using unneeded adverbs like \"just\", \"simply\"."

    list = [
        "simply",
        "easily",
        "just",
        "very",
        "really",
        "basically",
    ]

    return existence_check(text, list, err, msg, ignore_case=True)

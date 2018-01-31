# -*- coding: utf-8 -*-
"""Third-person personal pronouns."""

from proselint.tools import existence_check, memoize


@memoize
def check_pronoun(text):
    """Check third-person personal pronouns."""
    err = "style-guide.personal-pronoun"
    msg = "Avoid using third-person personal pronouns like \"he\", \"she\". "
    msg = msg + "In case of absolute need, prefer using \"they\"."

    list = [
        "he",
        "him",
        "his",
        "she",
        "her",
        "hers",
    ]

    return existence_check(text, list, err, msg, ignore_case=True)

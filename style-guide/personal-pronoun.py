# -*- coding: utf-8 -*-
"""Third-person personal pronouns."""

from proselint.tools import existence_check, memoize


@memoize
def check(text):
    """Check third-person personal pronouns."""
    err = "style-guide.personal-pronoun"
    msg = "Avoid using third-person personal pronouns like \"he.\", \"she.\", \"them\"."

    list = [
        "he",
        "him",
        "his",
        "she",
        "her",
        "hers",
        "they",
        "them",
        "their",
        "theirs",
    ]

    return existence_check(text, list, err, msg, ignore_case=True)

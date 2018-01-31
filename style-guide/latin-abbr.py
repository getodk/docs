# -*- coding: utf-8 -*-
"""Latin abbreviations."""

from proselint.tools import existence_check, memoize


@memoize
def check_latin(text):
    """Check Latin abbrevaiations."""
    err = "style-guide.latin-abbr"
    msg = "Avoid using Latin abbreviations like \"etc.\", \"i.e.\"."

    list = [
        "etc\.", "etc", "\*etc\.\*", "\*etc\*",
        "i\.e\.", "ie", "\*ie\.\*", "\*ie\*",
        "e\.g\.", "eg", "\*eg\.\*", "\*eg\*",
        "viz\.", "viz", "\*viz\.\*", "\*viz\*",
        "c\.f\.", "cf", "\*cf\.\*", "\*cf\*",
        "n\.b\.", "nb", "\*nb\.\*", "\*nb\*",
    ]

    return existence_check(text, list, err, msg, ignore_case=True)

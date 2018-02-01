# -*- coding: utf-8 -*-
"""How to construct."""

from proselint.tools import existence_check, memoize


@memoize
def check_howto(text):
    """Check how to construct."""
    err = "style-guide.check-howto"
    msg = "Avoid using \"How to\" construction."
    regex = "(How to.*)(\n)([=~\-\"\*]+)"

    return existence_check(text, [regex], err, msg, require_padding=False)


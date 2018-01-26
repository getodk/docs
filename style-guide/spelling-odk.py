# -*- coding: utf-8 -*-

"""odk spell check."""

from proselint.tools import memoize, preferred_forms_check

@memoize
def check_odkspell(text):
    """odk spell check"""
    err = "style-guide.spelling-odk"
    msg = "ODK spell check. '{}' is the preferred usage."

    preferences = [

        ["Open Data Kit",         ["Open data kit"]],
        ["Open Data Kit",         ["OpenDataKit"]],
        ["Aggregate",        	  ["{0} aggregate"]],
        ["Briefcase",             ["{0} briefcase"]],
        ["XForms",                ["Xforms"]],
        ["XForms",                ["X-Forms"]],
        ["XForms",                ["{0} xforms"]],
        ["XForms",                ["XFORMS"]],
        ["an Xform",              ["XForm"]],
        ["XLSForm",               ["{0} xlsform"]],
        ["XLSForm",               ["XLSform"]],
        ["XLSForm",               ["Xlsform"]]
    ]

    return preferred_forms_check(text, preferences, err, msg, ignore_case=False)

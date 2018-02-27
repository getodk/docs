"""Utility module to run the extra checks on docs."""
import importlib
e = importlib.import_module('style-guide.extra', None)

def check(text):
    """Run extra checks."""
    text = text.read()
    error = []
    errors = e.check_quotes(text) + e.check_curlyquotes(text)
    errors += e.check_label(text)
    errors = sorted(errors, key=lambda e: (e[2], e[3]))
    return errors

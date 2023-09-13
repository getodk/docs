import re
import mistune

def md2html(text):
    if text == None: return '<span></span>'

    return re.sub("\n", "", mistune.html(text))

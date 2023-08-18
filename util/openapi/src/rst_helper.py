import re
import mistune

def md2rs(text):
    if text == None: return '<span></span>'

    return re.sub("\n", "", mistune.html(text))

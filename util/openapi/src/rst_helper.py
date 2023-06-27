import re

def md2rs(text):
    if text == None: return ''

    r = formatVariables(text)
    r = formatItalic(r)
    r = formatBold(r)
    r = formatLinks(r)
    r = formatHeadings(r)
    return r

def formatLinks(text):
    return re.sub("\[([^\[]+)\]\(([^\(]*?)\)", "`\g<1> <\g<2>>`__", text)

# RST needs a space after the backticks
def formatVariables(text):
    return re.sub("`([^`]+)`", "``\g<1>``\ ", text)

def formatHeadings(text):
    r = re.sub("^## (.*)$", "\g<1>\n" + (120 * '^'), text,0,re.M)
    r = re.sub("^### (.*)$", "\g<1>\n" + (120 * '"'), r,0,re.M)
    return r

def formatBold(text):
    return re.sub("\*\*(.*?)\*\*", "**\g<1>**\ ", text)

def formatItalic(text):
    return re.sub("_([^_]*)_", "*\g<1>*\ ", text)

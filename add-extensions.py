import sys, os, re

# make a dict of names:extensions
img_exts = dict()

for _,_,f in os.walk("img"):
    for name in f:
        n, x = name.split(".")
        img_exts[n] = x

rst_ext = re.compile('\.rst\Z')
img_ref = re.compile('(img\/[a-z0-9\-]*\/([a-z0-9\-]*)\.)\*')

def replace_extension(m):
    extension = img_exts[m.group(2)]
    return "".join([m.group(1), extension])


for item in os.listdir("."):
    if rst_ext.search(item):
        with open(item, 'r') as file:
            filedata = file.read()

        filedata = img_ref.sub(replace_extension, filedata)

        # Write the file out again
        with open(item, 'w') as file:
            file.write(filedata)

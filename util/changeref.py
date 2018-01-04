#!/usr/bin/env python

import sys
import re
import os
import glob

old_ref_type = sys.argv[1]
old_ref = sys.argv[2]
new_ref_type = sys.argv[3]
new_ref = sys.argv[4]
old_path = sys.argv[5]
new_path =sys.argv[6]

if not all((old_ref_type, old_ref, new_ref_type, new_ref, old_path, new_path)):
    print("Not enough arguments. Exiting.")
    sys.exit()

if old_ref_type not in ["ref", "any", "doc"]:
    print("First arg not a valid ref type string.")
    sys.exit()

if new_ref_type not in ["ref", "any", "doc"]:
    print("Third arg not a valid ref type string.")
    sys.exit()  

redirect = "  %s: %s\n" %(old_path, new_path)

with open('s3_website.yml', 'a') as file:
    file.write(redirect)

ref_pattern = re.compile(r':((ref)|(doc)|(any)):`([^<`\n]*)<?([^>`\n]*)>?`')
    # group 1 : ref, doc, any (reference type)
    # group 5 : if 6 is empty, 5 is reference target; else 5 is anchor text
    # group 6 : if not empty, reference target


def updated_ref(matchobj):
    current_ref_type = matchobj.group(1)
    if current_ref_type != old_ref_type:
        return matchobj.group(0)
    if matchobj.group(6):
        current_ref = matchobj.group(6)
        current_anchor_text = matchobj.group(5)
    if not matchobj.group(6):
        current_ref = matchobj.group(5)
        current_anchor_text = ""
    if current_ref != old_ref:
        return matchobj.group(0)

    if current_anchor_text:
        replacement = ':{}:`{} <{}>`'.format(
            new_ref_type, current_anchor_text, new_ref
        )
    else:
        replacement = ':{}:`{}`'.format(
            new_ref_type, new_ref
        )

    print("Replacing: \n - ", matchobj.group(0), "\n + ", replacement)
    return replacement
    


for f in glob.glob('*.rst'): 
    with open(f, 'r') as file :
      filedata = file.read()

    # Replace the target string
    filedata = re.sub(ref_pattern, updated_ref, filedata)

    # Write the file out again
    with open(f, 'w') as file:
      file.write(filedata)



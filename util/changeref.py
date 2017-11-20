#!/usr/bin/env python

import sys
import re
import os
import glob

old_ref_type = sys.argv[1]
old_ref = sys.argv[2]
new_ref_type = sys.argv[3]
new_ref = sys.argv[4]

ref_pattern = re.compile(r':((ref)|(doc)|(any)):`([^<`\n]*)<?([^>`\n]*)>?`')
    # group 1 : ref, doc, any (reference type)
    # group 5 : if 6 is empty, 5 is reference target; else 5 is anchor text
    # group 6 : if not empty, reference target


def updated_ref(matchobj):
    current_ref_type = matchobj[1]
    if current_ref_type != old_ref_type:
        return matchobj[0]
    if matchobj[6]:
        current_ref = matchobj[6]
        current_anchor_text = matchobj[5]
    if not matchobj[6]:
        current_ref = matchobj[5]
    if current_ref != old_ref:
        return matchobj[0]

    if current_anchor_text:
        return f":{new_ref_type}:`{current_anchor_text} <{new_ref}>`"
    return f":{new_ref-type}:`{new-ref}`"
    


for f in glob.glob('*.rst'): 
    with open(f, 'r') as file :
      filedata = file.read()

    # Replace the target string
    filedata = re.sub(ref_pattern, updated_ref, filedata)

    # Write the file out again
    with open(f, 'w') as file:
      file.write(filedata)

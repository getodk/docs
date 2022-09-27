#!/env/python3

import os
import sys
import glob

if len(sys.argv) < 2:
    exit(0)

path = str(sys.argv[1])
spellings = glob.glob(path + '/**/*.spelling', recursive=True)
if spellings:
    print("Spell check failed")
    for spelling in spellings:
        os.system("cat " + spelling)
    exit(1)
# sphinx-spellcheck raises a warning because it conflicts with sphinx-tabs
# so we have to suppress warnings in circleci
# but that suppresses warnings related to misspellings.
# So this script checks the spellcheck output
# and raises an exception if there are any.
import os
import sys

class SpellingError(ValueError):
    pass

if len(sys.argv) < 2:
    raise ValueError("The parent directory of the spelling directory is a required argument")

build_dir = sys.argv[1]
spelling_dir = "spelling"
output_file = "output.txt"

output_path = os.path.join(build_dir, spelling_dir, output_file)

try:
    assert os.stat(output_path).st_size == 0   
except AssertionError:
    with open(output_path, 'r') as f:
        print(f.read())
        raise SpellingError("You have spelling errors.") from AssertionError
else:
    print("No spelling errors caught.")

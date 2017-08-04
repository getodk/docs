import os
import subprocess
import sys

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def screencap():
    return subprocess.check_output("adb exec-out screencap -p", shell=True)

def save_screencap(cap, filename):
    with open(filename, 'wb') as f:
        f.write(cap)

if __name__ == "__main__":
    short_filename = sys.argv[1]
    filename = '_static/img/' + short_filename + '.png'
    ensure_dir(filename)
    save_screencap(screencap(), filename)
    print("Insert image into doc with:")
    print(".. image:: /img/" + short_filename + ".*")
    print("  :alt: Alt text here. Be sure to add alt text.")
    print("")
    print("")
    print("See http://docs.opendatakit.org/contributing.html#images-and-figures for more details.")







# adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > screen.png

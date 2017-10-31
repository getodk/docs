#!/usr/bin/env python

import os
import subprocess
import sys
import PIL.Image
import PIL.ImageCms
import tempfile

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def screencap():
    return subprocess.check_output("adb exec-out screencap -p", shell=True)

def save_screencap(cap, filename):
    with open(filename, 'wb') as f:
        f.write(cap)

def convert_profile(filename):
    img = PIL.Image.open(filename)
    icc = tempfile.mkstemp(suffix='.icc')[1]
    if 'icc_profile' in img.info:
        with open(icc, 'wb') as f:
            f.write(img.info['icc_profile'])
        srgb = PIL.ImageCms.createProfile('sRGB')
        img = PIL.ImageCms.profileToProfile(img, icc, srgb)
    img.save(filename)

if __name__ == "__main__":
    short_filename = sys.argv[1]
    filename = 'img/' + short_filename + '.png'
    ensure_dir(filename)
    save_screencap(screencap(), filename)
    convert_profile(filename)
    if sys.argv[2] != '-s':
        print("Insert image into doc with:")
        print(".. image:: /img/" + short_filename + ".*")
        print("  :alt: Alt text here. Be sure to add alt text.")
        print("")
        print("")
        print("Use the figure directive to add a caption:")
        print(".. figure:: /img/" + short_filename + ".*")
        print("  :alt: Alt text here. Be sure to add alt text.")
        print("")
        print("  The caption is here.")
        print("")
        print("")
        print("See http://docs.opendatakit.org/contributing/#images-and-figures for more details.")

# -*- coding: UTF-8 -*-
from mutagen.id3 import ID3, APIC, ID3NoHeaderError
from PIL import Image
import io
import os
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('files', nargs='+',  help='fix cover audio file')

args = parser.parse_args()

APIC_KEY = 'APIC:'
PROGRAM_DIR_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
CURRENT_DIR_PATH = os.getcwd()
INPUT_FILES = args.files


def fix(filepath):
    try:
        audio = ID3(filepath)
        if APIC_KEY not in audio.keys():
            print(f"skip: {filepath}")
            return
        image_data = audio[APIC_KEY].data
        image = Image.open(io.BytesIO(image_data))
        with io.BytesIO() as output:
            image.save(output, format=image.format)
            audio.delall(APIC_KEY)
            audio[APIC_KEY] = APIC(
                type=3,
                mime=Image.MIME[image.format],
                data=output.getvalue(),
            )
            audio.save()
        print(f"fix: {filepath}")
    except ID3NoHeaderError as e:
        print(e)
        print(f"ignore: {filepath}")


def fix_files(files, parent_dir):
    for file in files:
        path = os.path.join(parent_dir, file)
        if os.path.isfile(path):
            fix(path)
            continue
        if os.path.isdir(path):
            fix_files(os.listdir(path), path)


if __name__ == '__main__':
    fix_files(INPUT_FILES, CURRENT_DIR_PATH)

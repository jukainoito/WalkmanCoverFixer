# -*- coding: UTF-8 -*-
import os
import sys
import argparse
import mimetypes
from fixer import fix


parser = argparse.ArgumentParser()
parser.add_argument('files', nargs='+',  help='fix cover audio file')

args = parser.parse_args()

PROGRAM_DIR_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
CURRENT_DIR_PATH = os.getcwd()
INPUT_FILES = args.files


def fix_files(files, parent_dir):
    for file in files:
        path = os.path.join(parent_dir, file)
        if os.path.isfile(path):
            mimetype, subtype = mimetypes.guess_type(path)
            fix(path, mimetype)
            continue
        if os.path.isdir(path):
            fix_files(os.listdir(path), path)


if __name__ == '__main__':
    fix_files(INPUT_FILES, CURRENT_DIR_PATH)

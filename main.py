# -*- coding: UTF-8 -*-
import os
import sys
import argparse
import mimetypes
from fixer import fix


parser = argparse.ArgumentParser()
parser.add_argument('-cover', '--cover', help='if audio file no have cover then add default cover image')
parser.add_argument('files', nargs='+',  help='fix cover audio file')

args = parser.parse_args()

PROGRAM_DIR_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
CURRENT_DIR_PATH = os.getcwd()
INPUT_FILES = args.files
DEFAULT_COVER_FILE = args.cover
DEFAULT_COVER_FILE_PATH = None
if DEFAULT_COVER_FILE is not None:
    DEFAULT_COVER_FILE_PATH = os.path.join(CURRENT_DIR_PATH, DEFAULT_COVER_FILE)


def get_mimetype(filepath):
    try:
        import magic
        return magic.from_file(filepath, mime=True)
    except ImportError:
        mimetype, subtype = mimetypes.guess_type(filepath)
        return mimetype


def fix_files(files, parent_dir):
    for file in files:
        path = os.path.join(parent_dir, file)
        if os.path.isfile(path):
            mimetype = get_mimetype(path)
            fix(path, mimetype, DEFAULT_COVER_FILE_PATH)
            continue
        if os.path.isdir(path):
            fix_files(os.listdir(path), path)


if __name__ == '__main__':
    fix_files(INPUT_FILES, CURRENT_DIR_PATH)

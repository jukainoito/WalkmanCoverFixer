# -*- coding: UTF-8 -*-

from .flac import FlacFixer
from .id3 import ID3Fixer


def fix(filepath, mimetype: str):
    if mimetype.find('flac'):
        fixer = FlacFixer()
    else:
        fixer = ID3Fixer()
    fixer.fix(filepath)

# -*- coding: UTF-8 -*-
import re
from .flac import FlacFixer
from .id3 import ID3Fixer
from .mp4 import MP4Fixer


def fix(filepath, mimetype: str):
    if re.search('flac', mimetype, re.IGNORECASE):
        fixer = FlacFixer()
    # elif re.search('(m4a|mp4)', mimetype, re.IGNORECASE):
    #     fixer = MP4Fixer()
    else:
        fixer = ID3Fixer()
    fixer.fix(filepath)

# -*- coding: UTF-8 -*-
import abc
from typing import Optional
from PIL import Image
import io


def fix_image(image_data) -> Optional[tuple[bytes, str]]:
    with io.BytesIO() as output:
        image = Image.open(io.BytesIO(image_data))
        image.save(output, format=image.format)
        return output.getvalue(), Image.MIME[image.format]


class Fixer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def fix(self, filepath):
        pass


def singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton

from .common import Fixer, fix_image, singleton
from mutagen.mp4 import MP4


COVER_KEY = 'covr'


@singleton
class MP4Fixer(Fixer):

    def fix(self, filepath):
        try:
            audio = MP4(filepath)
            if COVER_KEY not in audio.tags.keys() or len(audio.tags[COVER_KEY]) == 0:
                print(f'skip: {filepath}')
                return
            image_data = audio[COVER_KEY][0]
            fixed_image_data, mimetype = fix_image(image_data)
            if fixed_image_data is not None:
                audio[COVER_KEY] = [
                    fixed_image_data
                ]
                audio.save()
            print(f'fix: {filepath}')
        except Exception as e:
            print(f'ignore: {filepath} -- {e}')

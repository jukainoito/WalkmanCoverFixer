from .common import Fixer, fix_image, singleton
from mutagen.flac import FLAC, Picture


@singleton
class FlacFixer(Fixer):

    def fix(self, filepath):
        try:
            audio = FLAC(filepath)
            if len(audio.pictures) == 0:
                print(f'skip: {filepath}')
                return
            image_data = audio.pictures[0].data
            fixed_image_data, mimetype = fix_image(image_data)
            if fixed_image_data is not None:
                audio.clear_pictures()

                pic = Picture()
                pic.type = 3
                pic.mime = mimetype
                pic.colors = 0
                pic.data = fixed_image_data

                audio.add_picture(pic)

                audio.save()
            print(f'fix: {filepath}')
        except Exception as e:
            print(f'ignore: {filepath} -- {e}')

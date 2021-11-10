from .common import Fixer, fix_image, singleton
from mutagen.flac import FLAC, Picture
import traceback

@singleton
class FlacFixer(Fixer):

    def fix(self, filepath):
        try:
            audio = FLAC(filepath)
            image_data = None
            if len(audio.pictures) == 0:
                if self.cover is None:
                    print(f'skip: {filepath}')
                    return
                else:
                    image_data = self.cover
            image_data = audio.pictures[0].data if image_data is None else image_data
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
            traceback.print_exc()
            print(f'ignore: {filepath} -- {e}')

from .common import Fixer, fix_image, singleton
from mutagen.id3 import ID3, APIC, ID3NoHeaderError


APIC_KEY = 'APIC:'


@singleton
class ID3Fixer(Fixer):

    def fix(self, filepath):
        try:
            audio = ID3(filepath)
            if APIC_KEY not in audio.keys():
                print(f'skip: {filepath}')
                return
            image_data = audio[APIC_KEY].data
            fixed_image_data, mimetype = fix_image(image_data)
            if fixed_image_data is not None:
                audio.delall(APIC_KEY)
                audio[APIC_KEY] = APIC(
                    type=3,
                    mime=mimetype,
                    data=fixed_image_data,
                )
                audio.save()
            print(f'fix: {filepath}')
        except ID3NoHeaderError as e:
            print(f'ignore: {filepath} -- {e}')

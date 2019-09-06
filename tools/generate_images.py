from pathlib import Path

import utils


def main():
    repository_path = Path.cwd().parent
    cut_path = repository_path / 'CUT'
    img_path = repository_path / 'PUDR' / 'IMG'
    png_path = repository_path / 'PNG'

    if not img_path.exists():
        img_path.mkdir()

    if not png_path.exists():
        png_path.mkdir()

    for file_path in cut_path.glob('*.CUT'):
        short_name = file_path.stem
        img_file_path = (img_path / short_name).with_suffix('.IMG')
        png_file_path = (png_path / short_name).with_suffix('.PNG')

        cut_reader = utils.CutReader(file_path)
        cut_reader.write_img(img_file_path)
        cut_reader.write_png(png_file_path)


if __name__ == '__main__':
    main()

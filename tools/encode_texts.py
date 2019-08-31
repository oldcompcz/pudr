# -*- coding: utf-8 -*-

"""Script to encode all texts in the game."""

import logging


def translation_table():
    """Return a translation table combining two mappings:

    - Czech letters with diacritics mapped to chars '\xc0'..'\xdd'
    - ascii chars '\x20'..'\x7d' mapped to their value XORed by 1
    """
    translation_dict = dict(zip('ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽáčďéěíňóřšťúůýž',
                            map(chr, range(0xc0, 0xde))))

    translation_dict.update({chr(n): chr(n ^ 1) for n in range(0x20, 0x7e)})

    return str.maketrans(translation_dict)


def wrap_to_27(item):
    """Wrap input item to the width of 27 characters."""

    if '_' in item:
        for line in item.split('_'):
            yield line
        return

    while len(item) > 27 and ' ' in item:

        split_position = item[:28].rfind(' ')

        if item[:split_position].endswith((' k', ' s', ' v', ' z')):
            split_position -= 2

        line = item[:split_position]
        item = item[split_position + 1:]

        yield line.strip()

    yield item.strip()


def main():
    # logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    logging.basicConfig(level=logging.WARN, format='%(message)s')

    trans_table = translation_table()

    for filename in ('TEXTY.TXT', 'VECI.TXT'):

        with open('UTF8_{}'.format(filename), mode='r',
                  encoding='utf-8') as input_file,                            \
             open('/home/michal/dos/PUDR/PUDR/{}'.format(filename), mode='w',
                  encoding='latin-1', newline='\r\n') as output_file:

            item_lines = []

            for input_line in input_file:

                if not input_line.startswith(('!', '~')):
                    # normal line - part of current text item
                    item_lines.extend(wrap_to_27(input_line.rstrip()))

                else:
                    # special line - end of current text item
                    if item_lines:
                        print(*item_lines, '-' * 27, sep='\n')

                        output = '_'.join(item_lines)
                        output_file.write(output.translate(trans_table) + '\n')

                        item_lines = []

                    if input_line.startswith('~'):
                        # line not to be encoded
                        output_file.write(input_line[1:])


if __name__ == '__main__':
    main()

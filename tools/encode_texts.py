# -*- coding: utf-8 -*-

"""Script to encode all texts in the game."""

import logging

import data


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
    max_len = 128 - 4 - 3

    with open('/home/michal/dos/PUDR/PUDR/DATA.PAS', mode='w',
              encoding='latin1', newline='\r\n') as f:


        for section in data.texts:
            section_name = next(iter(section))
            section_texts = section[section_name]

            print('{}: array[0..{}] of string[{}] = ('
                  .format(section_name, len(section_texts) - 1,
                          max(len(t) for t in section_texts)),
                  file=f)

            output = []

            for item in section_texts:
                if isinstance(item, list):
                    output_line = ''.join(chr(n + 48) for n in item)
                else:
                    wrapped = list(wrap_to_27(item))
                    output_line = '_'.join(wrapped).translate(trans_table)

                output.append('    \'{}\''.format(output_line))

            print(',\n'.join(output), file=f)
            print('\n);\n', file=f)



if __name__ == '__main__':
    main()

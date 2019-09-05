# -*- coding: utf-8 -*-

import logging
import re
import unicodedata


def translation_table():
    """Return a translation table combining two mappings:

       - Czech letters with diacritics mapped to chars '\xc0'..'\xdd'
       - ascii chars '\x20'..'\x7d' mapped to their value XORed by 1
    """
    translation_dict = dict(zip('ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽáčďéěíňóřšťúůýž',
                                map(chr, range(0xc0, 0xde))))

    translation_dict.update({chr(n): chr(n ^ 1) for n in range(0x20, 0x7e)})

    return str.maketrans(translation_dict)


def wrap_text(item, width=27):
    """Wrap input item to the width of `width` characters."""

    if '_' in item:
        for line in item.split('_'):
            yield line
        return

    while len(item) > width and ' ' in item:

        split_position = item[:width + 1].rfind(' ')

        if item[:split_position].endswith((' k', ' s', ' v', ' z')):
            split_position -= 2

        line = item[:split_position]
        item = item[split_position + 1:]

        yield line.strip()

    yield item.strip()


def strip_diacritics(input_string: str) -> str:
    """Return a copy of `input_string` without diacritics, such that
       strip_diacritics('skříň') == 'skrin'
    """
    trans_dict = {}

    for char in input_string:
        if ord(char) < 0x80:
            continue

        match_letter = re.match(r'LATIN (?P<case>CAPITAL|SMALL) LETTER (?P<letter>\w)',
                                unicodedata.name(char))

        if match_letter:
            trans_dict[char] = (match_letter.groupdict()['letter'].lower()
                                if match_letter.groupdict()['case'] == 'SMALL'
                                else match_letter.groupdict()['letter'])

    trans_table = str.maketrans(trans_dict)
    return input_string.translate(trans_table)


def strip_diacritics_2(input_string: str) -> str:
    """Return a copy of `input_string` without diacritics, such that
       strip_diacritics('skříň') == 'skrin'
    """
    trans_dict = {char: int(unicodedata.decomposition(char).split()[0],
                            base=16)
                  for char in input_string
                  if ord(char) > 0x7f}

    trans_table = str.maketrans(trans_dict)
    return input_string.translate(trans_table)


def code_pairs(char_sequence):
    """Generate tuples containing diacritics & letter codes for each
       char in `char_sequence`.
    """
    for char in char_sequence:

        unicode_info = [unicodedata.name(char).split()[i] for i in (1, 3, 5)]

        if unicode_info[0] == 'SMALL':
            letter = unicode_info[1].lower()
            diacritic = unicode_info[2].lower()
        else:
            letter = unicode_info[1]
            diacritic = unicode_info[2]

        logging.debug('{}: {} with {} ---> '.format(char, letter, diacritic))

        letter_code = 1 + 'ACDEINORSTUYZacdeinorstuyz'.index(letter)

        if char == 'ď':
            # special case
            diacritic_code = 6
        else:
            diacritic_code = ['ACUTE', 'CARON', 'RING',
                              'acute', 'caron', 'ring'].index(diacritic)

        yield diacritic_code, letter_code


def combine_from_pair(bit_765, bit_43210):
    """Store diacritics code (values 0-6) & letter code (values 1-26)
       in one byte-sized code.
    """

    code = (bit_765 << 5) + bit_43210
    logging.debug('{:3b} {:5b} ---> {:#x}'.format(bit_765, bit_43210, code))

    return code


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# -*- coding: utf-8 -*-

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

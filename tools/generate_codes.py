"""Script to generate codes used for decoding and displaying Czech
   characters by the `decode_and_write` Pascal procedure.
"""
import unicodedata


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

        print('{}: {} with {} ---> '.format(char, letter, diacritic), end='')

        letter_code = 1 + 'ACDEINORSTUYZacdeinorstuyz'.index(letter)

        if char == 'ď':
            # special case
            diacritic_code = 6
        else:
            diacritic_code = ['ACUTE', 'CARON', 'RING',
                              'acute', 'caron', 'ring'].index(diacritic)

        yield diacritic_code, letter_code


def combine_from_pair(bit_765, bit_43210):

    code = (bit_765 << 5) + bit_43210
    print('{:3b} {:5b} ---> {:#x}'.format(bit_765, bit_43210, code))

    return code


def main():
    czech_chars = 'ÁČĎÉĚÍŇÓŘŠŤÚŮÝŽáčďéěíňóřšťúůýž'

    codes = (combine_from_pair(diacritic, letter)
             for diacritic, letter in code_pairs(czech_chars))

    code_strings = ('${:02x}'.format(code) for code in codes)

    with open('../PUDR/KODY.PAS', 'w') as f:
        print('{generated by tools/generate_codes.py}\n', file=f)

        print(',\n'.join(code_strings), file=f)


if __name__ == '__main__':
    main()

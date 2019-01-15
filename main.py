#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import permutations
"""
Molecules Assessment
"""

_author_ = "bomazani, davidstewy, with mob-coding assistance"


molecules_to_check = """CDBADCBBEFEF
DACCBADAFEAB
EFBDCAADBDCD
ABCDABCDABCD
DACCBADAFEAB
EFBDCAADBDCD
ABCDABCDABCD
CDBADCBBEFEF
ABABABABABAB
CDCDCDCDCDCD
EEEEEEEEEEEE
FFFFFFFFFFFF
ABAAAAAAAABA
CBCCCCCCCCBC
DBDDDDDDDDBD
EBEEEEEEEEBE
ABBBBBBBBBBA
ACCCCCCCCCCA
ADDDDDDDDDDA
AEEEEEEEEEEA
BBBABBBABBBB
CCACCCACCCCC
DDDDADDADDDD
EEAEEAEEEEEE
Q"""


def grab_molecule(molecules_to_split):
    """Splits given string into list of list with 4 strings each"""
    molecules = []
    molecules_to_split = molecules_to_split.split('\n')
    while molecules_to_split:
        molecules.append(molecules_to_split[:4])
        molecules_to_split = molecules_to_split[4:]
    return molecules


def rectangle_tuples(molecules_to_check):
    """Builds our possible rectangle dimensions based on string length"""
    str_length = len(molecules_to_check[0])
    pairs = [(w, h) for w in range(2, (str_length - 1))
             for h in range(w, (str_length - 1))]
    pairs.sort(
        key=lambda str_length: str_length[0] * str_length[1], reverse=True)
    return pairs


def best_fit(w, h, across1, down1, across2, down2):
    """
    Tries to fit a rectangle into a set of 4 molecule strings
    returns true if a fit is found.
    """
    for a1 in range(1, 12 - (w + 1)):
        for d1 in range(1, 12 - (h + 1)):
            if across1[a1] != down1[d1]:
                continue
            for a2 in range(1, 12 - (w + 1)):
                if across2[a2] != down1[d1 + (h + 1)]:
                    continue
                for d2 in range(1, 12 - (h + 1)):
                    if down2[d2] != across1[a1 + (w + 1)]:
                        continue
                    if down2[d2 + (h + 1)] == across2[a2 + (w + 1)]:
                        return True
    return False


def main():
    molecules_strings = grab_molecule(molecules_to_check)
    rectangle_dimensions = rectangle_tuples(molecules_strings[0])
    for molecule_strings in molecules_strings:
        answer = 0
        """Builds a list of all possible string permutations for molecule"""
        molecules_variations = list(permutations(molecule_strings))
        for w, h in rectangle_dimensions:
            if answer == 1:
                break
            for molecule_var in molecules_variations:
                if best_fit(w, h, *molecule_var):
                    # print 'Tested Molecule: {}'.format(molecule_strings)
                    print(w * h)
                    answer = 1
                    break
        if answer == 0:
            # print 'Tested Molecule: {}'.format(molecule_strings)
            print 0


if __name__ == '__main__':
    main()

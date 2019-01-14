#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import permutations
"""
Molecules Assessment
"""

_author_ = "bomazani, Stew, with mob-coding assistance"


molecules_to_check = ['CDBADCBBEFEF', 'DACCBADAFEAB',
                      'EFBDCAADBDCD', 'ABCDABCDABCD',
                      'DACCBADAFEAB', 'EFBDCAADBDCD',
                      'ABCDABCDABCD', 'CDBADCBBEFEF',
                      'ABABABABABAB', 'CDCDCDCDCDCD',
                      'EEEEEEEEEEEE', 'FFFFFFFFFFFF',
                      'ABAAAAAAAABA', 'CBCCCCCCCCBC',
                      'DBDDDDDDDDBD', 'EBEEEEEEEEBE',
                      'ABBBBBBBBBBA', 'ACCCCCCCCCCA',
                      'ADDDDDDDDDDA', 'AEEEEEEEEEEA',
                      'BBBABBBABBBB', 'CCACCCACCCCC',
                      'DDDDADDADDDD', 'EEAEEAEEEEEE',
                      'Q']


def grab_molecule(molecules_to_check):
    molecules = []
    while molecules_to_check:
        molecules.append(molecules_to_check[:4])
        molecules_to_check = molecules_to_check[4:]
    return molecules


def rectangle_tuples(molecules_to_check):
    str_length = len(molecules_to_check[0])
    pairs = [(w, h) for w in range(2, (str_length - 1))
             for h in range(w, (str_length - 1))]
    pairs.sort(
        key=lambda str_length: str_length[0] * str_length[1], reverse=True)
    return pairs


def best_fit(w, h, across1, down1, across2, down2):
    """ Tries to fit a rectangle into a set of 4 molecule strings returns true if a fit is found"""
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
    # print molecules_strings
    rectangle_dimensions = rectangle_tuples(molecules_to_check)
    # print(rectangle_dimensions)

    for molecule_strings in molecules_strings:
        answer = 0
        molecules_variations = list(permutations(molecule_strings))
        # print(molecules_variations)
        for w, h in rectangle_dimensions:
            if answer == 1:
                break
            for molecule_var in molecules_variations:
                if best_fit(w, h, *molecule_var):
                    print molecule_strings
                    print(w * h)
                    answer = 1
                    break
                else:
                    continue
        if answer == 0:
            print molecule_strings
            print 0
# across1, down1, across2, down2


if __name__ == '__main__':
    main()

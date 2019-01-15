#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import permutations
"""
Molecules Assessment
"""

_author_ = "bomazani, davidstewy, with mob-coding assistance"


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

def grab_molecule(molecules_to_split):

    molecules = []
    molecules_to_split = molecules_to_split.split('\n')
    while molecules_to_split:
        molecules.append(molecules_to_split[:4])
        molecules_to_split = molecules_to_split[4:]
    return molecules


def grab_molecule(molecules_to_check):
    # Pulls molecule (4 strings) from the list of strings.
    print('Grabbing molecule')
    molecule_list = []
    molecule = []
    print('molecule = {}'.format(molecule))
    for i in range(0, 4):
        if molecules_to_check[0] == 'Q':
            print('End of molecules.')
            print('molecule_list = {}'.format(molecule_list))
            return molecule_list
        molecule.append(molecules_to_check.pop(0))
        print('molecule = {}'.format(molecule))
        molecule_list.append(molecule)


def rectangle_tuples(molecules_to_check):
    # Generates list of (h, W) tuples. Runs once.
    str_length = len(molecules_to_check[0])
    pairs = [(w, h) for w in range(2, (str_length - 1))
             for h in range(w, (str_length - 1))]
    pairs.sort(
        key=lambda str_length: str_length[0] * str_length[1], reverse=True)
    return pairs


def best_fit(w, h, across1, down1, across2, down2):
    """ Tries to fit a set of 4 molecule strings around a rectangle.
     Returns true if a fit is found.
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
    rectangle_dimensions = rectangle_tuples(molecules_to_check)
    for molecule_strings in molecules_strings:
        answer = 0
        molecules_variations = list(permutations(molecule_strings))
        print('molecules_variations = {}'.format(molecules_variations))

        for w, h in rectangle_dimensions:
            print('Rectangle: w = {}, h={}'.format(w, h))
            if answer == 1:
                break
            for molecule in molecules_variations:
                print('molecule = {}'.format(molecule))
                if best_fit(w, h, *molecule):
                    print(molecule_strings)
                    print('area = {}'.format(w * h))
                    answer = 1
                    break
                else:
                    print('continuing')
                    continue
        if answer == 0:
            print(molecule_strings)
            print('0')


# across1, down1, across2, down2


if __name__ == '__main__':
    main()

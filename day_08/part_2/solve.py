import itertools
from copy import deepcopy
import numpy as np


def read_data():
    with open("example.txt") as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data = [line.split(" | ") for line in data]
        data = [[entry.split(" ") for entry in line] for line in data]

    return data


data = read_data()

identity_mapping = {
    0: [0, 0, 0, 0, 0, 0, 0],
    1: [0, 0, 1, 0, 0, 1, 0],
    2: [1, 0, 1, 1, 1, 0, 1],
    3: [1, 0, 1, 1, 0, 1, 1],
    4: [0, 1, 1, 1, 0, 1, 0],
    5: [1, 1, 0, 1, 0, 1, 1],
    6: [1, 1, 0, 1, 1, 1, 1],
    7: [1, 0, 1, 0, 0, 1, 0],
    8: [1, 1, 1, 1, 1, 1, 1],
}

value_mapping = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7
}

letter_mapping = {v: k for k, v in value_mapping.items()}


def impose_identity_mapping(permutations, value_mapping, identity_mapping, number):
    valid = []

    for permutation in permutations:
        identity = deepcopy(identity_mapping[number])

        for char in permutation:
            for i, num in enumerate(identity):
                if num == 0:
                    continue

                if num == 1:
                    identity[i] = value_mapping[char]
                    break

        valid.append(identity)

    return valid


def discard_invalid(possibilities, permutation_mapping, digit):
    indices_to_remove = []

    for i, possibility in enumerate(possibilities):
        valid = False

        for permutation in permutation_mapping[digit]:
            matches = []

            for j, number in enumerate(permutation):
                if number == 0:
                    matches.append(True)
                    continue

                if number != possibility[j]:
                    matches.append(False)

            if all(matches):
                #print("Valid:", digit, possibility, permutation)
                valid = True

        if not valid:
            indices_to_remove.append(i)

    # print("")

    possibilities = [x for i, x in enumerate(
        possibilities) if i not in indices_to_remove]

    return possibilities


for line in data:
    input_values = line[0]
    output_values = line[1]

    mapping = {
        1: [[char for char in x] for x in input_values if len(x) == 2][0],
        4: [[char for char in x] for x in input_values if len(x) == 4][0],
        7: [[char for char in x] for x in input_values if len(x) == 3][0],
        8: [[char for char in x] for x in input_values if len(x) == 7][0],
    }

    permutation_mapping = {
        k: impose_identity_mapping(list(itertools.permutations(
            mapping[k])), value_mapping, identity_mapping, k)
        for k in [1, 4, 7, 8]
    }

    possibilities = permutation_mapping[8]

    possibilities = np.unique(discard_invalid(
        possibilities, permutation_mapping, 1), axis=0)

    possibilities = np.unique(discard_invalid(
        possibilities, permutation_mapping, 4), axis=0)

    possibilities = np.unique(discard_invalid(
        possibilities, permutation_mapping, 7), axis=0)

    print(len(possibilities))
    for line in possibilities:
        print(line)

    # for line in possibilities:
    #     print("".join([letter_mapping[k] for k in line]))

    # print(len(possibilities))

    print("")

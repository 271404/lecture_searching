import os
import json

from Lecture_09.lecture_searching.generators import dna_sequence

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r") as json_file:
        seq = json.load(json_file)
    return seq

def linear_search(seq, number):
    """
    :return: (dict): {'position': <list of indices>, 'count': <total count>,}
    """
    indicies = []
    count = 0

    idx = 0
    while idx < len(seq):
        if seq[idx] == number:
            indicies.append(idx)
            count += 1
        idx += 1

    return {"positions": indicies,
            "count": count,
            }


def pattern_search(sequence, pattern):
    positions = set()
    pattern_length = len(pattern)
    sequence_length = len(sequence)

    for i in range(sequence_length - pattern_length + 1):
        match = True
        for j in range(pattern_length):
            if sequence(i + j) != pattern(j):
                match = False
                break
        if match:
            positions.add(i)
    return positions

def pattern_search1(sequence, pattern):
    indicies = set()
    pattern_size = len(pattern)

    left_idx = 0
    right_idx = pattern_size
    while right_idx < len(sequence):
        for idx in range(pattern_size):
            if pattern[idx] != sequence[left_idx + idx]:
                break
        else:
            indicies.add(left_idx + pattern_size //2)

        left_idx += 1
        right_idx += 1

    return indicies

def binary_search(seq, number):
    left = 0
    right = len(seq) - 1
    while left <= right:
        middle = (left + right) // 2
        if seq(middle) == number:



def main():
    file_name = "sequential.json"

    #read data
    seq = read_data(file_name, field="unordered_numbers") #musime prepsat field
    print(seq)

    #linear search
    search = linear_search(seq, number=0)
    print(search)

    #read data
    sequence = read_data(file_name, field="dna_sequence")
    pattern = 'ATA'

    #pattern search
    matches = pattern_search(sequence, pattern)
    print(f"vzor nalezen na pozicich: {sorted(matches)}")

    #read data
    seq = read_data(file_name, field='ordered_numbers')

    #paa
    number_pos = binary_search(seq, number=14)

if __name__ == '__main__':
    main()
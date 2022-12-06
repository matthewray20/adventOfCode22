#!/usr/bin/env python3

import numpy as np


FILENAME = 'rucksack_items.txt'


def bin_priorities(priority_bin, compartment):
    for item in compartment:
        priority_bin[ord(item) - 96 if item.islower() else ord(item) - (64-26)] += 1
    return priority_bin


def part1():
    priority_sum = 0
    with open(FILENAME, 'r') as f:
        for rucksack in f:
            rucksack = rucksack.strip()
            length = len(rucksack)        
            compartment1, compartment2 = list(set(rucksack[:length//2])), list(set(rucksack[length//2:]))
            priority_bin = np.zeros(55)
            priority_bin = bin_priorities(priority_bin, compartment1)
            priority_bin = bin_priorities(priority_bin, compartment2)
            priority_sum += np.argmax(priority_bin)

    print(priority_sum)


def part2():
    priority_sum = 0
    with open(FILENAME, 'r') as f:
        i = 0
        group_members = []
        for rucksack in f:
            group_members.append(rucksack.strip())
            if i == 2:
                priority_bin = np.zeros(53)
                priority_bin = bin_priorities(priority_bin, list(set(group_members[0])))
                priority_bin = bin_priorities(priority_bin, list(set(group_members[1])))
                priority_bin = bin_priorities(priority_bin, list(set(group_members[2])))
                priority_sum += np.argmax(priority_bin)
                group_members = []
            i = (i + 1) % 3

    print(priority_sum)






if __name__ == "__main__":
    part1()
    part2()
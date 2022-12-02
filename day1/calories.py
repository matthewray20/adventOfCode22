#!/usr/bin/env python3

FILENAME = 'calorie_data.txt'

def part1():
    elvesCalorieCount = [0]
    with open(FILENAME, 'r') as f:
        for line in f:
            line = line.strip('\n')
            if line.isnumeric():
                elvesCalorieCount[-1] += int(line)
            elif line == '':
                elvesCalorieCount.append(0)
            else:
                print(f'Unexpected line characters: "{line}"')

    return elvesCalorieCount

def part2(elvesCalorieCount):
    sortedCalories = sorted(elvesCalorieCount)
    top3 = sum(sortedCalories[-3:])
    return top3


if __name__ == '__main__':
    elvesCalorieCount = part1()
    print(f'The most calories carried by an elf are: {max(elvesCalorieCount)}')
    top3 = part2(elvesCalorieCount)
    print(f'The sum of the top 3 elves calories is: {top3}')


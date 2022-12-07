#!/Users/mattray/miniconda3/bin python

INITIAL_POSITIONS = 'crates_initial_config.txt'
MOVEMENTS = 'rearrangement_steps.txt'


def initial_loader():
    stacks = []
    with open(INITIAL_POSITIONS, 'r') as f:
        for line in f:
            line = line.strip()
            stacks.append(line.split(','))
    return stacks


def part1():
    stacks = initial_loader()
    with open(MOVEMENTS, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.replace(' ', '').replace('move', '').replace('from', ',').replace('to', ',')
            movement = line.split(',')
            movement = [int(info) for info in movement]
            for i in range(movement[0]):
                crate = stacks[movement[1]-1].pop()
                stacks[movement[2]-1].append(crate)
    final_positions = ''.join([stack[-1] for stack in stacks])
    print(final_positions)


def part2():
    stacks = initial_loader()
    with open(MOVEMENTS, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.replace(' ', '').replace('move', '').replace('from', ',').replace('to', ',')
            movement = line.split(',')
            movement = [int(info) for info in movement]
            stacks[movement[2]-1] += stacks[movement[1]-1][-movement[0]:]
            stacks[movement[1]-1] = stacks[movement[1]-1][:-movement[0]]
    print(stacks)
    final_positions = ''.join([stack[-1]for stack in stacks if len(stack) > 0])
    print(final_positions)





if __name__ == "__main__":
    part1()
    part2()

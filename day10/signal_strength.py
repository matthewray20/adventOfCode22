#!/Users/mattray/miniconda3/bin python


FILENAME = 'cpu_instructions.txt'




def part1():
    timestamps_to_measure = [20, 60, 100, 140, 180, 220]
    registor = 1
    timestamp = 0
    signal_strengths = []
    with open(FILENAME, 'r') as f:
        for line in f:
            line = line.strip()
            instruction = line[:4]
            to_add = 0
            if instruction == 'noop':
                timestamp += 1
            elif instruction == 'addx':
                to_add = int(line[5:])
                timestamp += 1
                if timestamp in timestamps_to_measure: signal_strengths.append((timestamp, registor, timestamp * registor))
                timestamp += 1
            if timestamp in timestamps_to_measure: signal_strengths.append((timestamp, registor, timestamp * registor))
            registor += to_add
    print(signal_strengths)
    print(sum([x[2] for x in signal_strengths]))






def part2():
    with open(FILENAME, 'r') as f:
        output_str = ''
        timestamp = -1
        registor = 1
        for line in f:
            line = line.strip()
            instruction = line[:4]
            if instruction == 'noop':
                to_add = 0
            elif instruction == 'addx':
                to_add = int(line[5:]) 
                timestamp += 1
                pixel_x = timestamp % 40
                if pixel_x == 0:
                    output_str += '\n'
                output_str += '#' if pixel_x in [x for x in range(registor-1, registor+2)] else '.'
            timestamp += 1
            pixel_x = timestamp % 40
            if pixel_x == 0:
                print('new line:', timestamp)
                output_str += '\n'
            output_str += '#' if pixel_x in [x for x in range(registor-1, registor+2)] else '.'
            registor += to_add
    print(output_str)
    lens = output_str.split()
    for d in lens:
        print(len(d))





if __name__ == "__main__":
    part1()
    part2()

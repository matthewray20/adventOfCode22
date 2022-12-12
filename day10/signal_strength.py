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





class CPU:
    def __init__(self):
        self.timestamp = 0
        self.registor = 1
        self.output_str = ''
    
    def cycle(self):
        self.print_pixel()
        self.timestamp += 1
    
    def noop(self):
        self.cycle()

    def addx(self, x):
        self.cycle()
        self.cycle()
        self.registor += x

    def print_pixel(self):
        sprite_pos = [self.registor - 1, self.registor, self.registor + 1]
        pixel_x = self.timestamp % 40
        if pixel_x == 0:
            self.output_str += '\n'
        if pixel_x in sprite_pos:
            self.output_str += '#'
        else:
            self.output_str += '.'
    
    def end(self):
        print(self.output_str)





def part2():
    processor = CPU()
    with open(FILENAME, 'r') as f:
        output_str = ''
        timestamp = -1
        registor = 1
        for line in f:
            line = line.strip()
            instruction = line[:4]
            if instruction == 'noop':
                processor.noop()
            elif instruction == 'addx':
                to_add = int(line[5:])
                processor.addx(to_add)
        processor.end()
        # EGJEGCFK






if __name__ == "__main__":
    part1()
    part2()

#!/Users/mattray/miniconda3/bin python


FILENAME = 'test.txt'


class Knot:
    def __init__(self, n):
        self.absolute_x = 0
        self.absolute_y = 0
        self.number = n
        self.tail = None
        self.locations_visited = []
    
    def add_tail(self):
        self.tail = Knot(self.number + 1)
    
    def print_all_pos(self):
        print(f'Knot: {self.number}, x: {self.absolute_x}, y: {self.absolute_y}')
        if self.tail is not None:
            self.tail.print_all_pos()
        else:
            print('-------------------------')
            
    def move(self, direction):
        if direction == 'U': # move up
            self.absolute_y += 1
            print(f'{self.number} moving U')
        elif direction == 'D': # move down
            self.absolute_y -= 1
            print(f'{self.number} moving D')
        elif direction == 'L': # move left
            self.absolute_x -= 1
            print(f'{self.number} moving L')
        elif direction == 'R': # move right
            self.absolute_x += 1
            print(f'{self.number} moving R')
        else:
            print(f"Somethign wrong unexpected input: {direction}")
        
        if self.tail is not None:
            self.tail.update_tail(self.absolute_x, self.absolute_y)

    def update_tail(self, head_x, head_y):
        # relative x -> -1 means head is 1 space left of tail (tail want to move left)
        # relative x -> 1 means head is 1 space right of tail (tail want to move right)
        relative_x = head_x - self.absolute_x
        relative_y = head_y - self.absolute_y

        if relative_x == 0 and relative_y > 1: # move up
            self.move('U')
        elif relative_x == 0 and relative_y < -1: # move down
            self.move('D')
        elif relative_y == 0 and relative_x > 1: # move right
            self.move('R')
        elif relative_y == 0 and relative_x < -1: # move left
            self.move('L')
        elif relative_x >= 1 and relative_y > 1 or relative_x > 1 and relative_y >= 1: # move diag up right
            self.move('U')
            self.move('R')
        elif relative_x >= 1 and relative_y < -1 or relative_x > 1 and relative_y <= -1: # move diag down right
            self.move('D')
            self.move('R')
        elif relative_x <= -1 and relative_y < -1 or relative_x < -1 and relative_y <= -1: # move diag down left
            self.move('D')
            self.move('L')
        elif relative_x <= -1 and relative_y > 1 or relative_x < -1 and relative_y >= 1: # move diag up left
            self.move('U')
            self.move('L')
        else:
            #print(f"touching should lead here! Rel x: {relative_x}, rel y: {relative_y}")
            pass
        self.locations_visited.append((self.absolute_x, self.absolute_y))
    
    def end(self, n):
        if self.number == n:
            print(len(set(self.locations_visited)))
        else:
            self.tail.end(n)

            

def part1():
    head = Knot(0)
    current = head
    for i in range(1, 10):
        current.add_tail()
        current = current.tail
    with open(FILENAME, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(' ')
            n = int(line[1])
            for _ in range(n):
                direction = line[0]
                head.move(direction)
                head.print_all_pos()
            print()
    head.end(9)














def part2():
    pass








if __name__ == "__main__":
    part1()
    part2()
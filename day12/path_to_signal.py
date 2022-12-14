#!/Users/mattray/miniconda3/bin python


FILENAME = 'hightmap.txt'



class Node:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.f = None
        self.g = None
        self.h = None
        self.parent = None
    
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col and self.value == other.value
    
        

class AStar:
    def __init__(self):
        self.open_list = []
        self.closed_list = []


    def get_node_lowest_f(self):
        # only called when len(self.open_list) > 0
        best_node = self.open_list[0]
        #print('possible_nodes:', [a_node.value for a_node in self.open_list])
        for a_node in self.open_list:
            if a_node.f < best_node.f:
                best_node = a_node
        self.open_list.remove(best_node)
        self.closed_list.append(best_node)
        #print('best node:', best_node.value, best_node.row, best_node.col)
        return best_node


    @staticmethod
    def get_sucessors(current):
        global length, height_map
        sucessors = []
        if current.row > 0: # up
            #print('up')
            sucessors.append(height_map[current.row - 1][current.col])
        if current.row < length - 1: # down
            #print('up')
            sucessors.append(height_map[current.row + 1][current.col])
        if current.col > 0: # left
            #print('left')
            sucessors.append(height_map[current.row][current.col - 1])
        if current.col < length - 1: #right
            #print('right')
            sucessors.append(height_map[current.row][current.col + 1])

        for sucessor in sucessors:
            sucessor.update(current)
            print('compare:', sucessor.value, current.value)
            if sucessor.value > current.value + 1:
                print('nope')
                print()
                sucessors.remove(sucessor)
                #print('removing:', sucessor.value, current.value + 1)

        #print('found:', len(sucessors), 'sucessors')
        return sucessors


    def find_path(self, root):
        global goal_row, goal_col
        self.open_list.append(root)
        while len(self.open_list) > 0:
            q = self.get_node_lowest_f()
            if q.col > 3:
                print('OMGjndvjndsvjnsvd')
            q_sucessors = self.get_sucessors(q)
            for sucessor in q_sucessors:
                if sucessor.row == goal_row and sucessor.col == goal_col: # found goal
                    return sucessor.f
                
                sucessor.g = q.g + 1
                sucessor.h = abs(sucessor.row - goal_row) + abs(sucessor.col - goal_col)
                sucessor.f = sucessor.g + sucessor.h
                for closed_node in self.closed_list:
                    if sucessor == closed_node:
                        continue
                
                for open_node in self.open_list:
                    if sucessor == open_node and sucessor.g > open_node.g:
                        continue
                
                self.open_list.append(sucessor)

        print('didnt work')
        return -1


def part1():
    global height_map
    global length
    global goal_row, goal_col
    start_row, start_col = None, None
    goal_row, goal_col = None, None
    with open(FILENAME, 'r') as f:
        height_map = []
        # converting string height map to Node with int value and finding goal and start locations
        for n, line in enumerate(f):
            line = line.strip()
            # 'S' becomes -13, 'E' becomes -27
            new_line = [ord(n)-96 for n in line]
            # 'S' now 0, 'E' now 27
            if -13 in new_line:
                new_line[new_line.index(-13)] = 0
                # set start position
                start_row = n
                start_col = new_line.index(0)
            if -27 in new_line:
                new_line[new_line.index(-27)] = 27
                # set goal position
                goal_row = n
                goal_col = new_line.index(27)
            
            height_map.append([Node(n, new_line.index(x), x) for x in new_line])
    length = len(height_map)
    if start_row is not None and start_col is not None and goal_row is not None and goal_col is not None:
        root = height_map[start_row][start_col]
        root.f = 0
        root.g = 0
        print('start', root.value, start_row, start_col)
        path_finder = AStar()
        path_length = path_finder.find_path(root)
        print(path_length)








if __name__ == '__main__':
    part1()

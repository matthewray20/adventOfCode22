#!/Users/mattray/miniconda3/bin python



FILENAME = 'filesystem_commands.txt'


class Directory:
    def __init__(self, name, parent):
        self.files = {}
        self.size = None
        self.parent = parent
    
    def __setitem__(self, key, value):
        self.files[key] = value

    def __contains__(self, other):
        return other in self.files
    
    def __getitem__(self, key):
        return self.files[key]
    

class File:
    def __init__(self, size, name):
        self.name = name
        self.size = size
        

def calc_size(current):
    count = 0
    for item_name in current.files:
        item = current[item_name]
        if isinstance(item, File):
            count += item.size
        elif isinstance(item, Directory):
            size = calc_size(item)
            item.size = size
            count += size
            global directory_count
            if size <= 100000: directory_count += size
        else:
            Exception(f'type: {type(item)} is not valid. Must be File or Directory')
    return count



def part1():
    global directory_count
    directory_count = 0
    with open(FILENAME, 'r') as f:
        root = Directory('/', None)
        next(f)
        i = 1
        current = root
        previous = root
        for line in f:
            i += 1
            line = line.strip()

            if line == "$ cd /":
                current = root
            elif line == "$ cd ..":
                current = current.parent
            elif line[:4] == "$ cd":
                the_dir = line[5:]
                assert the_dir in current
                current = current[the_dir]
            elif line == "$ ls":
                continue
            elif line[:3] == "dir":
                dirname = line[4:]
                if not dirname in current:
                    current[dirname] = Directory(dirname, current)
            elif line[0].isnumeric():
                size, filename = line.split()
                if not filename in current:
                    current[filename] = File(int(size), filename)
            else:
                Exception(f'Unrecognised command: {line}')
            
    # then calc dirs size recursively
    calc_size(root)
    print(directory_count)    



def part2():
    pass

if __name__ == "__main__":
    part1()
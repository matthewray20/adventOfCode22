#!//Users/mattray/miniconda3/bin python

class Assignment:
    def __init__(self, assignment_range):
        assignment_range = assignment_range.split('-')
        self.min = int(assignment_range[0])
        self.max = int(assignment_range[1])
    
    def __contains__(self, other):
        return self.min <= other.min and self.max >= other.max

    def overlaps(self, other):
        return self.min <= other.min and self.max >= other.min or self.max >= other.max and self.min <= other.max



def part1():
    overlap_count = 0
    with open(FILENAME, 'r') as f:
        for group in f:
            group = group.strip().split(',')
            assignment1, assignment2 = Assignment(group[0]), Assignment(group[1])
            if assignment1 in assignment2 or assignment2 in assignment1: overlap_count += 1 
    print(overlap_count)



def part2():
    overlap_count = 0
    with open(FILENAME, 'r') as f:
        for group in f:
            group = group.strip().split(',')
            assignment1, assignment2 = Assignment(group[0]), Assignment(group[1])
            if assignment1.overlaps(assignment2) or assignment2.overlaps(assignment1): overlap_count += 1 
    print(overlap_count)



if __name__ == "__main__":
    FILENAME = 'assignment_pairs.txt'
    part1()
    part2()
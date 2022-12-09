#!/Users/mattray/miniconda3/bin python


FILENAME = 'tree_heights_map.txt'



def part1():
    
    trees = []
    with open(FILENAME, 'r') as f:
        for line in f:
            line = line.strip()
            line = [int(i) for i in line]
            trees.append(line)

    length = len(trees[0])
    visibility_count = 4 * length - 4
    for row in range(1, length-1):
        for col in range(1, length-1):
            tree = trees[row][col]
            # looking each diretion
            rightmax = max(trees[row][col+1:])
            leftmax = max(trees[row][:col])
            upmax = max([x[col] for x in trees[:row]])
            downmax = max([y[col] for y in trees[row+1:]])
            if tree > rightmax or tree > leftmax or tree > upmax or tree > downmax: 
                visibility_count += 1
            
    print(visibility_count)



def dist_to_blocking(tree, othertrees):
    for i, othertree in enumerate(othertrees):
        if othertree >= tree:
            return i+1
    return len(othertrees)


def part2():
    trees = []
    with open(FILENAME, 'r') as f:
        for line in f:
            line = line.strip()
            line = [int(i) for i in line]
            trees.append(line)
    
    length = len(trees[0])
    visibility_best_score = 0
    for row in range(1, length-1):
        for col in range(1, length-1):
            tree = trees[row][col]

            # tree directions 
            righttrees = trees[row][col+1:]
            lefttrees = trees[row][:col]
            uptrees = [x[col] for x in trees[:row]]
            downtrees = [y[col] for y in trees[row+1:]]
            
            # blocking tree distance
            rightdist = dist_to_blocking(tree, righttrees)
            leftdist = dist_to_blocking(tree, [i for i in reversed(lefttrees)])
            updist = dist_to_blocking(tree, [j for j in reversed(uptrees)])
            downdist = dist_to_blocking(tree, downtrees)

            # calc score
            score = leftdist * rightdist * updist * downdist
            if score > visibility_best_score:
                visibility_best_score = score

            
            
    print(visibility_best_score)





if __name__ == "__main__":
    part1()
    part2()
                

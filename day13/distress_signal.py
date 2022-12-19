#!/Users/mattray/miniconda3/bin/ python

import json

FILENAME = 'packet_pairs.txt'
#FILENAME = 'test.txt'


def is_right_order(left, right, depth):
    # recursive comparison 
    if isinstance(left, list) and isinstance(right, list):
        #print('\t' * depth, f'- compare {left} vs {right}')
        left_len, right_len = len(left), len(right)
        for subleft, subright in zip(left, right):
            check = is_right_order(subleft, subright, depth + 1)
            if check is not None:
                return check
        #print('\t' * depth, f'left_len: {left_len}, right_len: {right_len}')
        if left_len < right_len:
            return True
        elif right_len < left_len:
            return False
    elif isinstance(left, int) and isinstance(right, int):
        #print('\t' * depth, f'- INT compare {left} vs {right}')
        if left < right:
            #print('return True')
            return True
        elif right < left:
            #print('return False')
            return False
    elif isinstance(left, int) and isinstance(right, list):
        #print('\t' * depth, f'mismatched left types')
        return is_right_order([left], right, depth+1)
    elif isinstance(left, list) and isinstance(right, int):
        #print('\t' * depth, f'mismatched right types')
        return is_right_order(left, [right], depth+1)
    else:
        print('UNKOWN INPUT PAIRS')
        #print("left:", left, type(left))
        #print("right:", right, type(right))



def part1():
    all_packets = []
    packet = []
    with open(FILENAME, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line == '':
                all_packets.append(packet)
                packet = []
            else:
                j = json.loads(line)
                packet.append(j)
    count = 0
    for i, pair in enumerate(all_packets):
        if is_right_order(pair[0], pair[1], 0): 
            print('#############', i+1)
            count += (i + 1)
        print('\n')
    print(count)



def bubble_sort(packets):
    length = len(packets)
    any_false = True
    while any_false:
        any_false = False
        for i in range(1, length):
            print('comparing', packets[i-1], packets[i])
            if not is_right_order(packets[i-1], packets[i], 0):
                tmp = packets[i]
                packets[i] = packets[i-1]
                packets[i-1] = tmp
                any_false = True
        print()
        print_packs(packets)
        print('going')
    return packets


def print_packs(packets):
    for pa in packets:
        print(pa)


def part2():
    all_packets = []
    with open(FILENAME, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            else:
                j = json.loads(line)
                all_packets.append(j)
    divider1 = [[2]]
    divider2 = [[6]]
    all_packets.append(divider1)
    all_packets.append(divider2)
    print('length of packets:', len(all_packets))
    print_packs(all_packets)
    print('---------------------------starting sorting---------------------')
    sorted_packets = bubble_sort(all_packets)
    locator1 = sorted_packets.index(divider1) + 1
    locator2 = sorted_packets.index(divider2) + 1
    print(locator1, locator2, locator1 * locator2)



if __name__ == "__main__":
    part1()
    part2()
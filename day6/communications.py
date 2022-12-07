#!/Users/mattray/miniconda3/bin python

FILENAME = 'datastream_buffer.txt'


def dataloader():
    with open(FILENAME, 'r') as f:
        data = f.readline()
    return data

def marker_detector(data, marker_length):
    length = len(data)
    assert length > marker_length, f"marker length ({marker_length}) cannot be longer than data stream ({length})"
    for i in range(marker_length, length):
        if len(set(data[i-(marker_length-1):i+1])) == marker_length:
            return(i+1)



def part1():
    data = dataloader()
    result = marker_detector(data, 4)
    print(result)
    


def part2():
    data = dataloader()
    result = marker_detector(data, 14)
    print(result)







if __name__ == "__main__":
    part1()
    part2()

def read_input(input):
    with open(input) as file:
        file_str = file.read()
        data = file_str.rstrip().split(',')
        data = [int(datum) for datum in data]
        if sorted:
            data.sort()
    return data

def median(list):
    len_list = len(list)
    index = (len_list - 1) // 2
    if (len_list % 2):
        return list[index]
    else:
        return (list[index] + list[index + 1]) // 2.0


def part1(input):
    data = read_input(input)
    mid = median(data)
    diffs = [abs(datum - mid) for datum in data]
    return sum(diffs)

def part2(input):
    data = read_input(input)
    mean = int(sum(data)/len(data))
    diffs = [abs(datum - mean) for datum in data]
    tris = [triangle_number(diff) for diff in diffs]
    return sum(tris)

def triangle_number(n):
    num = 0
    for i in range(1, n + 1):
        num += i
    return num


if __name__ == "__main__":
    p1 = part1('sample.txt')
    p2 = part2('input.txt')

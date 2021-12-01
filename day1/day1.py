test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def part1(data):
    counter = count_inc(data)
    print(counter)

def part2(data):
    grouped = group_measurements(data)
    print(count_inc(grouped))


def import_input():
    with open('input.txt') as file:
        lines = file.readlines()
        lines = [int(line.rstrip()) for line in lines]
    return lines

def is_inc(prev, curr):
    if curr > prev:
        return True
    else:
        return False

def count_inc(data):
    counter = 0
    for i in range(0, len(data) - 1):
        prev = data[i]
        curr = data[i+1]
        if is_inc(prev, curr):
            counter += 1
    return counter

def group_measurements(data):
    group_data = []
    for i in range(2, len(data)):
        grouped = data[i] + data[i-1] + data[i-2]
        group_data.append(grouped)
    return group_data





if __name__ == "__main__":
    data = import_input()
    part1(data)
    part2(data)

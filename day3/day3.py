from statistics import mode, multimode

def input_to_list(input):
    with open(input) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        return lines

input = input_to_list('input.txt')
sample = [
        '00100', 
        '11110', 
        '10110', 
        '10111', 
        '10101', 
        '01111', 
        '00111', 
        '11100', 
        '10000', 
        '11001', 
        '00010', 
        '01010', 
        ]
 

def part1(data):
    sets = get_common_sets(data)
    gamma = get_mode(sets)
    epsilon = get_epsilon(gamma)
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(gamma * epsilon)

def part2(data):
    o2 = get_o2(data)
    co2 = get_co2(data)
    o2 = int(o2, 2)
    co2 = int(co2, 2)
    print(o2 * co2)


def get_common_sets(data):
    sets = []
    for line in data:
        for i in range(0, len(line)):
            try:
                sets[i].append(line[i])
            except:
                sets.append([line[i]])

    return sets

def get_mode(sets):
    str_n = ""
    for list in sets:
        str_n += str(mode(list))
    return str_n

def get_epsilon(gamma):
    epsilon = ""
    for i in gamma:
        if i == '1':
            epsilon += '0'
        else:
            epsilon += '1'
    return epsilon

def get_common_digit(data, n):
    digits = []
    for line in data :
        digits.append(line[n])
    commons = multimode(digits)
    if len(commons) == 1:
        return commons[0]
    else:
        return '1'


def get_uncommon_digit(data, n):
    digits = []
    for line in data :
        digits.append(line[n])
    commons = multimode(digits)
    if len(commons) == 1:
        if commons[0] == '1':
            return '0'
        else:
            return '1'
    else:
        return '0'


def drop_digits(data, n, common):
    new_data = []
    for line in data:
        if line[n] == common:
            new_data.append(line)
    return new_data

def get_o2(data):
    for i in range(0, len(data[0])):
        common = get_common_digit(data, i)
        data = drop_digits(data, i, common)
    return data[0]


def get_co2(data):
    for i in range(0, len(data[0])):
        common = get_uncommon_digit(data, i)
        data = drop_digits(data, i, common)
        if len(data) == 1:
            return data[0]
    return data[0]


if __name__ == "__main__":
    part1(input)
    part2(input)


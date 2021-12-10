def read_input(input):
    with open(input) as file:
        lines = file.readlines()
        lines = [list(line.rstrip()) for line in lines]
        lines = [[int(n) for n in line] for line in lines]
    return lines

def lowest(n, lst):
    checks_count = 0
    for item in lst:
        if n < item:
            checks_count += 1
    if checks_count == len(lst): 
        return True
    else:
        return False

def part1(input, p2 = False):
    data = read_input(input)
    low_points = []
    #for part2
    low_ids = []
    for row in range(0, len(data)):
        for i in range(0, len(data[row])):
            top = 10
            bot = 10
            left = 10
            right = 10
            if row != 0:
                top = data[row -1 ][i]
            if row != len(data):
                try:
                    bot = data[row + 1 ][i]
                except:
                    pass
            if i != 0:
                left = data[row][i - 1]
            if i != len(data[row]):
                try:
                    right = data[row][i +1]
                except:
                    pass
            if lowest(data[row][i], [top, bot, left, right]):
                low_points.append(data[row][i])
                low_ids.append((i, row))
    if p2:
        return low_ids
    risks = [i+1 for i in low_points]
    return sum(risks)


def expand_basin(data, start, basin_set):
    basin_set = basin_set | {start}
    if start[1] == 0:
        up = None
    else:
        up = (start[0], start[1] - 1)
    if start[1] == len(data) -1:
        down = None
    else:
        down = (start[0], start[1] + 1)
    if start[0] == 0:
        left = None
    else:
        left = (start[0] - 1, start[1])
    if start[0] == len(data[start[1]]) -1:
        right = None
    else:
        right = (start[0] + 1, start[1])
    if up and up not in basin_set:
        up_val = resolve_coord(data, up)
        if up_val == 9:
            pass
        else:
             pass
             basin_set = basin_set | expand_basin(data, up, basin_set)
    if down and down not in basin_set:
        down_val = resolve_coord(data, down)
        if down_val == 9:
            pass
        else:
             pass
             basin_set = basin_set | expand_basin(data, down, basin_set)
    if right and right not in basin_set:
        right_val = resolve_coord(data, right)
        if right_val == 9:
            pass
        else:
             pass
             basin_set = basin_set | expand_basin(data, right, basin_set)
    if left and left not in basin_set:
        left_val = resolve_coord(data, left)
        if left_val == 9:
            pass
        else:
             pass
             basin_set = basin_set | expand_basin(data, left, basin_set)
    return basin_set




def resolve_coord(data, coord):
    return data[coord[1]][coord[0]]






def part2(input):
    data = read_input(input)
    low_ids = part1(input, p2 = True)
    #basin_sets = [get_basin_size(data, coord) for coord in low_ids]
    basin_sets = [expand_basin(data, coord, set()) for coord in low_ids]
    sizes = [len(basin) for basin in basin_sets]
    larges = []
    for _ in range(3):
        largest = max(sizes)
        larges.append(largest)
        sizes.remove(largest)
    return larges[0] * larges[1] * larges[2]





if __name__ == "__main__":
    #p1 = part1('sample.txt')
    p2 = part2('sample.txt')
    a = [[1,2,9], [2,2,9], [9,2,3]]
    b = expand_basin(a, (0,0), set())

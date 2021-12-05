def read_input(input):
    with open(input) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines
    
def convert_data(data):
    data = [line.split(' -> ') for line in data]
    data = [[point.split(',') for point in line] for line in data]
    return data 

def get_h_v_lines(data):
    h_lines = []
    v_lines = []
    for line in data:
        if line[0][0] == line[1][0]:
            h_lines.append(line)
        elif line[0][1] == line[1][1]:
            v_lines.append(line)
    return {'h': h_lines, 'v': v_lines}

def get_points(hv):
    points = {}
    for line in hv['h']:
        new_points = []
        r_min = min(int(line[0][1]), int(line[1][1]))
        r_max = max(int(line[0][1]), int(line[1][1])) + 1
        for i in range(r_min,r_max):
            point = (line[0][0],  str(i))
            new_points.append(point)
        for point in new_points:
            point_not = str(point[0]) + ',' + str(point[1])
            if point_not in points.keys():
                points[point_not].inc_count()
            else:
                points[point_not] = Point(point)
    for line in hv['v']:
        new_points = []
        r_min = min(int(line[0][0]), int(line[1][0]))
        r_max = max(int(line[0][0]), int(line[1][0])) + 1
        for i in range(r_min,r_max):
            point = (str(i), line[0][1])
            new_points.append(point)
        for point in new_points:
            point_not = str(point[0]) + ',' + str(point[1])
            if point_not in points.keys():
                points[point_not].inc_count()
            else:
                points[point_not] = Point(point)
    return points

def find_multipoints(points):
    counter = 0
    for point in points.values():
        if point.count > 1:
            counter += 1
    return counter

def get_points_p2(lines):
    points = {}
    for line in lines:
        print(line)
        new_points = []
        first_point = (int(line[0][0]), int(line[0][1]))
        second_point = (int(line[1][0]), int(line[1][1]))
        p1 = None
        p2 = None
        if first_point[0] < second_point[0]:
            p1 = first_point
            p2 = second_point
        else:
            p1 = second_point
            p2 = first_point
        try:
            slope = (p2[1]-p1[1]) / (p2[0] - p1[0])
            if slope == 0:
                print("slope 0")
                r_min = min(int(line[0][0]), int(line[1][0]))
                r_max = max(int(line[0][0]), int(line[1][0]))
                for i in range(r_min,r_max + 1):
                    point = (i,int(line[0][1]))
                    new_points.append(point)
            elif slope > 0: 
                print("slow > 0")
                p = p1

                while p  != p2:
                    new_points.append(( p[0],p[1] ))
                    p = (p[0]+1, p[1]+1)
                new_points.append((int(p2[0]),int(p2[1])))

            elif slope < 0: 
                print('slope < 0')
                p = p1
                while p != p2:
                    new_points.append(( p[0],p[1] ))
                    p = (p[0]+1, p[1]-1)
                new_points.append((int(p2[0]),int(p2[1])))

        except ZeroDivisionError:
            print('vertical')
            r_min = min(int(line[0][1]), int(line[1][1]))
            r_max = max(int(line[0][1]), int(line[1][1]))
            print('min: ' + str(r_min))
            print('max: ' + str(r_max))
            print(range(r_min, r_max +1))
            for i in range(r_min,r_max + 1):
                point = (int(line[0][0]), i )
                new_points.append(point)
        for point in new_points:
            point_not = str(point[0]) + ',' + str(point[1])
            if point_not in points.keys():
                points[point_not].inc_count()
            else:
                points[point_not] = Point(point)
    return points

        
    
def part1(input):
    data = convert_data(read_input(input))
    hv = get_h_v_lines(data)
    points = get_points(hv)
    counter = find_multipoints(points)

    return counter

def part2(input):
    data = convert_data(read_input(input))
    points = get_points_p2(data)
    #return points
    counter = find_multipoints(points)
    return counter



class Point:
    def __init__(self, point):
        self.x = point[0]
        self.y = point[1] 
        self.count = 1

    def inc_count(self):
        self.count += 1
    
    def print_count(self):
        print("({},{}: {})".format(self.x, self.y, self.count))


if __name__ == "__main__":
    p1 = part1('sample.txt')
    p2 = part2('sample.txt')

def input_to_list(input):
    with open(input) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        return lines

input = input_to_list('input.txt')
sample = [
        "forward 5"
        , "down 5"
        , "forward 8"
        , "up 3"
        , "down 8"
        , "forward 2"
        ]

 

def part1(data):
    horizontal = 0
    depth = 0
    for line in data:
        split = line.split(' ')
        if split[0] == "forward":
            horizontal += int(split[1])
        elif split[0] == "down":
            depth += int(split[1])
        else:
            depth -= int(split[1])
    print("Part1")
    print("horizontal: " + str(horizontal))
    print("depth: " + str(depth))
    print(horizontal * depth)
    print("------------------------------")




def part2(data):
    sub = Sub()
    for line in data:
        sub.read_command(line)
    print("Part2")
    sub.get_stats()



class Sub:
    def __init__(self):
        self.horizontal = 0
        self.aim = 0
        self.depth = 0

    def read_command(self, com):
        split = com.split (' ')
        if split[0] == 'down':
            self.aim += int(split[1])
        elif split[0] == 'up':
            self.aim -= int(split[1])
        else:
            self.horizontal += int(split[1])
            self.depth += (int(split[1]) * self.aim)

    def get_stats(self):
        print("horizontal: " + str(self.horizontal))
        print("aim: " + str(self.aim))
        print("depth: " + str(self.depth))
        print(self.horizontal * self.depth)


if __name__ == "__main__":
    part1(input)
    part2(input)

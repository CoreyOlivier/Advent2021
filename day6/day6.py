def read_input(input):
    with open(input) as file:
        file_str = file.read()
        data = file_str.rstrip().split(',')
    return data

class LanternFish:
    def __init__(self, timer = 9):
        self.timer = timer
    
    def increment_timer(self):
        if self.timer == 0:
            self.timer = 6
            return LanternFish()
        else:
            self.timer -= 1
    def __repr__(self):
        return str(self.timer)

    
    
def part1(input, days):
    data = read_input(input)
    fishies = []
    for datum in data:
        fishies.append(LanternFish(timer = int(datum)))
    for _ in range(days):
        for fish in fishies:
            new = fish.increment_timer()
            if new:
                fishies.append(new)

    return fishies

def part2_day(fishies):
    new_fishies = {
            '0':0, 
            '1':0, 
            '2':0, 
            '3':0, 
            '4':0, 
            '5':0, 
            '6':0, 
            '7':0, 
            '8':0, 
            }
    for k, v in fishies.items():
        if k == '0':
            new_k = '6'
            new_fishies[new_k] += v
            new_fishies['8'] += v
        else:
            new_k = str(int(k)-1)
            new_fishies[new_k] += v
    return new_fishies

    


def part2(input, days):
    data = read_input(input)
    fishies = {
            '0':0, 
            '1':0, 
            '2':0, 
            '3':0, 
            '4':0, 
            '5':0, 
            '6':0, 
            '7':0, 
            '8':0, 
            }
    for datum in data:
        fishies[str(datum)] += 1
           
    for _ in range(days):
        fishies = part2_day(fishies)

    return fishies


if __name__ == "__main__":
    p1 = part1('sample.txt', 10)
    p2 = part2('sample.txt', 18)

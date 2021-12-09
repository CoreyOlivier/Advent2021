def read_input(input):
    with open(input) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        lines = [line.split( ' | ' ) for line in lines]
        lines = [(line[0].split(' '), line[1].split(' ')) for line in lines]
    return lines



def part1(input):
    data = read_input(input)
    unique_len = [2, 4, 3, 7]
    counter = 0
    for datum in data:
        for code in datum[1]:
            if len(code) in unique_len:
                counter += 1

    return counter

class Display:
    def __init__(self, data):
        self.signals = data[0]
        self.output = data[1]
        self.num_codes = {}
        self.len_5 = []
        self.len_6 = []
        for signal in self.signals:
            if len(signal) == 2:
                self.num_codes['1'] = signal
            elif len(signal) == 3:
                self.num_codes['7'] = signal
            elif len(signal) == 4:
                self.num_codes['4'] = signal
            elif len(signal) == 7:
                self.num_codes['8'] = signal
            elif len(signal) == 5:
                self.len_5.append(signal)
            elif len(signal) == 6:
                self.len_6.append(signal)
        self.find_numbers()
        self.value = self.get_value()
        
    def get_value(self):
        value = []
        for digit in self.output:
            for num, code in self.num_codes.items():
                if set(digit) == set(code):
                    value.append(num)
        return int(''.join(value))


    

    def find_numbers(self):
        common_lines = []
        semi_common = []
        uncommon_lines = []
        possibles = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        combined = ''.join(self.len_5)
        for letter in possibles:
            count = combined.count(letter)
            if count == 1:
                uncommon_lines.append(letter)
            elif count == 2:
                semi_common.append(letter)
            else:
                common_lines.append(letter)

        for letter in uncommon_lines:
            if letter in self.num_codes['4']:
                for code in self.len_5:
                    if letter in code:
                        self.num_codes['5'] = code
                        self.len_5.remove(code)
            else:
                for code in self.len_5:
                    if letter in code:
                        self.num_codes['2'] = code
                        self.len_5.remove(code)
                    for c in self.len_6:
                        if letter not in c:
                            self.num_codes['9' ] = c
                            self.len_6.remove(c)
        self.num_codes['3'] = self.len_5[0]
        
        for letter in semi_common:
            if letter in self.num_codes['2']:
                for code in self.len_6:
                    if letter not in code:
                        self.num_codes['6'] = code
                        self.len_6.remove(code)
        self.num_codes['0'] = self.len_6[0]




def part2(input):
    data = read_input(input)
    displays = [Display(datum) for datum in data]
    outputs = [display.value for display in displays]
    return sum(outputs)


if __name__ == "__main__":
    p1 = part1('sample.txt')
    p2 = part2('sample.txt')
    td = Display(read_input('test.txt')[0])

def read_input(input):
    with open(input) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


class Line:
    def __init__(self, data_str):
        self.data = data_str
        self.corrupt = False
        self.chunk_tracker = []
        self.corrupted_chars = []
        self.chunk_matcher = {')':'(', ']':'[', '}':'{', '>':'<'}
        self.completion = []

    def set_corrupt(self, val):
        self.corrupt = val

    def dec_tracker(self, char):
        match = self.chunk_matcher[char]
        if self.chunk_tracker[-1] == match:
            self.chunk_tracker.pop( -1 )
        else:
            self.set_corrupt(True)
            self.corrupted_chars.append(char)

    def update_tracker(self, char):
        if char in self.chunk_matcher.values():
            self.chunk_tracker.append(char)
        else:
            self.dec_tracker(char)

    def check_corruption(self):
        for char in self.data:
            self.update_tracker(char)
    
    def __repr__(self):
        return self.data
    
    def score_p1(self):
        scoring = {')': 3, ']': 57, '}': 1197, '>': 25137}
        if self.corrupt:
            return scoring[self.corrupted_chars[0]]
    def complete(self):
        match = {'(': ')', '[': ']', '{':'}','<': '>'}
        for _ in range(len(self.chunk_tracker)):
            self.completion.append(match[self.chunk_tracker.pop(-1)])
    def score_p2(self):
        self.complete()
        scoring = {')': 1, ']': 2, '}': 3, '>': 4}
        scores = [scoring[char] for char in self.completion]
        final_score = 0
        for score in scores:
            final_score = final_score *5
            final_score += score
        return final_score



def run(input,  part):
    data = read_input(input)
    lines = [Line(datum) for datum in data]
    scores = []
    for line in lines:
        line.check_corruption()
        if line.corrupt:
            if part ==1:
                scores.append(line.score_p1())
        else:
            if part == 2:
                scores.append(line.score_p2())

    if part == 1:
        return sum(scores)
    scores.sort()
    return scores[int(len(scores)/2)]


        

    if part == 1:
        return sum(scores)




if __name__ == "__main__":
    d = read_input('sample.txt')
    p1 = run('sample.txt', 1)
    p2 = run('sample.txt', 2)

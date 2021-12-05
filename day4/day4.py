import re
#11760 --low
#22275 --high

def read_input(input):
    with open(input) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def convert_input(input):
    data = read_input(input)
    marks = data[0]
    data = data[2:]
    data = [i for i in data if i]
    boards_data = list(chunks(data,5))
    boards = []
    for i, board in enumerate(boards_data):
        boards.append(BingoCard(board, i))
    return marks, boards

def chunks(data, n):
    for i in range(0, len(data), n):
        yield data[i:i+n]


def part1(input):
    marks, boards = convert_input(input)
    marks = marks.split(',')
    for mark in marks:
        for board in boards:
            board.mark(mark)
            if board.check_marks():
                print(board.check_score(mark))
                return board, mark

    return boards, ''

def part2(input):
    marks, boards = convert_input(input)
    marks = marks.split(',')
    for mark in marks:
        if len(boards) > 1:
            for board in boards:
                board.mark(mark)
            for i, board in enumerate(boards):
                if board.check_marks():
                    boards.pop(i)
        boards[0].mark(mark)
        if boards[0].check_marks():
            print(boards[0].check_score(mark))
            return boards[0], mark
    return boards, ''

def test_card(card, marks):
    for mark in marks:
        print(mark)
        card.mark(mark)


class BingoCard:
    def __init__(self, data, i):
        self.rows = self._process_data(data)
        self.id = i
        self.marked = []
        self.tiles = []
        self._make_tiles()

    def _make_tiles(self):
        for i, row in enumerate(self.rows):
            for j, num in enumerate(row):
                self.tiles.append(CardTile(num, i, j))

    def _process_data(self, data):
        data = [datum.strip() for datum in data]
        data = [re.sub("  +", " ", datum) for datum in data ]
        data = [datum.split(' ') for datum in data]
        return data

    def _tiles_to_rows(self):
        for i in range(0, len(self.tiles), 5):
            yield self.tiles[i:i +5]

    def _get_marks(self):
        marks = []
        for tile in self.tiles:
            if tile.is_marked():
                marks.append(tile.is_marked())

        return marks

    def print_card(self):
        tile_rows = list(self._tiles_to_rows())
        for row in tile_rows:
            print(row)


    def mark(self, num):
        for tile in self.tiles:
            if tile.mark(num):
                return True



    def check_marks(self):
        row_counts = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0}
        col_counts = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0}
        diagonal_checks ={'lr': 0, 'rl': 0}
        marks = self._get_marks()
        if len(marks) > 4:
            for mark in marks:
                row_counts[ str(mark[0]) ] += 1
                col_counts[ str(mark[1]) ] += 1
                if mark[0] == mark[1]:
                    diagonal_checks['lr'] += 1
                elif int(mark[0]) + int(mark[1]) == 4:
                    diagonal_checks['rl'] += 1
            for k, v in row_counts.items():
                if v == 5:
                    return ('row', k)
            for k, v in col_counts.items():
                if v == 5:
                    return ('col', k)
            if diagonal_checks['lr'] == 5:
                return ('lr', '')
            elif diagonal_checks['rl'] == 5:
                return ('rl', '')

    def check_score(self, mark):
        check = self.check_marks()
        score = 0
        if check:
            for tile in self.tiles:
                if tile.is_marked():
                    pass
                else:
                    score += int(tile.num)
            return score * int(mark)
               




class CardTile:
    def __init__(self, num, row, col):
        self.num = num
        self.row = row
        self.col = col
        self.marked = False
    
    def mark(self, n):
        if self.num == n:
            self.marked = True
            return True

    def is_marked(self):
        if self.marked:
            return (self.row,self.col, self.num)
    
    def __repr__(self):
        if self.marked:
            return str(self.num)+'`'
        else:
            return str(self.num)

if __name__ == "__main__":
    s_board, s_mark = part2('sample.txt')
    test = s_board.check_score(s_mark)
    if test == 1924:
        print('test passed')
    else:
        print('test failed')
    c, m = part2('input.txt')

# learntris.py version 0.1.0
from sys import stdin
import re
from collections import defaultdict

num_rows = 22
num_cols = 10


class GameState:
    def __init__(self):
        self.cell = []
        for j in range(num_rows):
            self.cell.append([])
            for i in range(num_cols):
                self.cell[j].append('.')
        self.score = 0
        self.lines_cleared = 0
        self.active_name = ''
        self.top_left_active = [0, 0]
        self.active = []
        self.active_dictionary = defaultdict(list)
        self.active_dictionary['cyan'] = [['.', '.', '.', '.'], ['c', 'c', 'c', 'c'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
        self.active_dictionary['yellow'] = [['y', 'y'], ['y', 'y']]
        self.active_dictionary['red'] = [['r', 'r', '.'], ['.', 'r', 'r'], ['.', '.', '.']]
        self.active_dictionary['green'] = [['.', 'g', 'g'], ['g', 'g', '.'], ['.', '.', '.']]
        self.active_dictionary['blue'] = [['b', '.', '.'], ['b', 'b', 'b'], ['.', '.', '.']]
        self.active_dictionary['orange'] = [['.', '.', 'o'], ['o', 'o', 'o'], ['.', '.', '.']]
        self.active_dictionary['magenta'] = [['.', 'm', '.'], ['m', 'm', 'm'], ['.', '.', '.']]

    def print_game_state(self):
        for row in self.cell:
            print(' '.join(row))

    def update_game_state(self):
        stdin.read(1)
        for ndx, row in enumerate(self.cell):
                self.cell[ndx] = input().split()

    def clear_game_state(self):
        for ndx, row in enumerate(self.cell):
            self.cell[ndx] = ". . . . . . . . . .".split()

    def query_score(self):
        print(self.score)

    def query_lines_cleared(self):
        print(self.lines_cleared)

    def step_game(self):
        for ndx, row in enumerate(self.cell):
            if '.' not in self.cell[ndx]:
                self.cell[ndx] = ". . . . . . . . . .".split()
                self.score += 100
                self.lines_cleared += 1

    def initialize_active(self, tetranimo):
        self.active.clear()
        for ndx1 in range(2):
            for ndx2 in range(len(self.cell[0])):
                self.cell[ndx1][ndx2] = '.'
        self.active_name = tetranimo
        for row in self.active_dictionary[tetranimo]:
            self.active.append(row)
        if self.active_name == 'yellow':
            self.top_left_active = [0, 4]
        else:
            self.top_left_active = [0, 3]
        self.set_active()

    def set_active(self):
        for ndx1 in range(len(self.active)):
            for ndx2 in range(len(self.active)):
                self.cell[ndx1][ndx2+self.top_left_active[1]] = self.active[ndx1][ndx2].upper()

    def check_active(self):
        for row in self.active:
            print(' '.join(row))

    def rotate_clockwise(self):
        self.active = list(zip(*self.active[::-1]))

    def rotate_anticlockwise(self):
        self.active = list(zip(*self.active))[::-1]

    @staticmethod
    def output_line():
        print()

    def nudge_left(self):
        self.top_left_active[1] -= 1
        print(self.top_left_active[1])
    def nudge_right(self):
        lines_that_need_shift = []
        for ndx, line in enumerate(self.cell):
            match = re.search(r'[A-Z]', line)
            if match:
                lines_that_need_shift.append(ndx)
                if line[-1:].isupper():
                    return
        for line in lines_that_need_shift:
            self.cell[line] = ". "+self.cell[line][:-2]

    def detect_collision(self, ndx):
        if ndx == len(self.cell)-1:
            return True
        matches_upper = re.finditer(r'[A-Z]', self.cell[ndx])
        matches_lower = re.finditer(r'[a-z]', self.cell[ndx+1])
        for matchU in matches_upper:
            for matchL in matches_lower:
                if matchU.start() == matchL.start():
                    return True
        return False

    def nudge_down(self):
        for ndx, line in enumerate(self.cell):
            ndx2 = len(self.cell) - ndx - 1
            match = re.search(r'[A-Z]', self.cell[ndx2])
            if match:
                if self.detect_collision(ndx2):
                    return False
                else:
                    self.swap_elements(ndx2)
        return True

    def swap_elements(self, ndx2):
        upper_row = ndx2
        lower_row = ndx2+1
        matches_upper = re.finditer(r'[A-Z]', self.cell[upper_row])
        matches_lower = re.finditer(r'[A-Z]', self.cell[lower_row])
        for matchU in matches_upper:
            if self.cell[lower_row][matchU.start()].islower():
                print(self.cell[lower_row][matchU.start()])
            else:
                pass
        self.cell[ndx2], self.cell[ndx2+1] = self.cell[ndx2+1], self.cell[ndx2]

    def place_tiles(self):
        for ndx, row in enumerate(self.cell):
            self.cell[ndx] = row.lower()

    def drop_down(self):
        while self.nudge_down():
            pass
        self.place_tiles()


x = GameState()
command = ''
while True:
    command += stdin.read(1)
    if command == 'q':
        exit()
    elif command == 'p' or command == 'P':
        x.print_game_state()
        command = ''
    elif command == 'g':
        x.update_game_state()
        command = ''
    elif command == 'c':
        x.clear_game_state()
        command = ''
    elif command == '?':
        command += stdin.read(1)
        if command == '?s':
            x.query_score()
            command = ''
        elif command == '?n':
            x.query_lines_cleared()
            command = ''
    elif command == 's':
        x.step_game()
        command = ''
    elif command == 'I':
        x.initialize_active("cyan")
        command = ''
    elif command == 'O':
        x.initialize_active("yellow")
        command = ''
    elif command == 'Z':
        x.initialize_active("red")
        command = ''
    elif command == 'S':
        x.initialize_active("green")
        command = ''
    elif command == 'J':
        x.initialize_active("blue")
        command = ''
    elif command == 'L':
        x.initialize_active("orange")
        command = ''
    elif command == 'T':
        x.initialize_active("magenta")
        command = ''
    elif command == 't':
        x.check_active()
        command = ''
    elif command == ')':
        x.rotate_clockwise()
        command = ''
    elif command == '(':
        x.rotate_anticlockwise()
        command = ''
    elif command == ';':
        x.output_line()
        command = ''
    elif command == '<':
        x.nudge_left()
        command = ''
    elif command == '>':
        x.nudge_right()
        command = ''
    elif command == 'v':
        x.nudge_down()
        command = ''
    elif command == 'V':
        x.drop_down()
        command = ''
    else:
        command = ''

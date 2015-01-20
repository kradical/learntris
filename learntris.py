# learntris.py version 0.0.7
from sys import stdin
import re


class GameState:
    def __init__(self):
        self.row = []
        for i in range(0, 22):
            self.row.append(". . . . . . . . . .")
        self.score = 0
        self.lines_cleared = 0
        self.active_name = ''
        self.active = []
        self.active_dictionary = dict()
        self.active_dictionary['cyan'] = ['. . . .', 'c c c c', '. . . .', '. . . .']
        self.active_dictionary['yellow'] = ['y y', 'y y']
        self.active_dictionary['red'] = ['r r .', '. r r', '. . .']
        self.active_dictionary['green'] = ['. g g', 'g g .', '. . .']
        self.active_dictionary['blue'] = ['b . .', 'b b b', '. . .']
        self.active_dictionary['orange'] = ['. . o', 'o o o', '. . .']
        self.active_dictionary['magenta'] = ['. m .', 'm m m', '. . .']

    def print_game_state(self):
        for row in self.row:
            print(row)

    def update_game_state(self):
        stdin.read(1)
        for ndx, row in enumerate(self.row):
            self.row[ndx] = input()

    def clear_game_state(self):
        for ndx, row in enumerate(self.row):
            self.row[ndx] = ". . . . . . . . . ."

    def query_score(self):
        print(self.score)

    def query_lines_cleared(self):
        print(self.lines_cleared)

    def step_game(self):
        for ndx, row in enumerate(self.row):
            if '.' not in self.row[ndx]:
                self.row[ndx] = ". . . . . . . . . ."
                self.score += 100
                self.lines_cleared += 1

    def initialize_active(self, tetranimo):
        self.active.clear()
        self.active_name = tetranimo
        for row in self.active_dictionary[tetranimo]:
            self.active.append(row)
        for line in range(2):
            if self.active_name == 'cyan':
                self.row[line] = self.active[line].upper().join((". . . ", " . . ."))
            elif self.active_name == 'yellow':
                self.row[line] = self.active[line].upper().join((". . . . ", " . . . ."))
            else:
                self.row[line] = self.active[line].upper().join((". . . ", " . . . ."))

    def set_active(self):
        if self.active_name == 'yellow':
            for line in range(2):
                self.row[line] = self.active[line].upper().join((". . . . ", " . . . ."))
        elif self.active_name == 'cyan':
            for line in range(4):
                self.row[line] = self.active[line].upper().join((". . . ", " . . ."))
        else:
            for line in range(3):
                self.row[line] = self.active[line].upper().join((". . . ", " . . . ."))

    def check_active(self):
        for row in self.active:
            print(row)

    def rotate_clockwise(self):
        temp = []
        for _ in self.active:
            temp.append('')
        for ndx2, col in enumerate(self.active):
            for ndx1, row in enumerate(self.active):
                temp[ndx2] += self.active[len(self.active)-1-ndx1][2*ndx2]+' '
            temp[ndx2] = temp[ndx2][:-1]
        self.active = temp
        self.set_active()

    def rotate_anticlockwise(self):
        temp = []
        for _ in self.active:
            temp.append('')
        for ndx2, col in enumerate(self.active):
            for ndx1, row in enumerate(self.active):
                temp[ndx2] += self.active[ndx1][2*(len(self.active)-1)-2*ndx2]+' '
            temp[ndx2] = temp[ndx2][:-1]
        self.active = temp
        self.set_active()

    @staticmethod
    def output_line():
        print()

    def nudge_left(self):
        lines_that_need_shift = []
        for ndx, line in enumerate(self.row):
            match = re.search(r'[A-Z]', line)
            if match:
                lines_that_need_shift.append(ndx)
                if match.start() == 0:
                    return
        for line in lines_that_need_shift:
            self.row[line] = self.row[line][2:]+" ."

    def nudge_right(self):
        lines_that_need_shift = []
        for ndx, line in enumerate(self.row):
            match = re.search(r'[A-Z]', line)
            if match:
                lines_that_need_shift.append(ndx)
                if line[-1:].isupper():
                    return
        for line in lines_that_need_shift:
            self.row[line] = ". "+self.row[line][:-2]

    def nudge_down(self):
        for ndx, line in enumerate(self.row):
            ndx2 = len(self.row) - ndx - 1
            match = re.search(r'[A-Z]', self.row[ndx2])
            if match:
                if ndx == 0:
                    return
                else:
                    self.row[ndx2], self.row[ndx2+1] = self.row[ndx2+1], self.row[ndx2]

    def place_tiles(self):
        for ndx, row in enumerate(self.row):
            self.row[ndx] = row.lower()

    def drop_down(self):
        while True:
            for ndx, line in enumerate(self.row):
                ndx2 = len(self.row) - ndx - 1
                match = re.search(r'[A-Z]', self.row[ndx2])
                if match:
                    if ndx == 0:
                        self.place_tiles()
                        return
                    else:
                        self.row[ndx2], self.row[ndx2+1] = self.row[ndx2+1], self.row[ndx2]



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

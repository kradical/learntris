# learntris.py version 0.0.6
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
            if not '.' in self.row[ndx]:
                self.row[ndx] = ". . . . . . . . . ."
                self.score += 100
                self.lines_cleared += 1

    def set_active(self, tetranimo):
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
        self.active = temp

    def rotate_anticlockwise(self):
        temp = []
        for _ in self.active:
            temp.append('')
        for ndx2, col in enumerate(self.active):
            for ndx1, row in enumerate(self.active):
                pass
        self.active = temp

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
            from_bottom_ndx = len(self.row) - ndx - 1
            match = re.search(r'[A-Z]', self.row[from_bottom_ndx])
            if match:
                self.row[from_bottom_ndx], self.row[from_bottom_ndx+1] = self.row[from_bottom_ndx+1], self.row[from_bottom_ndx]

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
        x.set_active("cyan")
        command = ''
    elif command == 'O':
        x.set_active("yellow")
        command = ''
    elif command == 'Z':
        x.set_active("red")
        command = ''
    elif command == 'S':
        x.set_active("green")
        command = ''
    elif command == 'J':
        x.set_active("blue")
        command = ''
    elif command == 'L':
        x.set_active("orange")
        command = ''
    elif command == 'T':
        x.set_active("magenta")
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
    else:
        command = ''

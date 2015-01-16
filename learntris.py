# learntris.py version 0.0.5
from sys import stdin


class GameState:
    def __init__(self):
        self.row = []
        for i in range(0, 22):
            self.row.append(". . . . . . . . . .")
        self.score = 0
        self.lines_cleared = 0
        self.active = []
        self.active_dictionary = {}
        self.active_dictionary['cyan'] = ['. . . .', 'c c c c ', '. . . .', '. . . .']
        self.active_dictionary['yellow'] = ['y y', 'y y']
        self.active_dictionary['red'] = ['r r .', '. r r', '. . .']
        self.active_dictionary['green'] = ['. g g', 'g g .', '. . .']
        self.active_dictionary['blue'] = ['b . .', 'b b b', '. . .']
        self.active_dictionary['orange'] = ['. . o', 'o o o', '. . .']
        self.active_dictionary['magenta'] = ['. m .', 'm m m', '. . .']

    def print_game_state(self):
        for row in self.row:
            print(row)
        stdin.read(1)

    def update_game_state(self):
        stdin.read(1)
        for ndx, row in enumerate(self.row):
            self.row[ndx] = input()

    def clear_game_state(self):
        for ndx, row in enumerate(self.row):
            self.row[ndx] = ". . . . . . . . . ."
        stdin.read(1)

    def query_score(self):
        print(self.score)
        stdin.read(1)

    def query_lines_cleared(self):
        print(self.lines_cleared)
        stdin.read(1)

    def step_game(self):
        for ndx, row in enumerate(self.row):
            if not '.' in self.row[ndx]:
                self.row[ndx] = ". . . . . . . . . ."
                self.score += 100
                self.lines_cleared += 1
        stdin.read(1)

    def set_active(self, tetranimo):
        self.active.clear()
        for row in self.active_dictionary[tetranimo]:
            self.active.append(row)
        stdin.read(1)

    def check_active(self):
        for row in self.active:
            print(row)
        stdin.read(1)

    def rotate_clockwise(self):
        stdin.read(1)
        temp = []
        for row in self.active:
            temp.append('')
        for ndx2, col in enumerate(self.active):
            for ndx1, row in enumerate(self.active):
                temp[ndx2] += self.active[len(self.active)-1-ndx1][2*ndx2]+' '
        self.active = temp

x = GameState()
command = ''
while True:
    command += stdin.read(1)
    if command == 'q':
        break
    elif command == 'p':
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
    else:
        command = ''

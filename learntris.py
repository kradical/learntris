#learntris.py version 0.0.3


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

    def update_game_state(self):
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
        for row in self.active_dictionary[tetranimo]:
            self.active.append(row)
        return

    def check_active(self):
        for row in self.active:
            print(row)

x = GameState()

while True:
    command = input()
    if command == 'q':
        break
    elif command == 'p':
        x.print_game_state()
    elif command == 'g':
        x.update_game_state()
    elif command == 'c':
        x.clear_game_state()
    elif command == '?s':
        x.query_score()
    elif command == '?n':
        x.query_lines_cleared()
    elif command == 's':
        x.step_game()
    elif command == 'I':
        x.set_active("cyan")
    elif command == 'O':
        x.set_active("yellow")
    elif command == 'Z':
        x.set_active("red")
    elif command == 'S':
        x.set_active("green")
    elif command == 'J':
        x.set_active("blue")
    elif command == 'L':
        x.set_active("orange")
    elif command == 'T':
        x.set_active("magenta")
    elif command == 't':
        x.check_active()
    else:
        print("HAHAHA"+command)
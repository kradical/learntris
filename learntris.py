#learntris.py version 0.0.2


class GameState:
    def __init__(self):
        self.row = []
        for i in range(0, 22):
            self.row.append(". . . . . . . . . .")
        self.score = 0
        self.lines_cleared = 0
        self.active = []

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

    def set_active_cyan(self):
        self.active.clear()
        for i in range(0, 4):
            self.active.append(". . . .")
        self.active[1] = "c c c c"
        return

    def set_active_yellow(self):
        self.active.clear()
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
        x.set_active_cyan()
    elif command == 't':
        x.check_active()
    elif command == 'O':
        x.set_active_yellow()
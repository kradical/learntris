#learntris.py version 0.0.1


class GameState:
    def __init__(self):
        self.row = []
        for i in range(0, 22):
            self.row.append(". . . . . . . . . .")
        self.score = 0

    def print_game_state(self):
        for row in self.row:
            print(row)

    def update_game_state(self, test_input):
        for ndx, row in enumerate(self.row):
            self.row[ndx] = input()

    def clear_game_state(self):
        for ndx, row in enumerate(self.row):
            self.row[ndx] = ". . . . . . . . . ."

    def query_score(self):
        print(self.score)

x = GameState()

while True:
    command = input()
    if command == 'q':
        break
    elif command == 'p':
        x.print_game_state()
    elif command == 'g':
        x.update_game_state(command)
    elif command == 'c':
        x.clear_game_state()
    elif command == '?s':
        x.query_score()
#learntris.py version 0.0.0


class GameState:
    def __init__(self):
        self.row = []
        for i in range(0, 22):
            self.row.append(". . . . . . . . . .")

    def print_game_state(self):
        for row in self.row:
            print(row)

    def update_game_state(self, test_input):
        for ndx, row in enumerate(self.row):
            self.row[ndx] = input()


x = GameState()

while True:
    command = input()
    if command == 'q':
        break
    elif command == 'p':
        x.print_game_state()
    elif command == 'g':
        x.update_game_state(command)
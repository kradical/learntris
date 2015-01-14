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
        print("HERE IT IS\n\n")
        test_input2 = test_input[3:418]
        print(test_input2+"\n\n")

x = GameState()

while True:
    command = input()
    if command == 'q':
        break
    elif command == 'p':
        x.print_game_state()
    elif command == 'g':
        x.update_game_state(command)
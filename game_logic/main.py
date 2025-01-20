from class_game import Game

class Main:
    def __init__(self):
        self.game = Game(15, 15)
        self.play()

    def play(self):
        import random
        turn = 0
        players = ["red", "blue"]

        while True:
            self.game.print()
            current_player = players[turn % 2]
            print(f"It's {current_player}'s turn.")
            dice = random.randint(1, 6)
            print(f"Dice roll: {dice}")

            piece_index = 0  # Only one piece per player in this example
            moved = self.game.move_piece(current_player, piece_index, dice)

            if moved:
                print("Move successful!")
            else:
                print("Move failed.")

            turn += 1
            input("Press Enter to continue...")  # Wait for user input


if __name__ == "__main__":
    main_instance = Main()
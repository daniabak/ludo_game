from ludo_game.game_logic.class_game import Game

class Main:
    def __init__(self):
        self.game = Game(15, 15)
        self.game.print()



if __name__ == "__main__":
    main_instance = Main()

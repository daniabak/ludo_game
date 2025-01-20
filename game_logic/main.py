from class_game import LudoBoard

class Main:
    def __init__(self):
        self.ludo_board = LudoBoard()
        self.ludo_board.initialize_board()
        self.ludo_board.print_board()



if __name__ == "__main__":
    main = Main()

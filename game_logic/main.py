from class_game import LudoBoard
import random
class Main:
    def init(self):
        self.game=LudoBoard()
    def MoveWithDice(self):
        input=str(input(f"{"select stone in this list please:"+self.numberOfStoneInPlayerB if len(self.game.numberOfStoneInPlayerB) != 0 else "enter s to start as blue"}"))
        dice= random.randint(1, 6)
        self.game.move_piece(input,dice)
        # if dice ==6:
             
from class_game import LudoBoard
from expectiminimax import Expectiminimax
class Main:
    def __init__(self):
        self.game=LudoBoard()
        print("start game , welcome \n ")
        self.game.print_board()
        self.expectiminimax=Expectiminimax(3)
        self.ControlTheMovement(self.game,self.expectiminimax)

    def ControlTheMovement(self,game,expectiminimax):
      while True:
        if game.check_win() and game.isCurrentPlayerIsUser: 
         print("Red is win ")
         print(game.check_win())
         break
        if game.check_win() and not game.isCurrentPlayerIsUser:
         print("blue is win ")
         break
        
        print("current player is Blue" if  game.isCurrentPlayerIsUser else "current player is Red")
        dice =6
         
        print("dice value =",dice)
        print(game.numberOfStoneInPlayerB,"list of player blue")
        print(game.numberOfStoneInPlayerR,"list of player red")
        if game.isCurrentPlayerIsUser and dice==6:
          inputUser=input(f"select stone in this list please:{game.numberOfStoneInPlayerB} or press s to add stone as blue in start square" if len(game.numberOfStoneInPlayerB) != 0 else "enter s to start as blue (user)")
        if game.isCurrentPlayerIsUser and dice!=6:
          if len(game.numberOfStoneInPlayerB) != 0 :
           inputUser=input(f"select stone in this list please:{game.numberOfStoneInPlayerB } ")
          else:
             print("wait")
             game.isCurrentPlayerIsUser = not game.isCurrentPlayerIsUser 
             continue
        if not game.isCurrentPlayerIsUser and dice==6:
           inputUser=expectiminimax.get_best_move(game,'r',dice)
           print("index from exp dice 6",inputUser)
           if inputUser==0:
              inputUser=="s"
          # inputUser=input(f"select stone in this list please:{game.numberOfStoneInPlayerR} or press s to add stone as red in start square" if len(game.numberOfStoneInPlayerR) != 0 else "enter s to start as red (user)") 
        if not game.isCurrentPlayerIsUser and dice!=6:
          if len(game.numberOfStoneInPlayerR) != 0 :
           inputUser=expectiminimax.get_best_move(game,'r',dice) 
           print("index from exp dice ! 6",inputUser)
          else:
             print("wait")
             game.isCurrentPlayerIsUser = not game.isCurrentPlayerIsUser
             continue
        if dice ==6:
          if str(inputUser) == "s" :
            self.addStoneFromBase(game)
            game.print_board()
            game.countDiceOfValueSix+=1
            if game.countDiceOfValueSix>2:
             
            #  self.ControlTheMovement(game)
            

               game.isCurrentPlayerIsUser = not game.isCurrentPlayerIsUser
               game.countDiceOfValueSix=0
              #  self.ControlTheMovement(game)
          else:
              
      
             if (int(inputUser)  in game.numberOfStoneInPlayerB ):  
               game.countDiceOfValueSix+=1

               if game.countDiceOfValueSix<3:
                game=game.move_piece(int(inputUser),dice)
               else:

                game=game.move_piece(int(inputUser),dice)

                game.isCurrentPlayerIsUser = not game.isCurrentPlayerIsUser
                game.countDiceOfValueSix=0
                # self.ControlTheMovement(game)
             elif int(inputUser)  in game.numberOfStoneInPlayerR :  
               game.countDiceOfValueSix+=1

               if game.countDiceOfValueSix<3:
                game=game.move_piece(int(inputUser),dice)


                # self.ControlTheMovement(game)
               else:

                game=game.move_piece(int(inputUser),dice)
 
                game.isCurrentPlayerIsUser = not game.isCurrentPlayerIsUser
                game.countDiceOfValueSix=0
        else:
             
             game=game.move_piece(int(inputUser),dice)
             game.isCurrentPlayerIsUser = not game.isCurrentPlayerIsUser
             game.countDiceOfValueSix=0
            #  self.ControlTheMovement(game)

            


    def addStoneFromBase(self,game):
    
         if game.isCurrentPlayerIsUser:
            if len(game.numberOfStoneInPlayerB)<4:
              if  game.board[26].player is None:
                    game.board[26].player = "b"
                 
              else:
                game.board[26].player += "b"

              game.numberOfStoneInPlayerB.append(26)
              print(game.board[26].player,"player start cell blue")
              print("Stone added to base for Blue.")
            else:
               print("no stone left")

         else:   
              if len(game.numberOfStoneInPlayerR) < 4:
                if  game.board[0].player is None:
                    game.board[0].player = "r"
                else:
                    game.board[0].player += "r"

                game.numberOfStoneInPlayerR.append(0)
                print(game.board[0].player,"player start cell red")
                print("done add to numberOfStoneInPlayerR")
              else:
                print("No stones left to add for Red.")
      
if __name__ == "__main__":
    main_game = Main()           
      

        
       
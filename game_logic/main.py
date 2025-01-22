from class_game import LudoBoard
class Main:
    def __init__(self):
        self.game=LudoBoard()
        print("start game , welcome \n ")
        self.game.print_board()
        self.ControlTheMovement(self.game)

    def ControlTheMovement(self,game):
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
        # game.roll_dice()
        print("dice value =",dice)
        print(game.numberOfStoneInPlayerB,"list of player blue")
        print(game.numberOfStoneInPlayerR,"list of player red")
        if game.isCurrentPlayerIsUser and dice==6:
          inputUser=input(f"select stone in this list please:{game.numberOfStoneInPlayerB} or press s to add stone as blue in start square" if len(game.numberOfStoneInPlayerB) != 0 else "enter s to start as blue (user)")
        if game.isCurrentPlayerIsUser and dice!=6:
          inputUser=input(f"select stone in this list please:{game.numberOfStoneInPlayerB} " if len(game.numberOfStoneInPlayerB) != 0 else "sorry wait!")
        if not game.isCurrentPlayerIsUser and dice==6:
          inputUser=input(f"select stone in this list please:{game.numberOfStoneInPlayerR} or press s to add stone as red in start square" if len(game.numberOfStoneInPlayerR) != 0 else "enter s to start as red (user)") 
        if not game.isCurrentPlayerIsUser and dice!=6:
          inputUser=input(f"select stone in this list please:{game.numberOfStoneInPlayerR} " if len(game.numberOfStoneInPlayerR) != 0 else "sorry wait !") 
        if dice ==6:
          if str(inputUser) == "s" :
            self.addStoneFromBase(game)
            game.print_board()
            game.countDiceOfValueSix+=1
            if game.countDiceOfValueSix>4:
             
            #  self.ControlTheMovement(game)
            

               game.isCurrentPlayerIsUser = not game.isCurrentPlayerIsUser
               game.countDiceOfValueSix=1
              #  self.ControlTheMovement(game)
          else:
              
             print(game.numberOfStoneInPlayerB,"_________________",inputUser)
             game.print_board()
             if (int(inputUser)  in game.numberOfStoneInPlayerB ):  
               game.countDiceOfValueSix+=1
               print("FGhjk")
               if game.countDiceOfValueSix<4:
                dd=game.move_piece(inputUser,dice)
                dd.print_board()
                print("jhgfdssdfghjk")
                # self.ControlTheMovement(game)
               else:
                print("masa")
                game.isCurrentPlayerIsUser = not game.isCurrentPlayerIsUser
                game.countDiceOfValueSix=1
                # self.ControlTheMovement(game)
             elif inputUser  in game.numberOfStoneInPlayerR and len(game.numberOfStoneInPlayerR)>0:  
               game.countDiceOfValueSix+=1
               print("danaadanaa")
               if game.countDiceOfValueSix<4:
                dd=game.move_piece(inputUser,dice)
                dd.print_board()
                print("++++++++++++")
                # self.ControlTheMovement(game)
               else:
                print("))))))))))))))))")
                game.isCurrentPlayerIsUser = not game.isCurrentPlayerIsUser
                game.countDiceOfValueSix=1 
        else:
             game.move_piece(inputUser,dice)
             game.isCurrentPlayerIsUser = not game.isCurrentPlayerIsUser

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
                    game.board[0].player + "r"

                game.numberOfStoneInPlayerR.append(0)
                print(game.board[0].player,"player start cell red")
                print("done add to numberOfStoneInPlayerR")
              else:
                print("No stones left to add for Red.")
      
if __name__ == "__main__":
    main_game = Main()           
      

        
       
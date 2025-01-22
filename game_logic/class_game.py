import copy
from class_square import Squares
import random

class LudoBoard:
    def __init__(self):
        self.board = [] 
        self.initialize_board() 
        self.goalR = [None, None, None, None]  
        self.goalB = [None, None, None, None] 
        self.numberOfStoneInPlayerR = [] 
        self.numberOfStoneInPlayerB = [] 
        self.isCurrentPlayerIsUser=True
        self.countDiceOfValueSix=0

    def roll_dice(self):
          
        return random.randint(1, 6)

    def initialize_board(self):
        for i in range(52):
            if i == 0:
 
                self.board.append(Squares(player=None, type="startR"))

            elif i == 26:
         
                self.board.append(Squares(player=None, type="startB"))
            elif i in [0, 13, 26, 39]:
             
                self.board.append(Squares(player=None, type="#"))
            elif i == 51:
  
                self.board.append(Squares(player=None, type="endR"))
            elif i == 25:
    
                self.board.append(Squares(player=None, type="endB"))
            else:
     
                self.board.append(Squares(player=None, type="path"))




    def add_stone_to_goal(self, color_player, dice_value):
        goal = self.goalR if color_player == "r" else self.goalB
        none_count = goal.count(None)

        if dice_value != none_count:
            return False

        for i in range(len(goal) - 1, -1, -1):
            if goal[i] is None:
                if color_player == 'r':
                    goal[i] = "Red_Stone"
                    
                else:
                    goal[i] = "Blue_Stone"
                print("goal :",goal)
                return True
        print(goal)
        return False



    def check_win(self):

           if  None not in self.goalB or None not in self.goalR :
               return True
           
           return False


    def print_board(self):

     for i in range(0, len(self.board), 15): 
        row = [] 
        for cell in self.board[i:i+15]: 
            if cell.type == "path": 
                row.append(f"{cell.player if cell.player is not None else '   '}") 
            else:

                row.append(
                    f"{cell.type[0].upper() + cell.type[-1].upper()} {cell.player if cell.player is not None else ''}"
                )
        print(" | ".join(row))  
    def checkPathHaveWall(self,board,index,dice):
     currentCell=board.board[index]
     finalIndex= (index + dice) % len(board.board) 
     if(index+1 < finalIndex):
         for cell in range(index+1,finalIndex):
            
            if  board.board[cell].player is not None and len(board.board[cell].player) >1 and board.board[cell].player[0]!=currentCell.player[0]:
                    return False
     else   :
      for cell in range(index + 1, len(board.board)):
        if board.board[cell].player is not None and len(board.board[cell].player) > 1 and board.board[cell].player[0] != currentCell.player[0]:
            return False

      for cell in range(0, finalIndex):
        if board.board[cell].player is not None and len(board.board[cell].player) > 1 and board.board[cell].player[0] != currentCell.player[0]:
            return False
  
     return True
 
    def move_piece(self, index, steps):
     newBoard =  copy.deepcopy(self)
     current_square = newBoard.board[index]
     if index < 0 or index >= len(newBoard.board):
            print("Invalid index!")
            return newBoard

        
     if current_square.player =="":
            print("No piece at the specified index!")
            return newBoard


     if(newBoard.checkPathHaveWall(newBoard,index,steps)==True): 

       isHaveend=newBoard.check_path_contains_end(current_square.player[0],steps,index)

       if isHaveend == False: 
         
         new_index = index + steps


         current_index=index
         while steps > 0:
             steps -= 1
             current_index+=1
             if(current_index<len(newBoard.board)):
              if newBoard.board[current_index].type == f"end{newBoard.board[index].player[0].upper()}" and steps != 0:
      
                return newBoard
         if new_index >= len(newBoard.board):

          steps_remaining = new_index - len(newBoard.board) 
          new_index = 0 
          while steps_remaining > 0:

            new_index += 1
            steps_remaining -= 1

       



         destination_square = newBoard.board[new_index]

         print(destination_square.player)
         if  destination_square.player != "" :
            if(destination_square.player[0]==current_square.player[0] ):
              
              destination_square.player= destination_square.player+current_square.player[0]
              current_square.player=current_square.player[1:]
              if destination_square.player == "b" * (len(destination_square.player) // len("b")):
                  if index in newBoard.numberOfStoneInPlayerB:
                
                     newBoard.numberOfStoneInPlayerB.remove(index)
                  newBoard.numberOfStoneInPlayerB.append(new_index)
              elif destination_square.player == "r" * (len(destination_square.player) // len("r")):
                 if index in newBoard.numberOfStoneInPlayerR:
        
                      print("remove..........................")
                      newBoard.numberOfStoneInPlayerR.remove(index)
                 newBoard.numberOfStoneInPlayerR.append(new_index)
            elif (destination_square.player!=current_square.player and destination_square.type!="#" and destination_square.type!="startB" and destination_square.type!="startR"): 
               if(destination_square.player=="b" * (len(destination_square.player) // len("b"))):
                   newBoard.numberOfStoneInPlayerB.remove(new_index)
                 
                   newBoard.numberOfStoneInPlayerR.remove(index)
                   newBoard.numberOfStoneInPlayerR.append(new_index)
                   destination_square.player = current_square.player[0]
                   current_square.player = current_square.player[1:]
                   print(newBoard.numberOfStoneInPlayerB)
                   print(newBoard.numberOfStoneInPlayerR)
               elif(destination_square.player=="r" * (len(destination_square.player) // len("r"))):
                   newBoard.numberOfStoneInPlayerR.remove(new_index)
                   #if not current_square.player[1:] :
                   newBoard.numberOfStoneInPlayerB.remove(index)
                   newBoard.numberOfStoneInPlayerB.append(new_index)
                   destination_square.player = current_square.player[0]
                   current_square.player = current_square.player[1:]   
            # newBoard.print_board()
            return newBoard
  
         destination_square.player = current_square.player[0]
         if(destination_square.player=="b"):
                  print(current_square.player[1:]+"++++++++++++")
                 # if not current_square.player[1:] :
                  newBoard.numberOfStoneInPlayerB.remove(index)
                  newBoard.numberOfStoneInPlayerB.append(new_index)
                  print(newBoard.numberOfStoneInPlayerB)
         elif(destination_square.player=="r"):
                  #if not current_square.player[1:] :
                  newBoard.numberOfStoneInPlayerR.remove(index)
                  newBoard.numberOfStoneInPlayerR.append(new_index)
                  print(newBoard.numberOfStoneInPlayerR)
         current_square.player = current_square.player[1:]
       
                  
         
        #  newBoard.print_board()
         return newBoard
       else :
         if(current_square.player[0]=="r"):
           #if not current_square.player[1:] :
           newBoard.numberOfStoneInPlayerR.remove(index)
           newBoard.numberOfStoneInPlayerR.append(52)
           current_square.player = current_square.player[1:]
         elif(current_square.player[0]=="b"):
           #if not current_square.player[1:] :
           newBoard.numberOfStoneInPlayerB.remove(index)
           newBoard.numberOfStoneInPlayerB.append(52)
           current_square.player = current_square.player[1:]
    #  newBoard.print_board()
     return newBoard
    
    def next_state(self, dice_value, player):
     newboard=copy.deepcopy(self)
     next_states = []  # قائمة لتخزين الحالات الجديدة

     stones_to_move = (
        newboard.numberOfStoneInPlayerB if player else newboard.numberOfStoneInPlayerR
     )
   
     if dice_value == 6 and len(stones_to_move) < 4:
        new_board = copy.deepcopy(newboard)
        start_index = 0 if not player else 26 
        
        start_square = new_board.board[start_index]


        if start_square.player =="" or start_square.player[0] != ("r" if  player else "b"):
      
            start_square.player = (start_square.player or "") + ("r" if not player else "b")
            
            if not player:
                new_board.numberOfStoneInPlayerR.append(start_index)
            else:
                new_board.numberOfStoneInPlayerB.append(start_index)
            
            next_states.append(tuple([new_board,start_index]))

     for index in stones_to_move: 
        new_board = newboard.move_piece(index, dice_value) 

        if not newboard.is_same_board(newboard, new_board):
            next_states.append(tuple([new_board,index])) 

     return next_states

    def is_same_board(self,new_board, other_board):
    
     if len(new_board.board) != len(other_board.board):
        return False
     
     for i in range(len(new_board.board)):
 
        if new_board.board[i].type != other_board.board[i].type or new_board.board[i].player != other_board.board[i].player:
            return False
     if new_board.goalR != other_board.goalR or new_board.goalB != other_board.goalB:
        return False

     if new_board.numberOfStoneInPlayerR != other_board.numberOfStoneInPlayerR or new_board.numberOfStoneInPlayerB != other_board.numberOfStoneInPlayerB:
        return False

     return True

    def check_path_contains_end(self,color, value,index):
        if index < 0 or index >= len(self.board):
         print("Invalid index!")
         return False

        current_square = self.board[index]

        if current_square.player =="":
         print("No piece at the specified index!")
         return False

        current_color = current_square.player[0].lower()  # Assume first character represents color (e.g., 'r' or 'b')
        steps_remaining = value
        current_position = index

        while steps_remaining > 0:
          if self.board[current_position].type == f"end{current_color.upper()}":
           
            if(self.add_stone_to_goal(current_color, steps_remaining)):
                return True
          current_position += 1

          if current_position >= len(self.board):
            current_position = 0

          steps_remaining -= 1


        return False
    def evaluate_board(self, board, player):
       
        score = 0
        goalR=[]
        for i in board.goalR :
          if i is not None:
           goalR.append(i)
        goalB=[]
        for i in board.goalB :
          if i is not None:
           goalB.append(i)  
   
        score += len(goalR) * (10 if player == "r" else -10)
        score += len(goalB) * (10 if player == "b" else -10)

        score += len(board.numberOfStoneInPlayerR) * (5 if player == "r" else -5)
        score += len(board.numberOfStoneInPlayerB) * (5 if player == "b" else -5)

        for index in board.numberOfStoneInPlayerR:
            distance = self.calculate_distance_to_goal(index, "r")
            score += (10 - distance) if player == "r" else -(10 - distance)
       
        for index in board.numberOfStoneInPlayerB:
            distance = self.calculate_distance_to_goal(index, "b")
            score += (10 - distance) if player == "b" else -(10 - distance)

        for index in board.numberOfStoneInPlayerR:
            if board.board[index].type == "#":
                score += 3 if player == "r" else -3
       
        for index in board.numberOfStoneInPlayerB:
            if board.board[index].type == "#":
                score += 3 if player == "b" else -3
       
        return score
    def calculate_distance_to_goal(self, index, player):
        """
        حساب المسافة بين موضع الحجر الحالي ونقطة النهاية.
        """
        if player == "r":
                goal_start = 51 
        elif player == "b":
                goal_start = 25  

        if index <= goal_start:
                return goal_start - index 
        else:
            return (len(self.board) - index) + goal_start


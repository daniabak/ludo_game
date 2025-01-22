import copy
from class_square import Squares
import random

class LudoBoard:
    def __init__(self):
        # تمثيل الرقعة باستخدام مصفوفة أحادية
        self.board = []  # قائمة لتمثيل الرقعة
        self.initialize_board()  # استدعاء دالة لتعبئة الرقعة
        self.goalR = [None, None, None, None]  # منطقة الهدف للاعب الأحمر
        self.goalB = [None, None, None, None]  # منطقة الهدف للاعب الأزرق
        self.numberOfStoneInPlayerR = []  # أحجار اللاعب الأحمر
        self.numberOfStoneInPlayerB = []  # أحجار اللاعب الأزرق
        self.isCurrentPlayerIsUser=True
        self.countDiceOfValueSix=0

    def roll_dice(self):
          
        return random.randint(1, 6)

    def initialize_board(self):
        # إنشاء الرقعة باستخدام كائنات Squares
        for i in range(52):  # مثال لمسار يحتوي على 52 خلية
            if i == 0:
                # أول خلية هي نقطة البداية للاعب الأحمر
                self.board.append(Squares(player=None, type="startR"))

            elif i == 26:
                # منتصف الرقعة نقطة البداية للاعب الأزرق
                self.board.append(Squares(player=None, type="startB"))
            elif i in [0, 13, 26, 39]:
                # خانات آمنة
                self.board.append(Squares(player=None, type="#"))
            elif i == 51:
                # نهاية المسار للاعب الأحمر
                self.board.append(Squares(player=None, type="endR"))
            elif i == 25:
                # نهاية المسار للاعب الأزرق
                self.board.append(Squares(player=None, type="endB"))
            else:
                # خانات عادية
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
                return True

        return False



    def check_win(self):

           if  None not in self.goalB or None not in self.goalR :
               return True
           
           return False


    def print_board(self):

# إنشاء الرقعة 
    # طباعة الرقعة على التيرمنال
     for i in range(0, len(self.board), 15):  # طباعة كل صف من 15 عنصر
        row = []  # قائمة مؤقتة لتخزين العناصر في الصف الحالي
        for cell in self.board[i:i+15]:  # أخذ 15 عنصر من المصفوفة
            if cell.type == "path":  # إذا كانت الخلية من النوع "path"
                row.append(f"{cell.player if cell.player is not None else '   '}")  # طباعة player إذا لم يكن None
            else:
                # طباعة محتوى الخلية إذا كان هناك player أو طباعة النوع فقط
                row.append(
                    f"{cell.type[0].upper() + cell.type[-1].upper()} {cell.player if cell.player is not None else ''}"
                )
        print(" | ".join(row))  # طباعة الصف مع الفصل بين العناصر بـ " | " # طباعة الصف مع الفصل بين العناصر بـ " | "
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

    # المرور على الجزء الثاني (من بداية الرقعة إلى finalIndex)
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

        
     if current_square.player is None:
            print("No piece at the specified index!")
            return newBoard

    #  print(newBoard.checkPathHaveWall(index,steps))
     if(newBoard.checkPathHaveWall(newBoard,index,steps)==True): 
      #  print("checkPathHaveWall")
       isHaveend=newBoard.check_path_contains_end(current_square.player[0],steps,index)
      #  print( isHaveend)
       if isHaveend == False: 
         
         new_index = index + steps

        # Handle wrapping around the board
         current_index=index
         while steps > 0:
             steps -= 1
             current_index+=1
             if(current_index<len(newBoard.board)):
              if newBoard.board[current_index].type == f"end{newBoard.board[index].player[0].upper()}" and steps != 0:
                newBoard.print_board()
                return newBoard
         if new_index >= len(newBoard.board):

          steps_remaining = new_index - len(newBoard.board)  # الخطوات المتبقية بعد تجاوز الرقعة
          new_index = 0  # إعادة التحديد إلى بداية الرقعة
          while steps_remaining > 0:

            new_index += 1
            steps_remaining -= 1

       


        # Check if the destination is valid
         destination_square = newBoard.board[new_index]

         print(destination_square.player)
         if destination_square.player != None:
            if(destination_square.player[0]==current_square.player[0] ):
              
              destination_square.player= destination_square.player+current_square.player[0]
              current_square.player=current_square.player[1:]
              if destination_square.player == "b" * (len(destination_square.player) // len("b")):
                  if index in newBoard.numberOfStoneInPlayerB:
                  # if not current_square.player : 
                     newBoard.numberOfStoneInPlayerB.remove(index)
                  newBoard.numberOfStoneInPlayerB.append(new_index)
              elif destination_square.player == "r" * (len(destination_square.player) // len("r")):
                 if index in newBoard.numberOfStoneInPlayerR:
                    #if not current_square.player:
                      print("remove..........................")
                      newBoard.numberOfStoneInPlayerR.remove(index)
                 newBoard.numberOfStoneInPlayerR.append(new_index)
            elif (destination_square.player!=current_square.player and destination_square.type!="#" and destination_square.type!="startB" and destination_square.type!="startR"): 
               if(destination_square.player=="b" * (len(destination_square.player) // len("b"))):
                   newBoard.numberOfStoneInPlayerB.remove(new_index)
                   #if not current_square.player[1:] :
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
            newBoard.print_board()
            return newBoard
        # Move the piece
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
       
                  
         
         newBoard.print_board()
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
     newBoard.print_board()
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
         # نقطة البداية لكل لاعب
        start_square = new_board.board[start_index]

        # تحقق من أن الخلية ليست ممتلئة
        if start_square.player is None or start_square.player[0] != ("r" if  player else "b"):
            # إضافة حجر إلى نقطة البداية
            start_square.player = (start_square.player or "") + ("r" if not player else "b")
            
            # تحديث قائمة الأحجار
            if not player:
                new_board.numberOfStoneInPlayerR.append(start_index)
                print("::::::::::::::::::::::")
                print(new_board.numberOfStoneInPlayerR)
            else:
                new_board.numberOfStoneInPlayerB.append(start_index)
            
            next_states.append(new_board)

     for index in stones_to_move:  # تكرار على كل حجر
        new_board = newboard.move_piece(index, dice_value)  # استدعاء تابع الحركة

        # التحقق مما إذا كانت الرقعة الجديدة مختلفة
        if not newboard.is_same_board(newboard, new_board):
            next_states.append(new_board)  # إضافة الرقعة الجديدة إلى القائمة

     return next_states

    def is_same_board(self,new_board, other_board):
    
     if len(new_board.board) != len(other_board.board):
        return False
     
     for i in range(len(new_board.board)):
        # مقارنة الحقول حسب النوع واللاعب
        if new_board.board[i].type != other_board.board[i].type or new_board.board[i].player != other_board.board[i].player:
            return False

    # مقارنة الأهداف
     if new_board.goalR != other_board.goalR or new_board.goalB != other_board.goalB:
        return False

    # مقارنة أحجار اللاعبين
     if new_board.numberOfStoneInPlayerR != other_board.numberOfStoneInPlayerR or new_board.numberOfStoneInPlayerB != other_board.numberOfStoneInPlayerB:
        return False

     return True

    def check_path_contains_end(self,color, value,index):
        if index < 0 or index >= len(self.board):
         print("Invalid index!")
         return False

        current_square = self.board[index]

        if current_square.player is None:
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

        # Wrap around the board
          if current_position >= len(self.board):
            current_position = 0

          steps_remaining -= 1

        # Check if the square is an 'end' square of the same color

        return False

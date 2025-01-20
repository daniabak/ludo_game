from class_square import Squares


class LudoBoard:
    def __init__(self):
        # تمثيل الرقعة باستخدام مصفوفة أحادية
        self.board = []  # قائمة لتمثيل الرقعة
        self.initialize_board()  # استدعاء دالة لتعبئة الرقعة
        self.goalR = [None, None, None, None]  # منطقة الهدف للاعب الأحمر
        self.goalB = [None, None, None, None]  # منطقة الهدف للاعب الأزرق
        self.numberOfStoneInPlayerR = []  # أحجار اللاعب الأحمر
        self.numberOfStoneInPlayerB = []  # أحجار اللاعب الأزرق

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

    def check_win(self):
        # Check if any player has all their goals filled
        if all(goal is not None for goal in self.goalR):
            return "Red"
        elif all(goal is not None for goal in self.goalB):
            return "Blue"
        return None

    def print_board(self):
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
        print(" | ".join(row))  # طباعة الصف مع الفصل بين العناصر بـ " | "

    def move_piece(self, index, steps):
        """
        Move a piece from the specified index by the given number of steps.
        :param index: The index of the piece to move.
        :param steps: The number of steps to move.
        """
        if index < 0 or index >= len(self.board):
            print("Invalid index!")
            return False

        current_square = self.board[index]
        
        if current_square.player is None:
            print("No piece at the specified index!")
            return False

        new_index = index + steps

        # Handle wrapping around the board
        if new_index >= len(self.board):
            new_index = new_index % len(self.board)

        # Check if the destination is valid
        destination_square = self.board[new_index]

        if destination_square.player is not None:
            if(destination_square.player[0]==current_square.player[0] ):
              
              destination_square.player= destination_square.player+current_square.player[0]
              current_square.player=current_square.player[1:]
              if destination_square.player == "b" * (len(destination_square.player) // len("b")):
                  if index in self.numberOfStoneInPlayerB:
                    self.numberOfStoneInPlayerB.remove(index)
                  self.numberOfStoneInPlayerB.append(new_index)
              elif destination_square.player == "r" * (len(destination_square.player) // len("r")):
                 if index in self.numberOfStoneInPlayerR:
                    self.numberOfStoneInPlayerR.remove(index)
                 self.numberOfStoneInPlayerR.append(new_index)
            elif (destination_square.player!=current_square.player and destination_square.type!="#" and destination_square.type!="startB" and destination_square.type!="startR"): 
               if(destination_square.player=="b"):
                   self.numberOfStoneInPlayerB.remove(new_index)
                   self.numberOfStoneInPlayerR.remove(index)
                   self.numberOfStoneInPlayerR.append(new_index)
                   destination_square.player = current_square.player[0]
                   current_square.player = current_square.player[1:]
                   print(self.numberOfStoneInPlayerB)
                   print(self.numberOfStoneInPlayerR)
               elif(destination_square.player=="r"):
                   self.numberOfStoneInPlayerR.remove(new_index)
                   self.numberOfStoneInPlayerB.remove(index)
                   self.numberOfStoneInPlayerB.append(new_index)
                   destination_square.player = current_square.player[0]
                   current_square.player = current_square.player[1:]   
            return True
        # Move the piece
        destination_square.player = current_square.player[0]
        if(destination_square.player=="b"):
                  self.numberOfStoneInPlayerB.remove(index)
                  self.numberOfStoneInPlayerB.append(new_index)
                  print(self.numberOfStoneInPlayerB)
        elif(destination_square.player=="r"):
                  self.numberOfStoneInPlayerR.remove(index)
                  self.numberOfStoneInPlayerR.append(new_index)
                  print(self.numberOfStoneInPlayerR)
        current_square.player = current_square.player[1:]
       
                  
        print(f"Moved player {destination_square.player} from index {index} to index {new_index}.")
        return True
     # طباعة الصف مع الفصل بين العناصر بـ " | "


# Example Usage
board = LudoBoard()
board.board[1].player="r"
board.board[13].player="r"

board.numberOfStoneInPlayerR.append(1)
board.numberOfStoneInPlayerR.append(13)
board.print_board()
# Move a piece from index 0 by 5 steps
success = board.move_piece(1, 12)
if success:
    print("\nAfter moving:\n")
    board.print_board()
    print(board.numberOfStoneInPlayerR)
    print(board.numberOfStoneInPlayerB)
print(board.check_win())

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
            for cell in self.board[i:i + 15]:  # أخذ 15 عنصر من المصفوفة
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
        print(current_square.player)
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
            if(destination_square.player == current_square.player):
                destination_square.player = destination_square.player + current_square.player
                current_square.player = None
            elif (destination_square.player != current_square.player):
                if(destination_square.player == "b"):
                    self.numberOfStoneInPlayerB.remove(new_index)
                    destination_square.player = current_square.player
                    current_square.player = None
                elif(destination_square.player == "r"):
                    self.numberOfStoneInPlayerR.remove(new_index)
                    destination_square.player = current_square.player
                    current_square.player = None
            return True

        # Move the piece
        destination_square.player = current_square.player
        current_square.player = None
        print(f"Moved player {destination_square.player} from index {index} to index {new_index}.")
        return True

    def check_path_contains_end(self, value):
        """
        Check if the path contains the end within the given steps.
        :param value: The number of steps to check.
        :return: True if the path reaches an end square, otherwise False.
        """
        for i in range(len(self.board)):
            current_square = self.board[i]
            if current_square.player is not None:
                steps_remaining = value
                current_position = i

                while steps_remaining > 0:
                    current_position += 1

                    # Wrap around if we reach the end of the board
                    if current_position >= len(self.board):
                        current_position = 0

                    steps_remaining -= 1

                    # Check if we've reached an end square
                    if self.board[current_position].type in ["endR", "endB"]:
                        return True, value - steps_remaining

        return False, value


# Example Usage
board = LudoBoard()
board.board[1].player = "b"
board.board[6].player = "r"
board.numberOfStoneInPlayerB.append(1)
board.numberOfStoneInPlayerR.append(6)
board.print_board()
# Move a piece from index 0 by 5 steps
success = board.move_piece(1, 5)
if success:
    print("\nAfter moving:\n")
    board.print_board()
print(board.check_win())

# Check path contains end example
result, remaining = board.check_path_contains_end(10)
print(f"Path contains end: {result}, Remaining steps: {remaining}")








# # Place a piece on the board near the "end" square for player Red
# board.board[48].player = "r"  # Assume 'r' represents a red player
# steps = 5

# # Call the function and print the results
# result, remaining_steps = board.check_path_contains_end( steps)

# # Display test details
# print(f"Starting index: 48, Steps: {steps}")
# print(f"Result: {result}, Remaining Steps: {remaining_steps}")
# print(f"Expected: True (if end is within {steps} steps), Remaining Steps: {steps - 3}")  # Example expectation

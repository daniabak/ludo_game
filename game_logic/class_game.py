from class_square import Squares

from class_square import Squares

class LudoBoard:
    def __init__(self):
        # تمثيل الرقعة باستخدام مصفوفة أحادية
        self.board = []  # قائمة لتمثيل الرقعة
        self.initialize_board()  # استدعاء دالة لتعبئة الرقعة
        self.goalR=[None,None,None,None,]
        self.goalB=[None,None,None,None,]
        self.numberOfStoneInPlayerR=[]
        self.numberOfStoneInPlayerB=[]
    def initialize_board(self):
        # إنشاء الرقعة باستخدام كائنات Squares
        for i in range(52):  # مثال لمسار يحتوي على 52 خلية
            if i == 0:
                # أول خلية هي نقطة البداية للاعب 1
                self.board.append(Squares(player=1, type="startR"))
            elif i == 26:
                # منتصف الرقعة نقطة البداية للاعب 2
                self.board.append(Squares(player=2, type="startB"))
            elif i in [0, 13, 26, 39]:
                # خانات آمنة
                self.board.append(Squares(player=None, type="#"))
            elif i ==51:
                # خانات آمنة
                self.board.append(Squares(player=None, type="endR"))
            elif i ==25:
                # خانات آمنة
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
                if cell.type == "path":  # إذا كانت الخلية فارغة
                    row.append("   ")  # أضف مساحة فارغة
                else:
                    # أضف رمز الخلية إلى الصف
                    row.append(
                        f"{cell.type[0].upper()+cell.type[-1].upper()  }"
                    )
            print(" | ".join(row))  # طباعة الصف مع الفصل بين العناصر بـ " | "


# إنشاء الرقعة
board = LudoBoard()
board.print_board()
print(board.check_win())
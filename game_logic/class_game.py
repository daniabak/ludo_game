from ludo_game.game_logic.class_square import Squares


class Game:
    def __init__(self, x, y):  # تغيير هنا
        self.x = x
        self.y = y
        self.grid = [[None for _ in range(y)] for _ in range(x)]
        self.init()



#تهيئة الرقعة بقيم افتراضية
    def init(self):
        for i in range(self.x):
            for j in range(self.y):
                self.grid[i][j] = Squares(i, j, ".", 0, 0)



#تابع لنقدر نغير بحالة المربع من حيث مثلا عدد الاحجار يلي فيه ..الخ
    def set_square(self, x, y, color,is_safty,wall):
        self.grid[x][y] = Squares(x, y, color, is_safty, wall)




    def print(self):
        for i in range(self.x):
            for j in range(self.y):
                print(self.grid[i][j].color, end=" ")
            print()

from ludo_game.game_logic.class_square import Squares


class Game:
    def __init__(self, x, y):  # تغيير هنا
        self.x = x
        self.y = y
        self.grid = [[None for _ in range(y)] for _ in range(x)]
        self.init()



    #تهيئة الرقعة بقيم افتراضية
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = [[None for _ in range(y)] for _ in range(x)]
        self.init()

    # Initialize the grid with default values
    def init(self):
        for i in range(self.x):
            for j in range(self.y):
                self.grid[i][j] = Squares(i, j, ".", 0, ".")

        self.create_plus_shape()

    def set_square(self, x, y, color, is_safety, type, wall):
        self.grid[x][y] = Squares(x, y, color, is_safety, type, wall)

    def create_plus_shape(self):
        for i in range(self.x):
            self.grid[i][6].type = "#"
            self.grid[i][7].type = "#"
            self.grid[i][8].type = "#"

        for j in range(self.y):
            self.grid[6][j].type = "#"
            self.grid[7][j].type = "#"
            self.grid[8][j].type = "#"

        self.grid[7][7].type = "."
        self.grid[7][6].type = "."
        self.grid[7][5].type = "."
        self.grid[7][8].type = "."
        self.grid[7][9].type = "."
        self.grid[6][7].type = "."
        self.grid[8][7].type = "."

        self.grid[13][6].type = "r"
        self.grid[13][7].type = "r"
        self.grid[12][7].type = "r"
        self.grid[11][7].type = "r"
        self.grid[10][7].type = "r"
    
        self.grid[6][1].type = "g"
        self.grid[7][1].type = "g"
        self.grid[7][2].type = "g"
        self.grid[7][3].type = "g"
        self.grid[7][4].type = "g"

        self.grid[1][8].type = "b"
        self.grid[1][7].type = "b"
        self.grid[2][7].type = "b"
        self.grid[3][7].type = "b"
        self.grid[4][7].type = "b"

        self.grid[8][13].type = "y"
        self.grid[7][13].type = "y"
        self.grid[7][12].type = "y"
        self.grid[7][11].type = "y"
        self.grid[7][10].type = "y"

    def print(self):
        for i in range(self.x):
            for j in range(self.y):
                print(self.grid[i][j].type, end=" ")
            print()

    def print_path(self, path, path_color="*"):
        """
        Highlights a path on the grid.
        :param path: List of tuples representing the path [(x1, y1), (x2, y2), ...].
        :param path_color: Symbol or color to use for the path.
        """
        for x, y in path:
            self.grid[x][y].type = path_color

        self.print()

        for x, y in path:
            self.grid[x][y].type = "#"

    def canMoveTop(self, x, y):
        """
        Checks if the square above the given (x, y) position is '#'.
        :param x: Current x-coordinate.
        :param y: Current y-coordinate.
        :return: True if the square above is '#', False otherwise.
        """
        if x > 0:  # Ensure we don't go out of bounds
            return self.grid[x - 1][y].type == "#"
        return False


    def canMoveLeft(self, x, y):
        """
        Checks if the square to the left of the given (x, y) position is '#'.
        :param x: Current x-coordinate.
        :param y: Current y-coordinate.
        :return: True if the square to the left is '#', False otherwise.
        """
        if y > 0:  # Ensure we don't go out of bounds
            return self.grid[x][y - 1].type == "#"
        return False

    def canMoveBottom(self, x, y):
        """
        Checks if the square below the given (x, y) position is '#'.
        :param x: Current x-coordinate.
        :param y: Current y-coordinate.
        :return: True if the square below is '#', False otherwise.
        """
        if x < len(self.grid) - 1:  # Ensure we don't go out of bounds
            return self.grid[x + 1][y].type == "#"
        return False
        
    def canMoveRight(self, x, y):
        """
        Checks if the square to the right of the given (x, y) position is '#'.
        :param x: Current x-coordinate.
        :param y: Current y-coordinate.
        :return: True if the square to the right is '#', False otherwise.
        """
        if y < len(self.grid[0]) - 1:  # Ensure we don't go out of bounds
            return self.grid[x][y + 1].type == "#"
        return False
#تابع لنقدر نغير بحالة المربع من حيث مثلا عدد الاحجار يلي فيه ..الخ
    def set_square(self, x, y, color,is_safty,wall):
        self.grid[x][y] = Squares(x, y, color, is_safty, wall)




    def print(self):
        for i in range(self.x):
            for j in range(self.y):
                print(self.grid[i][j].color, end=" ")
            print()

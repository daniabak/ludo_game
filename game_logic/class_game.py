from class_square import Squares
class Game:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = [[None for _ in range(y)] for _ in range(x)]
        self.players = {"red": [(13, 6)], "blue": [(1, 8)]}  # Player piece positions
        self.init()

    def init(self):
        for i in range(self.x):
            for j in range(self.y):
                self.grid[i][j] = Squares(i, j, ".", 0, ".")
        self.create_plus_shape()

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

    def set_square(self, x, y, color, is_safety, wall, type="."):
        self.grid[x][y] = Squares(x, y, color, is_safety, type, wall)

    def print(self):
        for i in range(self.x):
            for j in range(self.y):
                # Print player color or square type
                print(self.grid[i][j].color if self.grid[i][j].color != "." else self.grid[i][j].type, end=" ")
            print()

    def move_piece(self, player, piece_index, steps):
        """
        Move a player's piece on the board.
        :param player: Player name ("red" or "blue")
        :param piece_index: Index of the piece to move
        :param steps: Number of steps
        """
        # Get the current position of the piece
        current_pos = self.players[player][piece_index]
        x, y = current_pos

        # Remove the piece from the current square
        self.grid[x][y].color = "."

        # Calculate the new position
        new_x = x
        new_y = y + steps  # Horizontal movement (example)
        if new_y >= self.y:  # Check for board boundaries
            print("You cannot move outside the board!")
            self.grid[x][y].color = player[0]  # Restore the piece to the previous square
            return False

        # Check if the new square is occupied
        if self.grid[new_x][new_y].color != ".":
            print("The square is occupied! The other player's piece will be sent back to the base.")
            other_player = self.grid[new_x][new_y].color
            self.return_piece_to_base(other_player)

        # Place the piece in the new position
        self.grid[new_x][new_y].color = player[0]
        self.players[player][piece_index] = (new_x, new_y)
        return True

    def return_piece_to_base(self, player):
        """Send a player's piece back to its starting position."""
        base = (13, 6) if player == "r" else (1, 8)
        for i, pos in enumerate(self.players[player]):
            if pos == base:
                continue  # Base is already occupied
            self.players[player][i] = base
            return

class Squares:
    def __init__(self, x, y, color, is_safety, type, wall=0):
        self.x = x
        self.y = y
        self.color = color
        self.wall = wall
        self.is_safety = is_safety
        self.type = type  # "." for normal, "#" for special

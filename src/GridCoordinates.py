class GridCoordinates:

    def __init__(self, col, row):
        self.col  = col
        self.row  = row

    def left(self):
        return GridCoordinates(self.col - 1, self.row)

    def right(self):
        return GridCoordinates(self.col + 1, self.row)

    def top(self):
        return GridCoordinates(self.col, self.row - 1)

    def bottom(self):
        return GridCoordinates(self.col, self.row + 1)

    def clone(self):
        return GridCoordinates(self.col, self.row)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.col == other.col and self.row == other.row
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash((self.col, self.row))

    def __str__(self):
        return "%d,%d" % (self.col, self.row)

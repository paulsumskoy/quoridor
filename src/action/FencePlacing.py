from src.action.IAction  import *
from src.interface.Fence import *

class FencePlacing(IAction):
    def __init__(self, coord, direction):
        self.coord     = coord
        self.direction = direction

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.coord == other.coord and self.direction == other.direction
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        #return hash(tuple(sorted(self.__dict__.items())))
        return hash((self.coord, self.direction))

    def __str__(self):
        vertical = (self.direction == Fence.DIRECTION.VERTICAL)
        return "%s-fence at %s" % ("V" if vertical else "H", self.coord)

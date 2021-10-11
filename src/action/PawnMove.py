from src.action.IAction import *

class PawnMove(IAction):
    def __init__(self, fromCoord, toCoord, throughCoord = None):
        self.fromCoord    = fromCoord
        self.toCoord      = toCoord
        self.throughCoord = throughCoord

    def isJump(self):
    	return (self.throughCoord is not None)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.fromCoord == other.fromCoord and self.toCoord == other.toCoord and self.throughCoord == other.throughCoord
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        #return hash(tuple(sorted(self.__dict__.items())))
        return hash((self.fromCoord, self.toCoord, self.throughCoord))

    def __str__(self):
    	return "from %s to %s%s" % (self.fromCoord, self.toCoord, " through %s" % self.throughCoord if self.throughCoord is not None else "") 

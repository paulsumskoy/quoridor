import random

from src.player.IBot    import *
from src.action.IAction import *



class RandomBot(IBot):
    def moveRandomly(self, board) -> IAction:
        validPawnMoves = board.storedValidPawnMoves[self.pawn.coord]
        return random.choice(validPawnMoves)

    def placeFenceRandomly(self, board) -> IAction:
        randomFencePlacing = random.choice(board.storedValidFencePlacings)
        attempts = 5
        while board.isFencePlacingBlocking(randomFencePlacing) and attempts > 0:
            randomFencePlacing = random.choice(board.storedValidFencePlacings)
            attempts -= 1
        if (attempts == 0):
            return self.moveRandomly()
        return randomFencePlacing

    def play(self, board) -> IAction:
        if random.randint(0, 2) == 0 and self.remainingFences() > 0 and len(board.storedValidFencePlacings) > 0:
            return self.placeFenceRandomly(board)
        else:
            return self.moveRandomly(board)

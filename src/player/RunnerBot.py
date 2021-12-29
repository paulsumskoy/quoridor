from src.player.IBot import *
from src.action.IAction import *
from src.Path import *


class RunnerBot(IBot):
    def moveAlongTheShortestPath(self, board) -> IAction:
        path = Path.BreadthFirstSearch(board, self.pawn.coord, self.endPositions, ignorePawns=False)
        if path is None:
            path = Path.BreadthFirstSearch(board, self.pawn.coord, self.endPositions, ignorePawns=True)
            firstMove = path.firstMove()
            if not board.isValidPawnMove(firstMove.fromCoord, firstMove.toCoord, ignorePawns=False):
                return None
        return path.firstMove()

    def play(self, board) -> IAction:
        return self.moveAlongTheShortestPath(board)

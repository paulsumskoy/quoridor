from src.player.IPlayer import *
from src.action.IAction import * 
from src.action.Quit    import *

class Human(IPlayer):
    def play(self, board) -> IAction:
        if not INTERFACE:
            raise Exception("")
        while True:
            key = board.window.getKey()
            if key == "p": 
                validPawnMoves = board.storedValidPawnMoves[self.pawn.coord] 
                board.displayValidPawnMoves(self, validPawnMoves)
                click = board.window.getMouse()
                pawnMove = board.getPawnMoveFromMousePosition(self.pawn, click.x, click.y)
                clickOnValidTarget = (pawnMove is not None)
                board.hideValidPawnMoves(self, validPawnMoves)
                if clickOnValidTarget:
                    return pawnMove
            if key == "f" and self.remainingFences() > 0:
                validFencePlacings = board.storedValidFencePlacings 
                
                click = board.window.getMouse()
                fencePlacing = board.getFencePlacingFromMousePosition(click.x, click.y)
                clickOnValidTarget = (fencePlacing is not None)
                
                if clickOnValidTarget:
                    return fencePlacing
            if key == "Escape":
                return Quit()

    def __str__(self):
        return "[HUMAN] %s (%s)" % (self.name, self.color.name)


import random
import time

from src.player.BuilderBot import *
from src.player.RunnerBot import *
from src.action.IAction import *


class BuildAndRunBot(BuilderBot, RunnerBot):
    def play(self, board) -> IAction:
        # если забора не осталось, передвинуть фишку
        if self.remainingFences() < 1 or len(board.storedValidFencePlacings) < 1:
            return self.moveAlongTheShortestPath(board)
        fencePlacingImpacts = self.computeFencePlacingImpacts(board)
        # если нет доступного забора, передвинуть фишку
        if len(fencePlacingImpacts) < 1:
            return self.moveAlongTheShortestPath(board)
        # наилучшее размещение фишки
        bestFencePlacing = self.getFencePlacingWithTheHighestImpact(fencePlacingImpacts)
        # если нет удобного расположения забора, передвинуть фишку
        if fencePlacingImpacts[bestFencePlacing] < 1:
            return self.moveAlongTheShortestPath(board)
        return bestFencePlacing

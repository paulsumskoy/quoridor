import random
import time

from src.player.RandomBot import *
from src.action.IAction   import *
from src.exception.PlayerPathObstructedException import *

class BuilderBot(RandomBot):
    def computeFencePlacingImpacts(self, board):
        fencePlacingImpacts = {}
        for fencePlacing in board.storedValidFencePlacings:
            try:
                impact = board.getFencePlacingImpactOnPaths(fencePlacing)
            except PlayerPathObstructedException as e:
                continue
            globalImpact = 0
            for playerName in impact:
                globalImpact += (-1 if playerName == self.name else 1) * impact[playerName]
            fencePlacingImpacts[fencePlacing] = globalImpact
        return fencePlacingImpacts

    def getFencePlacingWithTheHighestImpact(self, fencePlacingImpacts):
        return max(fencePlacingImpacts, key = fencePlacingImpacts.get)

    def play(self, board) -> IAction:
        if self.remainingFences() < 1 or len(board.storedValidFencePlacings) < 1:
            return self.moveRandomly(board)
        fencePlacingImpacts = self.computeFencePlacingImpacts(board)

        if len(fencePlacingImpacts) < 1:
            return self.moveRandomly(board)
        
        bestFencePlacing = self.getFencePlacingWithTheHighestImpact(fencePlacingImpacts)
        
        if fencePlacingImpacts[bestFencePlacing] < 1:
            return self.moveRandomly(board)
        return bestFencePlacing

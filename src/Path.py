import math

from src.Settings        import *
from src.action.PawnMove import *

class Path:

    def __init__(self, moves):
        self.moves = moves

    def length(self):
        return len(self.moves)

    def startCoord(self):
        return self.moves[0].fromCoord

    def endCoord(self):
        return self.moves[-1].toCoord

    def firstMove(self):
        return self.moves[0]

    def __str__(self):
        return "[%s] -> %s" % (str(self.startCoord()), " -> ".join(map(lambda move:str(move.toCoord), self.moves)))

    def ManhattanDistance(fromCoord, toCoord):
        return abs(toCoord.col - fromCoord.col) + abs(toCoord.row - fromCoord.row)

    def ManhattanDistanceMulti(fromCoord, toCoords):
        minManhattanDistance = math.inf
        for toCoord in toCoords:
            manhattanDistance = Path.ManhattanDistance(fromCoord, toCoord)
            if manhattanDistance < minManhattanDistance:
                minManhattanDistance = manhattanDistance
        return minManhattanDistance

    def BreadthFirstSearch(board, startCoord, endCoords, ignorePawns = False):
        global TRACE
        TRACE["Path.BreadthFirstSearch"] += 1
        root = PawnMove(None, startCoord)

        previousMoves = {startCoord: root}
        nextMoves = [root]
        validPawnMoves = board.storedValidPawnMovesIgnoringPawns if ignorePawns else board.storedValidPawnMoves
        
        while nextMoves:
            move = nextMoves.pop(0)
            for endCoord in endCoords:
                
                if move.toCoord == endCoord:
                    
                    pathMoves = [move]
                    while move.fromCoord is not None:
                        move = previousMoves[move.fromCoord]
                        pathMoves.append(move)
                    pathMoves.reverse()
                    return Path(pathMoves[1:])
            
            validMoves = validPawnMoves[move.toCoord]
            
            sorted(validMoves, key=lambda validMove: Path.ManhattanDistanceMulti(validMove.toCoord, endCoords))
            for validMove in validMoves:
                if validMove.toCoord not in previousMoves:
                    previousMoves[validMove.toCoord] = validMove
                    nextMoves.append(validMove)
        return None

    def DepthFirstSearch():
        pass

    def Dijkstra(board, startCoord, endCoords, moveScore = lambda move, step: 1, ignorePawns = False):
        global TRACE
        TRACE["Path.Dijkstra"] += 1
        root = PawnMove(None, startCoord)

        previousMoves = {startCoord: (0, root)}
        nextMoves = [(0, 0, root)]
        validPawnMoves = board.storedValidPawnMovesIgnoringPawns if ignorePawns else board.storedValidPawnMoves
        while nextMoves:
            sorted(nextMoves, key=lambda nextMove: nextMove[1])
            (step, score, move) = nextMoves.pop(0)
            for endCoord in endCoords:
                if move.toCoord == endCoord:
                    pathMoves = [move]
                    while move.fromCoord is not None:
                        move = previousMoves[move.fromCoord][1]
                        pathMoves.append(move)
                    pathMoves.reverse()
                    return Path(pathMoves[1:])
            validMoves = validPawnMoves[move.toCoord]

            sorted(validMoves, key=lambda validMove: Path.ManhattanDistanceMulti(validMove.toCoord, endCoords))
            for validMove in validMoves:
                validMoveScore = score + moveScore(validMove, step + 1)
                if validMove.toCoord not in previousMoves:
                    previousMoves[validMove.toCoord] = (validMoveScore, validMove)
                    nextMoves.append((step + 1, validMoveScore, validMove))
                if validMoveScore < previousMoves[validMove.toCoord][0]:
                    previousMoves[validMove.toCoord] = (validMoveScore, validMove)
        return None

    def AStar():
        pass

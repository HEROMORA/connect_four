import numpy as np

from models.state import State
from models.node_type import NodeType
from models.pruning import Pruning
from scoreCalculation import *


# Chip Color
# Red --> Model
# Blue --> User


def maximize(boardState, k):  # boardState is state object, k is number of levels
    if not k:
        boardState.cost = boardState.evaluate_state()  # End of tree, get score using heuristics
        return boardState, boardState.cost

    if boardState.is_full_board():  # Full Board
        boardState.cost = getScore(boardState, 'r')
        return boardState, boardState.cost

    maxChild = None
    maxScore = -np.inf
    for child in boardState.children:
        childNode = State(child, NodeType.mini, Pruning(0, 0))
        node, cost = minimize(childNode, k - 1)
        childNode.cost = cost

        if cost > maxScore:
            maxChild, maxScore = childNode, cost

    return maxChild, maxScore


def minimize(boardState, k):
    if not k:
        boardState.cost = boardState.evaluate_state()  # End of tree, get score using heuristics
        return boardState, boardState.cost

    if boardState.is_full_board():
        boardState.cost = getScore(boardState, 'b')
        return boardState, boardState.cost

    minChild = None
    minScore = np.inf
    for child in boardState.children:
        childNode = State(child, NodeType.max, Pruning(0, 0))
        node, cost = maximize(childNode, k - 1)
        childNode.cost = cost

        if cost < minScore:
            minChild, minScore = childNode, cost

    return minChild, minScore


def decide(boardState, k, prune, color):
    if not prune:
        if color == 'r':
            node, cost = maximize(boardState, k)
        else:
            node, cost = minimize(boardState, k)
    return node, cost

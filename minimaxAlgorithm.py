import numpy as np

from models.state import State
from models.constants import *


# Chip Color
# Red --> Model (MAXIMIZER)
# Blue --> User (MINIMIZER)


def maximize(board_state: State, k: int, prune: bool):  # boardState is state object, k is number of levels
    if not k or board_state.is_full_board():
        board_state.evaluate_set_cost()  # End of tree, get score using heuristics
        return board_state

    maxChild = None
    board_state.generate_children()
    for child in board_state.children:
        min_child = minimize(child, k - 1, prune)

        if maxChild is None or min_child.cost > maxChild.cost:
            maxChild = child
            maxChild.cost = min_child.cost

        if prune:
            if(maxChild.cost >= child.pruning.beta):
                break
            child.pruning.alpha = max(maxChild.cost, child.pruning.alpha)  # Update alpha


    return maxChild


def minimize(board_state: State, k: int, prune: bool):
    if not k or board_state.is_full_board():
        board_state.evaluate_set_cost()  # End of tree, get score using heuristics
        return board_state

    minChild = None
    board_state.generate_children()
    for child in board_state.children:
        max_child = maximize(child, k - 1, prune)

        if minChild is None or max_child.cost < minChild.cost:
            minChild = child
            minChild.cost = max_child.cost

        if prune:
            if(minChild.cost <= child.pruning.alpha):
                break
            child.pruning.beta = min(minChild.cost, child.pruning.beta)  # Update beta

    return minChild


def decide(board_state: State, k: int, prune: bool, color: str):
    node = None
    # TODO: USE OR NON USE PRUNING
    if color == red:
        node = maximize(board_state, k, prune)
    else:
        node = minimize(board_state, k, prune)
    return node

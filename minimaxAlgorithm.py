import numpy as np

from models.state import State
from models.constants import *


# Chip Color
# Red --> Model (MAXIMIZER)
# Blue --> User (MINIMIZER)


def maximize(board_state: State, k: int):  # boardState is state object, k is number of levels
    if not k or board_state.is_full_board():
        board_state.evaluate_set_cost()  # End of tree, get score using heuristics
        return board_state

    maxChild = None
    board_state.generate_children()
    for child in board_state.children:
        min_child = minimize(child, k - 1)

        if maxChild is None or min_child.cost > maxChild.cost:
            maxChild = min_child
            maxChild.pruning.alpha = max(maxChild.cost, maxChild.pruning.alpha) # Updating alpha

        # Break on pruning
        if maxChild.pruning.alpha > maxChild.pruning.beta:
            return maxChild

    return maxChild


def minimize(board_state: State, k: int):
    if not k or board_state.is_full_board():
        board_state.evaluate_set_cost()  # End of tree, get score using heuristics
        return board_state

    minChild = None
    board_state.generate_children()
    for child in board_state.children:
        max_child = maximize(child, k - 1)

        if minChild is None or max_child.cost < minChild.cost:
            minChild = max_child
            minChild.pruning.beta = min(minChild.cost, minChild.pruning.beta)  # Update beta

        # Break on pruning
        if minChild.pruning.alpha > minChild.pruning.beta:
            return minChild

    return minChild


def decide(board_state: State, k: int, prune: bool, color: str):
    node = None
    if not prune:
        if color == red:
            node = maximize(board_state, k)
        else:
            node = minimize(board_state, k)
    return node

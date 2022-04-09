import numpy as np

from models.state import State
from models.constants import *
from treelib import Tree
import time

# Chip Color
# Red --> Model (MAXIMIZER)
# Blue --> User (MINIMIZER)


def maximize(board_state: State, k: int, prune: bool, tree):  # boardState is state object, k is number of levels
    if not k or board_state.is_full_board():
        board_state.evaluate_set_cost()  # End of tree, get score using heuristics
        return board_state

    maxChild = None
    board_state.generate_children()
    for child in board_state.children:
        
        n = tree.create_node(child.cost, child.id, parent=board_state.id)
        min_child = minimize(child, k - 1, prune, tree)

        n.tag = min_child.cost
        if maxChild is None or min_child.cost > maxChild.cost:
            maxChild = child
            maxChild.cost = min_child.cost

            if prune:
                maxChild.pruning.alpha = max(maxChild.cost, maxChild.pruning.alpha) # Updating alpha

        # Break on pruning
        if prune and maxChild.pruning.alpha > maxChild.pruning.beta:
            return maxChild

    return maxChild


def minimize(board_state: State, k: int, prune: bool, tree):
    if not k or board_state.is_full_board():
        board_state.evaluate_set_cost()  # End of tree, get score using heuristics
        return board_state

    minChild = None
    board_state.generate_children()

    for child in board_state.children:

        n = tree.create_node(child.cost, child.id, parent=board_state.id)
        max_child = maximize(child, k - 1, prune, tree)
        
        n.tag = max_child.cost
        if minChild is None or max_child.cost < minChild.cost:
            minChild = child
            minChild.cost = max_child.cost

            if prune:
                minChild.pruning.beta = min(minChild.cost, minChild.pruning.beta)  # Update beta

        # Break on pruning
        if prune and minChild.pruning.alpha > minChild.pruning.beta:
            return minChild

    return minChild


def decide(board_state: State, k: int, prune: bool, color: str):
    node = None
    tree = Tree()
    root = tree.create_node(board_state.cost, board_state.id)
    time1 = time.time()

    if color == red:
        node = maximize(board_state, k, prune, tree)
    else:
        node = minimize(board_state, k, prune, tree)


    root.tag = node.cost
    totalTime = time.time() - time1
    tree.show()
    print(totalTime)
    return node

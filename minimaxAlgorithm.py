from models.pruning import Pruning
from models.state import State
from treelib import Tree
import time


# Chip Color
# Red --> Model (MAXIMIZER)
# Blue --> User (MINIMIZER)


def maximize(board_state: State, k: int, prune: bool, tree, alpha: int, beta: int):  # boardState is state object, k is number of levels
    if not k or board_state.is_full_board():
        score = board_state.evaluate_set_cost()  # End of tree, get score using heuristics
        return None, score

    maxChild = None
    max_utility = -float('inf')

    board_state.generate_children()
    for child in board_state.children:

        n = tree.create_node(f'{child.node_type}:{0}', child.id, parent=board_state.id)
        _, utility = minimize(child, k - 1, prune, tree, alpha, beta)

        n.tag = f'{child.node_type}:{utility}'
        if maxChild is None or utility > max_utility:
            maxChild = child
            max_utility = utility

        if prune:

            if max_utility >= beta:
                break

            alpha = max(max_utility, alpha)  # Update alpha

    return maxChild, max_utility


def minimize(board_state: State, k: int, prune: bool, tree, alpha, beta):
    if not k or board_state.is_full_board():
        score = board_state.evaluate_set_cost()  # End of tree, get score using heuristics
        return None, score

    minChild = None
    min_utility = float('inf')
    board_state.generate_children()

    for child in board_state.children:

        n = tree.create_node(f'{child.node_type}:{0}', child.id, parent=board_state.id)
        _, utility = maximize(child, k - 1, prune, tree, alpha, beta)

        n.tag = f'{child.node_type}:{utility}'
        if minChild is None or utility < min_utility:
            minChild = child
            min_utility = utility

        if prune:

            if min_utility <= alpha:
                break

            beta = min(min_utility, beta)  # Update beta

    return minChild, min_utility


def decide(board_state: State, k: int, prune: bool, color: str):
    node = None
    tree = Tree()
    root = tree.create_node(f'{board_state.node_type}:{0}', board_state.id)
    time1 = time.time()

    pruning = Pruning(-float('inf'), float('inf'))
    node, utility = maximize(board_state, k, prune, tree, pruning.alpha, pruning.beta)

    root.tag = f'{board_state.node_type}:{utility}'
    totalTime = time.time() - time1
    tree.show()
    print(totalTime)
    return node

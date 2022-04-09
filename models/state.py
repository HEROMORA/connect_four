from models.node_type import NodeType
from models.pruning import Pruning
from scoreCalculation import *
from models.constants import *
from uuid import uuid4

# We will use String for representing the board
# R - Red Tile
# B - Blue Tile
# X - Empty Tile

# for the board representation the index 0 is the lower-left bit

#   10 11 12 13 14
#   5  6  7  8  9
#   0  1  2  3  4


class State:

    def __init__(self, sequence: str, node_type: NodeType, pruning: Pruning):
        self.id = uuid4()
        self.sequence = sequence
        self.node_type = node_type
        self.pruning = pruning
        self.cost = -1
        self.children = []

        assert len(self.sequence) == width * height

    def evaluate_set_cost(self):
        score = get_score(self.sequence, red if self.node_type == NodeType.max else blue)
        self.cost = score
        return score

    def generate_children(self):
        color = red if self.node_type == NodeType.max else blue
        current_sequence = self.sequence

        for i in range(width):
            childSequence = self.sequence[i::width]

            if empty not in childSequence:
                continue

            index = childSequence.index(empty) * width + i
            childSequence = current_sequence[:index] + color + current_sequence[index + 1:]

            childNodeType = self.get_child_node_type()
            childState = State(childSequence, childNodeType, self.pruning)
            self.children.append(childState)

    def is_full_board(self):
        for i in range(width):
            index = (width * (height - 1)) + i
            if self.sequence[index] == empty:
                return False

        return True

    def get_child_node_type(self):
        if self.node_type == NodeType.max:
            return NodeType.mini

        return NodeType.max

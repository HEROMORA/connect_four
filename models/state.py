from models.node_type import NodeType
from models.pruning import Pruning

# We will use String for representing the board
# R - Red Tile
# B - Blue Tile
# X - Empty Tile

# for the board representation the index 0 is the lower-left bit

#   10 11 12 13 14
#   5  6  7  8  9
#   0  1  2  3  4

# TODO: Check to move these constants to somewhere more global
width = 7
height = 6

red = 'r'
blue = 'b'
empty = '0'


class State:

    def __init__(self, sequence: str, node_type: NodeType, pruning: Pruning):
        self.sequence = sequence
        self.node_type = node_type
        self.pruning = pruning
        self.cost = -1
        self.children = self.generate_children()

        assert len(self.sequence) == width * height

    # TODO: IMPLEMENT evaluation
    def evaluate_state(self):
        return self.cost + 93

    # TODO: return a list of possible children to the state @yosra
    def generate_children(self):
        return []

    def is_full_board(self):
        for i in range(width):
            index = (width * (height - 1)) + i
            if self.sequence[index] == empty:
                return False

        return True


# Press the green button in the gutter to run the script.
from models.node_type import NodeType
from models.pruning import Pruning
from models.state import State


if __name__ == '__main__':
    sample_seq = "rbr000b00000000000000000000000000000000000"
    sample_state = State(sample_seq, NodeType.max, Pruning(0, 0))

    print(sample_state.is_full_board())


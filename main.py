# Press the green button in the gutter to run the script.
from models.node_type import NodeType
from models.pruning import Pruning
from models.state import State
from minimaxAlgorithm import *
from scoreCalculation import *
from queue import PriorityQueue
from GUI.gui import main as gui


if __name__ == '__main__':
    # sample_seq = 'rrr0rrrbbb0bbb0000000000000000000000000000'
    # sample_state = State(sample_seq, NodeType.max, Pruning(-float('inf'), float('inf')))

    # # print(sample_state.is_full_board())
    # node = decide(sample_state, 2, False, red)
    # test = '123456712345671234567123456712345671234567'
    # seq = 'rrrbbbbrrrrbbrbrrrbbrrrrrbrrrbbbbbrrbbbbrr'

    gui()


    # print(getDiagonal(seq, 14))
    # print(getScore(seq, 'r'))
    # print(getScore(seq, 'b'))

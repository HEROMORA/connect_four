from models.constants import *


#   15 16 17 18 19
#   10 11 12 13 14
#   5  6  7  8  9
#   0  1  2  3  4

def is_unique_vector(vector: str, color: str):
    unique_values = set(vector)
    if len(unique_values) == 1 and unique_values.pop() == color:
        return True

    return False


def loop_tiles(sequence: str, count: int, color: str, evaluation_function):
    total_score = 0

    # Counting horizontal counts
    for i in range(height):
        bias = i * width
        for j in range(width - count):
            index = bias + j
            row = sequence[index: index + count]
            total_score = evaluation_function(total_score, row, color)

    # Counting vertical counts
    for i in range(height - count + 1):
        for j in range(width):
            start = (i * width) + j
            end = start + (width * count)
            column = sequence[start:end:width]
            total_score = evaluation_function(total_score, column, color)

    # Counting forward diagonals
    for i in range(height - count + 1):
        for j in range(width - count + 1):
            start = (i * width) + j
            step = width + 1
            end = start + (width * (count - 1)) + count
            diagonal = sequence[start:end:step]
            total_score = evaluation_function(total_score, diagonal, color)

    # Counting inverse diagonals
    for i in range(height - count + 1):
        for j in range(width - 1, count - 2, -1):
            start = (i * width) + j
            dec_step = width - 1
            end = start + (dec_step * (count - 1)) + 1
            inv_diagonal = sequence[start:end:dec_step]
            total_score = evaluation_function(total_score, inv_diagonal, color)

    return total_score


def get_abs_score(sequence: str):
    return get_score(sequence, red) - get_score(sequence, blue)


def get_score(sequence: str, color: str):
    # Other herustics to be added here
    fours = count_fours(sequence, color) * 50

    # fours = 0
    possibleSixs = count_possibles_combs(sequence, 6, color) * 20
    possibleFours = count_possibles_combs(sequence, 4, color) * 6
    possibleThrees = count_possibles_combs(sequence, 3, color) * 3
    possibleTwos = count_possibles_combs(sequence, 2, color) * 2
    score = possibleTwos + possibleThrees + possibleFours + possibleSixs + fours

    return score


# Count possible combinations


def count_possibles_combs(sequence: str, count: int, color: str):
    return loop_tiles(sequence, count, color, evaluate_possible_combination)


# TODO : Keep in mind increasing diagonals
# TODO: middles are weaker
def evaluate_possible_combination(score, vector, color):
    emptyDigits = 0
    for x in vector:
        if (x is not color and x is not empty) or emptyDigits > 1:
            return 0

        if x is empty:
            emptyDigits += 1

    return score + emptyDigits


# Count Evaluation Heruistics
def count_fours(sequence: str, color: str):
    return loop_tiles(sequence, 4, color, evaluate_count)


def evaluate_count(score, vector, color):
    if is_unique_vector(vector, color):
        return score + 1
    return score

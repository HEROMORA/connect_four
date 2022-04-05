def getDiagonal(boardState, index, inverse):
    value = index
    if inverse:
        remainder = 0
        increment = 6
    else:
        remainder = 6
        increment = 8
    chunk = ''
    while value < 42:
        chunk += boardState[value]
        if value % 7 == remainder:  # index reached the last column
            break
        value += increment
    return chunk


def calculateScore(chunk, color):
    score = 0
    if len(chunk) > 3:
        for i in range((len(chunk) % 4) + 1):  # range --> number of 4's in the given string
            uniqueValues = list(set(chunk[i:i + 4]))  # get unique values in each 4 chars, 'bbbb' returns ['b']
            if len(uniqueValues) == 1 and uniqueValues[0] == color:
                score += 1
    return score


def getScore(boardState, color):  # boardState is String (sequence)
    j = 0
    score = 0

    for i in range(6):  # get score of each row
        row = boardState[j:j + 7]
        j += 7
        score += calculateScore(row, color)

    for i in range(7):  # get score of each column
        column = boardState[i::7]
        score += calculateScore(column, color)

    for i in range(7):  # get score of Diagonal and inverse diagonal starting from the bottom
        diagonal = getDiagonal(boardState, i, False)
        score += calculateScore(diagonal, color)
        invDiagonal = getDiagonal(boardState, i, True)
        score += calculateScore(invDiagonal, color)

    for i in range(6):  # get score of Diagonal and inverse diagonal starting from the left
        diagonal = getDiagonal(boardState, i + 7, False)
        score += calculateScore(diagonal, color)

    for i in range(6, 41, 7):  # get score of Diagonal and inverse diagonal starting from the right
        invDiagonal = getDiagonal(boardState, i, True)
        score += calculateScore(invDiagonal, color)

    return score

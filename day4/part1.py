guessNums = []
boards = []

# create boards
with open("./day4-input.txt", "r") as f:
    guessNums = [int(num) for num in (f.readline().split(","))]
    board = []
    count = 0
    for line in f:
        if len(line.replace("\n", "")):
            board.append([int(num) for num in line.split()])
            count += 1
        if count % 5 == 0 and board:
            boards.append(board)
            board = []

def checkBoard(board, row, col):
    bingo = True
    for num in board[row]:
        if num > -1:
            bingo = False
            break

    if not bingo:
        bingo = True
        for row in board:
            if row[col] > -1:
                bingo = False
                break

    return bingo

def calculateScore(board, bingoNum):
    score = 0
    for rows in board:
        for num in rows:
            if num > -1:
                score += num

    return score * bingoNum

def guess():
    score = -1
    for guessNum in guessNums:
        for board in boards:
            guessed = False
            for rowNum in range(0, len(board[0])):
                row = board[rowNum]
                for col in range(0, len(row)):
                    if guessNum == row[col]:
                        if row[col] == 0:
                            row[col] = -1
                        else:
                            row[col] = -row[col]
                        guessed = True
                        break

                if guessed:
                    break

            if checkBoard(board, rowNum, col):
                score = calculateScore(board, guessNum)
                if score > -1:
                    return score

print(guess())
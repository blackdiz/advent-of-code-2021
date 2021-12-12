guess_nums = []
boards = []

# create boards
with open("./day4-input.txt", "r") as f:
    guess_nums = [int(num) for num in (f.readline().split(","))]
    board = []
    count = 0
    for line in f:
        if len(line.replace("\n", "")):
            board.append([int(num) for num in line.split()])
            count += 1
        if count % 5 == 0 and board:
            boards.append(board)
            board = []

def check_board(board, row, col):
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

def calculate_score(board, bingo_num):
    score = 0
    for rows in board:
        for num in rows:
            if num > -1:
                score += num

    return score * bingo_num

def guess():
    score = -1
    for guess_num in guess_nums:
        for board in boards:
            guessed = False
            for row_num in range(0, len(board[0])):
                row = board[row_num]
                for col in range(0, len(row)):
                    if guess_num == row[col]:
                        if row[col] == 0:
                            row[col] = -1
                        else:
                            row[col] = -row[col]
                        guessed = True
                        break

                if guessed:
                    break

            if check_board(board, row_num, col):
                score = calculate_score(board, guess_num)
                if score > -1:
                    return score

print(guess())
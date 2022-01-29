def flash(matrix, row, column):
    flashes = 1
    matrix[row][column] = -1
    top_row = row - 1
    if top_row >= 0:
        if column - 1 >= 0 and matrix[top_row][column - 1] != -1:
            matrix[top_row][column - 1] = matrix[top_row][column - 1] + 1
            if matrix[top_row][column - 1] > 9:
                flashes = flashes + flash(matrix, top_row, column - 1)
        if column >= 0 and matrix[top_row][column] != -1:
            matrix[top_row][column] = matrix[top_row][column] + 1
            if matrix[top_row][column] > 9:
                flashes = flashes + flash(matrix, top_row, column)
        if  column + 1 < len(matrix[top_row]) and matrix[top_row][column + 1] != -1:
            matrix[top_row][column + 1] = matrix[top_row][column + 1] + 1
            if matrix[top_row][column + 1] > 9:
                flashes = flashes + flash(matrix, top_row, column + 1)

    if  column - 1 >= 0 and matrix[row][column - 1] != -1:
        matrix[row][column - 1] = matrix[row][column - 1] + 1
        if matrix[row][column - 1] > 9:
            flashes = flashes + flash(matrix, row, column - 1)
    if  column + 1 < len(matrix[row]) and matrix[row][column + 1] != -1:
        matrix[row][column + 1] = matrix[row][column + 1] + 1
        if matrix[row][column + 1] > 9:
            flashes = flashes + flash(matrix, row, column + 1)

    under_row = row + 1
    if under_row < len(matrix):
        if column - 1 >= 0 and matrix[under_row][column - 1] != -1:
            matrix[under_row][column - 1] = matrix[under_row][column - 1] + 1
            if matrix[under_row][column - 1] > 9:
                flashes = flashes + flash(matrix, under_row, column - 1)
        if column >= 0 and matrix[under_row][column] != -1:
            matrix[under_row][column] = matrix[under_row][column] + 1
            if matrix[under_row][column] > 9:
                flashes = flashes + flash(matrix, under_row, column)
        if column + 1 < len(matrix[under_row]) and matrix[under_row][column + 1] != -1:
            matrix[under_row][column + 1] = matrix[under_row][column + 1] + 1
            if matrix[under_row][column + 1] > 9:
                flashes = flashes + flash(matrix, under_row, column + 1)

    return flashes


with open('./day11-input.txt', 'r') as f:
    matrix = [[int(row) for row in rows.replace('\n', '')] for rows in f.readlines()]

    step = 1
    while True:
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] > -1:
                    matrix[row][column] = matrix[row][column] + 1
                    if matrix[row][column] > 9:
                        flash(matrix, row, column)

        all_bright = True
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] == -1:
                    matrix[row][column] = 0
                else:
                    all_bright = False

        if all_bright == True:
            print(step)
            break

        step = step + 1
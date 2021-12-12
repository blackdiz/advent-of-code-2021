with open("./day5-input.txt", "r") as f:
    coordinate = []
    for line in f:
        coordinate.append([[int(c) for c in coordinates.split(",")] for coordinates in line.replace("\n", "").split(" -> ")])

    dot_count = 0
    matrix = {}
    for i in range(0, 9):
        matrix[i] = matrix.get(i, {})
        for j in range(0, 10):
            matrix[i][j] = 0
    for co in coordinate:
        x1 = co[0][0]
        y1 = co[0][1]
        x2 = co[1][0]
        y2 = co[1][1]

        if x1 == x2: # vertical line
            for y in range(min(y1, y2), max(y1, y2) + 1):
                vertical_line = matrix.get(y, {})
                vertical_line[x1] = vertical_line.get(x1, 0)
                vertical_line[x1] += 1
                if vertical_line[x1] == 2:
                    dot_count += 1
                matrix[y] = vertical_line
        elif y1 == y2: # horizontal line
            horizontal_line = matrix.get(y1, {})

            for x in range(min(x1, x2), max(x1, x2) + 1):
                horizontal_line[x] = horizontal_line.get(x, 0)
                horizontal_line[x] += 1
                if horizontal_line[x] == 2:
                    dot_count += 1

            matrix[y1] = horizontal_line
        elif abs((x1 - x2) / (y1 - y2)) == 1: # diagonal line
            if x1 <= x2:
                start_x = x1
                start_y = y1
                end_x = x2
            else:
                start_x = x2
                start_y = y2
                end_x = x1

            while start_x != end_x + 1:
                line = matrix.get(start_y, {})
                line[start_x] = line.get(start_x, 0)
                line[start_x] += 1
                matrix[start_y] = line
                if (line[start_x] == 2):
                    dot_count += 1

                start_x += 1
                if (x1 - x2) / (y1 - y2) > 0: # direction is right down
                    start_y += 1
                else: # direction is right up
                    start_y -= 1

    print(dot_count)
with open("./day5-input.txt", "r") as f:
    coordinate = []
    for line in f:
        coordinate.append([[int(c) for c in coordinates.split(",")] for coordinates in line.replace("\n", "").split(" -> ")])

    dot_count = 0
    matrix = {}
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

    print(dot_count)
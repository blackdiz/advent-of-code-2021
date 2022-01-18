with open('./day9-input.txt', 'r') as f:
    heightmap = [list(row.replace('\n', '')) for row in f.readlines()]
    risk_level = 0
    for i, locations in enumerate(heightmap):
        for j, height in enumerate(locations):
            if j + 1 < len(locations) and locations[j + 1] <= height:
                continue
            if j - 1 >= 0 and locations[j - 1] <= height:
                continue
            if i - 1 >= 0 and heightmap[i - 1][j] <= height:
                continue
            if i + 1 < len(heightmap) and heightmap[i + 1][j] <= height:
                continue

            risk_level = risk_level + int(height) + 1

    print(risk_level)

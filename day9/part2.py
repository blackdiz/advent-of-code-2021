def find_low_locations(heightmap):
    low_locations = []
    for y, locations in enumerate(heightmap):
        for x, height in enumerate(locations):
            if x + 1 < len(locations) and locations[x + 1] <= height:
                continue
            if x - 1 >= 0 and locations[x - 1] <= height:
                continue
            if y - 1 >= 0 and heightmap[y - 1][x] <= height:
                continue
            if y + 1 < len(heightmap) and heightmap[y + 1][x] <= height:
                continue

            low_locations.append({'x': x, 'y': y})

    return low_locations

def calc_basin_size(heightmap, coordinates, size):
    x = coordinates['x']
    y = coordinates['y']
    heightmap[y][x] = 9
    size = size + 1
    if x - 1 >= 0 and heightmap[y][x - 1] < 9:
        size = calc_basin_size(heightmap, {'x': x - 1, 'y': y}, size)
    if x + 1 < len(heightmap[y]) and heightmap[y][x + 1] < 9:
        size = calc_basin_size(heightmap, {'x': x + 1, 'y': y}, size)
    if y - 1 >= 0 and heightmap[y - 1][x] < 9:
        size = calc_basin_size(heightmap, {'x': x, 'y': y - 1}, size)
    if y + 1 < len(heightmap) and heightmap[y + 1][x] < 9:
        size = calc_basin_size(heightmap, {'x': x, 'y': y + 1}, size)

    return size

with open('./day9-input.txt', 'r') as f:
    heightmap = [list(map(lambda n: int(n), list(row.replace('\n', '')))) for row in f.readlines()]
    basin_sizes = []
    for coordinates in find_low_locations(heightmap):
        size = calc_basin_size(heightmap, coordinates, 0)
        if len(basin_sizes) < 3:
            basin_sizes.append(size)
        else:
            if min(basin_sizes) < size:
                basin_sizes[basin_sizes.index(min(basin_sizes))] = size

    result = 1
    for i in range(3):
        result = result * basin_sizes[i]

    print(result)

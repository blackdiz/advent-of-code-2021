list = []
with open('./day3-input.txt', 'r') as f:
    list = [line.replace('\n', '') for line in f]

def find_oxygen(list, pos, final_pos):
    if pos == final_pos or len(list) == 1:
        return int(list[0], 2)

    ones = 0
    zeros = 0
    groups = [[], []]
    for num in list:
        if num[pos] == '1':
            ones += 1
            groups[1].append(num)
        else:
            zeros += 1
            groups[0].append(num)

    if ones >= zeros:
        return find_oxygen(groups[1], pos + 1, final_pos)
    else:
        return find_oxygen(groups[0], pos + 1, final_pos)

def find_co2(list, pos, final_pos):
    if pos == final_pos or len(list) == 1:
        return int(list[0], 2)

    ones = 0
    zeros = 0
    groups = [[], []]
    for num in list:
        if num[pos] == '1':
            ones += 1
            groups[1].append(num)
        else:
            zeros += 1
            groups[0].append(num)

    if ones < zeros:
        return find_co2(groups[1], pos + 1, final_pos)
    else:
        return find_co2(groups[0], pos + 1, final_pos)

print(find_oxygen(list, 0, 12) * find_co2(list, 0, 12))
list = []
with open("./day3-input.txt", "r") as f:
    list = [line.replace("\n", "") for line in f]

def findOxygen(list, pos, finalPos):
    if pos == finalPos or len(list) == 1:
        return int(list[0], 2)

    ones = 0
    zeros = 0
    groups = [[], []]
    for num in list:
        if num[pos] == "1":
            ones += 1
            groups[1].append(num)
        else:
            zeros += 1
            groups[0].append(num)

    if ones >= zeros:
        return findOxygen(groups[1], pos + 1, finalPos)
    else:
        return findOxygen(groups[0], pos + 1, finalPos)

def findCO2(list, pos, finalPos):
    if pos == finalPos or len(list) == 1:
        return int(list[0], 2)

    ones = 0
    zeros = 0
    groups = [[], []]
    for num in list:
        if num[pos] == "1":
            ones += 1
            groups[1].append(num)
        else:
            zeros += 1
            groups[0].append(num)

    if ones < zeros:
        return findCO2(groups[1], pos + 1, finalPos)
    else:
        return findCO2(groups[0], pos + 1, finalPos)

print(findOxygen(list, 0, 12) * findCO2(list, 0, 12))
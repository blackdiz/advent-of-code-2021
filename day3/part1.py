with open("./day3-input.txt", "r") as f:
    sumList = []
    for i in range(12):
        sumList.append({"one": 0, "zero": 0})
    for line in f:
        for i in range(12):
            if line[i] == "0":
                sumList[i]["zero"] += 1
            if line[i] == "1":
                sumList[i]["one"] += 1

    gamma = ""
    espilon = ""
    for i in range(12):
        sums = sumList[i]
        if sums["one"] > sums["zero"]:
            gamma += "1"
            espilon += "0"
        else:
            gamma += "0"
            espilon += "1"

    print(int(gamma, 2) * int(espilon, 2))
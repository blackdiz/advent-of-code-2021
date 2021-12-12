with open("./day3-input.txt", "r") as f:
    sum_list = []
    for i in range(12):
        sum_list.append({"one": 0, "zero": 0})
    for line in f:
        for i in range(12):
            if line[i] == "0":
                sum_list[i]["zero"] += 1
            if line[i] == "1":
                sum_list[i]["one"] += 1

    gamma = ""
    espilon = ""
    for i in range(12):
        sums = sum_list[i]
        if sums["one"] > sums["zero"]:
            gamma += "1"
            espilon += "0"
        else:
            gamma += "0"
            espilon += "1"

    print(int(gamma, 2) * int(espilon, 2))
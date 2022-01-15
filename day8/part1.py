with open("./day8-input.txt") as f:
    sum = 0
    for line in f.readlines():
        sum = sum + len(list(filter(lambda output: len(output) in [2, 3, 4, 7], line.replace("\n", "").split(" | ")[1].split(" "))))

    print(sum)
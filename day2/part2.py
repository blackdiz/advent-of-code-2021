with open("./day2-input.txt", "r") as f:
    horizontalPosition = 0
    depth = 0
    aim = 0
    for line in f:
        command, number = line.split(" ")
        if command == "forward":
            horizontalPosition += int(number)
            depth += int(number) * aim
        if command == "up":
            aim -= int(number)
        if command == "down":
            aim += int(number)

    print("horizontal position: " + str(horizontalPosition))
    print("depth: " + str(depth))
    print("product: " + str(horizontalPosition * depth))
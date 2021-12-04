with open("./day2-input.txt", "r") as f:
    horizontalPosition = 0
    depth = 0
    for line in f:
        command, number = line.split(" ")
        if command == "forward":
            horizontalPosition += int(number)
        if command == "up":
            depth -= int(number)
        if  command == "down":
            depth += int(number)

    print("horizontal position: " + str(horizontalPosition))
    print("depth: " + str(depth))
    print("product: " + str(horizontalPosition * depth))
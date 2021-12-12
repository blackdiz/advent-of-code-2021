with open("./day2-input.txt", "r") as f:
    horizontal_position = 0
    depth = 0
    for line in f:
        command, number = line.split(" ")
        if command == "forward":
            horizontal_position += int(number)
        if command == "up":
            depth -= int(number)
        if  command == "down":
            depth += int(number)

    print("horizontal position: " + str(horizontal_position))
    print("depth: " + str(depth))
    print("product: " + str(horizontal_position * depth))
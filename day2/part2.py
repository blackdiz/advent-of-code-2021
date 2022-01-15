with open('./day2-input.txt', 'r') as f:
    horizontal_position = 0
    depth = 0
    aim = 0
    for line in f:
        command, number = line.split(' ')
        if command == 'forward':
            horizontal_position += int(number)
            depth += int(number) * aim
        if command == 'up':
            aim -= int(number)
        if command == 'down':
            aim += int(number)

    print('horizontal position: ' + str(horizontal_position))
    print('depth: ' + str(depth))
    print('product: ' + str(horizontal_position * depth))
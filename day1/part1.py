with open("./day1-input.txt", "r") as f:
    increasement_count = 0
    first = f.readline()
    second = f.readline()
    while first and second:
        if int(second) - int(first) > 0:
            increasement_count += 1
        first = second
        second = f.readline()
    print(increasement_count)
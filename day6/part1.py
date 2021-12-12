with open("./day6-input.txt", "r") as f:
    initial = [int(fish) for fish in f.readline().split(",")]
    next = []
    for i in range(0, 256):
        for fish in initial:
            if (fish == 0):
                next.append(6)
                next.append(8)
            else:
                fish -= 1
                next.append(fish)

        initial = next.copy()
        next.clear()
        print(i)

    print(len(initial))

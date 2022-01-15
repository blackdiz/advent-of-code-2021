with open('./day6-input.txt', 'r') as f:
    initial = {}
    for fish in f.readline().split(','):
        initial[int(fish)] = initial.get(int(fish), 0)
        initial[int(fish)] = initial[int(fish)] + 1

    next = {}
    for i in range(0, 80):
        for timer, count in initial.items():
            if timer == 0:
                next[8] = count
                next[6] = next.get(6, 0) + count
            else:
                next[timer - 1] = next.get(timer - 1, 0) + count

        initial = next.copy()
        next.clear()

    print(sum(initial.values()))

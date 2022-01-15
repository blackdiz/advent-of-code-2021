import sys

with open('./day7-input.txt', 'r') as f:
    crabs = [int(c) for c in f.readline().split(',')]
    max_position = max(crabs)
    min_position = min(crabs)
    minimum_cost = sys.maxsize
    for i in range(min_position, max_position):
        cost = 0
        for crab in crabs:
            cost += abs(crab - i)
        minimum_cost = min(minimum_cost, cost)

    print(minimum_cost)

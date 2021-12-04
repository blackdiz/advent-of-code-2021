f = open("./part1-input.txt", "r")
increasementCount = 0
first = f.readline()
second = f.readline()
while first and second:
    if int(second) - int(first) > 0:
        increasementCount += 1
    first = second
    second = f.readline()
print(increasementCount)
f.close()
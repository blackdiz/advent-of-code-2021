intList = []
with open("./part1-input.txt", "r") as f:
    intList = [int(i) for i in f]

start = 0
end = 2
firstWindow = 0
secondWindow = 0
increasementCount = 0

for i in range(start, end):
    firstWindow += intList[i]

while end < len(intList) - 1:
    secondWindow = firstWindow - intList[start] + intList[end + 1]
    if secondWindow - firstWindow > 0:
        increasementCount += 1

    firstWindow = secondWindow
    start += 1
    end += 1

print(increasementCount)
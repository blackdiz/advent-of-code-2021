int_list = []
with open('./day1-input.txt', 'r') as f:
    int_list = [int(i) for i in f]

start = 0
end = 2
first_window = 0
second_window = 0
increasement_count = 0

for i in range(start, end):
    first_window += int_list[i]

while end < len(int_list) - 1:
    second_window = first_window - int_list[start] + int_list[end + 1]
    if second_window - first_window > 0:
        increasement_count += 1

    first_window = second_window
    start += 1
    end += 1

print(increasement_count)
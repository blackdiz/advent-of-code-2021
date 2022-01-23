def calc_score(stack:list):
    score_table = {'(': 1, '[': 2, '{': 3, '<': 4}
    score = 0
    while len(stack) != 0:
        score = score * 5 + score_table[stack.pop()]

    return score

with open('./day10-input.txt', 'r') as f:
    patterns = [list(line.replace('\n', '')) for line in f.readlines()]

    scores = []
    for pattern in patterns:
        stack = []
        is_corrupt = False
        for symbol in pattern:
            if '[' == symbol or '(' == symbol or '{' == symbol or '<' == symbol:
                stack.append(symbol)
            elif ']' == symbol and stack.pop() != '[' or ')' == symbol and stack.pop() != '(' or '}' == symbol and stack.pop() != '{' or '>' == symbol and stack.pop() != '<':
                is_corrupt = True
                break

        if is_corrupt == False:
            scores.append(calc_score(stack))

    scores.sort()

    print(scores[int(len(scores) / 2)])
score_table = {')': 3, ']': 57, '}': 1197, '>': 25137}

with open('./day10-input.txt', 'r') as f:
    patterns = [list(line.replace('\n', '')) for line in f.readlines()]
    score = 0
    for pattern in patterns:
        stack = []
        for symbol in pattern:
            if ['[', '(', '{', '<'].count(symbol) != 0:
                stack.append(symbol)
            elif [']', ')', '}', '>'].count(symbol) != 0:
                pop_symbol = stack.pop()
                if symbol == ']' and pop_symbol != '[':
                    score = score + score_table[symbol]
                    break
                if symbol == ')' and pop_symbol != '(':
                    score = score + score_table[symbol]
                    break
                if symbol == '}' and pop_symbol != '{':
                    score = score + score_table[symbol]
                    break
                if symbol == '>' and pop_symbol != '<':
                    score = score + score_table[symbol]
                    break

    print(score)
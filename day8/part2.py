def build_pattern(displays):
    pattern = {}
    for display in displays:
        if len(display) == 2:
            pattern['1'] = display
        elif len(display) == 3:
            pattern['7'] = display
        elif len(display) == 4:
            pattern['4'] = display
        elif len(display) == 7:
            pattern['8'] = display

    nine_temp = set(pattern['4'] + pattern['7'])
    for display in displays:
        if len(display) == 6:
            if len(set(display) - set(nine_temp)) == 1 and len(set(pattern['8']) - set(display)) == 1:
                pattern['9'] = display
                break
    for display in displays:
        if len(display) == 5 and len(set(display) - set(pattern['9'])) == 1:
            pattern['2'] = display
            break
    for display in displays:
        if len(display) == 5 and len(set(display) - set(pattern['2'])) == 1:
            pattern['3'] = display
            break
    for display in displays:
        if len(display) == 5 and len(set(display) - set(pattern['2'])) == 2:
            pattern['5'] = display
            break
    for display in displays:
        if len(display) == 6 and len(set(display) - set(pattern['5'])) == 1 and len(set(display) - set(pattern['9'])) == 1:
            pattern['6'] = display
            break
    pattern['0'] = list(filter(lambda k: k not in pattern.values(), displays))[0]

    return {''.join(sorted(value)): key for key, value in pattern.items()}

with open('./day8-input.txt', 'r') as f:
    sum = 0
    for line in f.readlines():
        outputs = line.replace('\n', '').split(' | ')

        pattern = build_pattern(outputs[0].split(' '))

        result = ''
        for output in outputs[1].split(' '):
            result = result + pattern[''.join(sorted(output))]

        sum = sum + int(result)
    print(sum)
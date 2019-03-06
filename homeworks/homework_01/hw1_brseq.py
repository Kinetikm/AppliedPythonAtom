def is_bracket_correct(input_string):
    temp = ['[]', '{}', '()']
    ind = input_string.find
    while (True):
        dlina = len(input_string)
        for skob in temp:
            input_string = input_string.replace(skob, '')
        if dlina == len(input_string):
            break
    if s == '':
        return True
    else:
        return False

def validation_bracket_string(s):
    temp = ['[]', '{}', '()']
    ind = s.find
    while (True):
        dlina = len(s)
        for skob in temp:
            s = s.replace(skob, '')
        if dlina == len(s):
            break
    if s == '':
        return True
    else:
        return False

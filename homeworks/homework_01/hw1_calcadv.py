def advanced_calculator(input_string):
    for i in range(10):
        input_string = input_string.replace(str(i) + " ", str(i) + "|")
    for x in [" ", "\t", "--", "++", "+-", "(-", "/-", "*-"]:
        while x in input_string:
            input_string = input_string.replace("\t", "").\
                replace(" ", "")
            input_string = input_string.replace("--", "+").\
                replace("++", "+")
            input_string = input_string.replace("+-", "-").\
                replace("-+", "-")
            input_string = input_string.replace("(-", "(0-")
            input_string = input_string.replace("/-", "*(0-1)/").\
                replace("*-", "*(0-1)*")
    if len(input_string) > 0 and input_string[0] in ["-", "+"]:
        input_string = "0" + input_string
    item = ""
    output = []
    l = []
    while len(input_string) > 0:
        if input_string[0] in ["+", "-", "/", "*"]:
            if len(item) > 0:
                try:
                    output.append(float(item))
                    item = ""
                except (TypeError, ValueError):
                    return None
            while len(l) > 0 and l[len(l) - 1] is not "(":
                if l[len(l) - 1] in ['*', '/'] or\
                        input_string[0] in ['+', '-']:
                    output.append(l.pop())
                else:
                    break
            l.append(input_string[0])
            input_string = input_string[1::]
        elif input_string[0] is "(":
            if len(item) > 0:
                return None
            l.append("(")
            input_string = input_string[1::]
        elif input_string[0] is ")":
            if len(item) == 0:
                return None
            try:
                output.append(float(item))
                item = ""
            except (TypeError, ValueError):
                return None
            input_string = input_string[1::]
            try:
                item = l.pop()
                while item is not "(":
                    output.append(item)
                    item = l.pop()
                item = ""
            except IndexError:
                    return None
        elif input_string[0].isdigit() or input_string[0] is ".":
            item += input_string[0]
            input_string = input_string[1::]
        elif input_string[0] is "|":
            output.append(float(item))
            item = ""
            input_string = input_string[1::]
        else:
            return None
    if len(item) > 0:
        try:
            output.append(float(item))
            item = ""
        except (ValueError, TypeError):
            return None
    while len(l) > 0:
        output.append(l.pop())
    try:
        while len(output) > 0:
            item = output.pop(0)
            if isinstance(item, float):
                l.append(item)
            else:
                a = l.pop()
                b = l.pop()
                if item is "+":
                    l.append(b + a)
                elif item is "-":
                    l.append(b - a)
                elif item is "/":
                    try:
                        l.append(b / a)
                    except ZeroDivisionError:
                        return None
                elif item is "*":
                    l.append(b * a)
    except IndexError:
        return None
    if len(l) != 1:
        return None
    return l[0]
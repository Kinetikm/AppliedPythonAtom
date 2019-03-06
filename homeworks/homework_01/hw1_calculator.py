

def calculator(x, y, operator):
    if format(type(x)) == format(type(1)) or\
        format(type(x)) == format(type(1.0)):
        if format(type(y)) == format(type(1)) or\
        format(type(y)) == format(type(1.0)):
            if operator == "plus":
                return x + y
            if operator == "minus":
                return x - y
            if operator == "mult":
                return x * y
            if operator == "divide":
                if y != 0:
                    return x / y
        return None

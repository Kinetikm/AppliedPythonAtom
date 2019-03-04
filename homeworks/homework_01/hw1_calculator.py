def calculator(a, b, operator):
    if isinstance(a, (float, int)) and isinstance(b, (float, int)):
        if operator.lower() == "plus":
            return a + b
        elif operator.lower() == "minus":
            return a - b
        elif operator.lower() == "mult":
            return a * b
        elif operator.lower() == "divide" and not (b == 0 or b == 0.0):
            return a / b
        else:
            return None
    else:
        return None
    raise NotImplementedError

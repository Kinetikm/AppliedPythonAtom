def calculator(a, b, operator):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if operator == "minus":
            return a - b
        if operator == "plus":
            return a + b
        if operator == "mult":
            return a * b
        if operator == "divide":
            return a / b
        else:
            return None
    else:
        return None
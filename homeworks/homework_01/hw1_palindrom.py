

def check_palindrom(input_string):
    s2 = input_string[::-1]
    if input_string == s2:
        return True
    return False

print(check_palindrom('asdsa'))
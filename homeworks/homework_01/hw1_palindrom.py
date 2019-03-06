def polidrom(s):
    s = s.lower()
    if s != s[::-1]:
        return False
    else:
        return True
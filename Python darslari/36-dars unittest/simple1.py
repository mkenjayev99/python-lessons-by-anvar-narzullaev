def max_num(a, b, c):
    if b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    return a

def min_num(a, b, c):
    if b < a and b < c:
        return b
    elif c < a and c < b:
        return c
    return a
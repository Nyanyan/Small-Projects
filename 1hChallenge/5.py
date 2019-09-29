import math

l = range(1,10)

def a(i, num, n, plus):
    out = 0
    if n == 0:
        num += l[i]
    elif n == 1:
        num -= l[i]
    elif n == 2:
        num *= l[i]
    elif n == 3:
        num /= l[i]
    elif n == 4:
        out = plus + l[i] ** (math.log10(plus) + 1)
    return num, out


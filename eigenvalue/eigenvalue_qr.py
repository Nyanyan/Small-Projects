from math import sqrt

def householder(a, num):
    n = len(a)
    x11 = [a[i][num] for i in range(num, n)]
    x11_size = 0
    for i in x11:
        x11_size += i ** 2
    x11_size = sqrt(x11_size)
    x21 = [0 for _ in range(num, n)]
    x21[0] = x11_size
    dif = [x11[i] - x21[i] for i in range(n - num)]
    dif_size = 0
    for i in dif:
        dif_size += i ** 2
    dif_size = sqrt(dif_size)
    z = [i / dif_size for i in dif]
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        res[i][i] = 1
    for i in range(num, n):
        for j in range(num, n):
            res[i][j] -= 2 * z[i - num] * z[j - num]
    return res

def multiplication(a, b):
    h = len(a)
    w = len(b[0])
    res = [[0 for _ in range(w)] for _ in range(w)]
    for i in range(h):
        for j in range(w):
            tmp = 0
            for k in range(len(a[0])):
                tmp += a[i][k] * b[k][j]
            res[i][j] = tmp
    return res

def transposition(a):
    n = len(a)
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = a[j][i]
    return res

def householders(a, num):
    h = householder(a, num)
    nxt_a = multiplication(h, a)
    res = []
    if num < len(a) - 2:
        res = householders(nxt_a, num + 1)
    res.append(h)
    return res

def calc_q(hs):
    hts = []
    for h in hs:
        hts.append(transposition(h))
    q = hts[-1]
    for ht in reversed(hts[:-1]):
        q = multiplication(q, ht)
    return q

n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a[i] = [int(i) for i in input().split()]
nxt_a = [[j for j in i] for i in a]
former_ans = [0 for _ in range(n)]
num = 300
for i in range(num):
    q = calc_q(householders(nxt_a, 0))
    qt = transposition(q)
    nxt_a = multiplication(qt, nxt_a)
    nxt_a = multiplication(nxt_a, q)
    if i == num - 2:
        former_ans = [nxt_a[j][j] for j in range(n)]
ans = []
for i in range(n):
    threshold = 0.001
    for j in ans:
        if abs(nxt_a[i][i] - j) <= threshold:
            break
    else:
        for j in former_ans:
            if abs(nxt_a[i][i] - j) <= threshold:
                ans.append(nxt_a[i][i])
                break
print('eigenvalue:')
for i in range(len(ans)):
    print(i + 1, round(ans[i], 3))

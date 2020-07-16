from random import randint
import sys
sys.setrecursionlimit(10 ** 7)

def det_char(a):
    n = len(a)
    if n == 2:
        res = [0 for _ in range(3)]
        for i in range(len(a[0][0])):
            for j in range(len(a[0][0])):
                res[i + j] += a[0][0][i] * a[1][1][j]
                res[i + j] -= a[0][1][i] * a[1][0][j]
        return res
    res = [0 for _ in range(n + 1)]
    for i in range(n):
        pm = -1 if i % 2 else 1
        cofactor = [[[0 for _ in range(2)] for _ in range(n - 1)] for _ in range(n - 1)]
        y = 0
        x = 0
        for j in range(n):
            if j == 0:
                continue
            for k in range(n):
                if k == i:
                    continue
                cofactor[y][x] = [l for l in a[j][k]]
                x += 1
            x = 0
            y += 1
        tmp = det_char(cofactor)
        for j in range(len(tmp)):
            for k in range(len(a[0][i])):
                res[j + k] += pm * a[0][i][k] * tmp[j]
    return res

def assignment(arr, x):
    res = 0
    for i in range(len(arr)):
        res += arr[i] * (x ** i)
    return res

def differential(arr):
    res = [0 for _ in range(len(arr) - 1)]
    for i in range(1, len(arr)):
        res[i - 1] = i * arr[i]
    return res

def newton(arr, arr_d, x, threshold):
    fx = assignment(arr,x)
    if abs(fx) < threshold:
        return x
    slope = assignment(arr_d, x)
    return newton(arr, arr_d, x - fx / slope, threshold)

n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a[i] = [int(i) for i in input().split()]
#for i in a:
#    print(i)
b = [[[0 for _ in range(2)] for i in j] for j in a]
for i in range(n):
    for j in range(n):
        b[i][j][0] = a[i][j]
    b[i][i][1] = -1
det_char_b = det_char(b)
print('det:', det_char_b[0])
#print('det_char', det_char_b)
d_det_char_b = differential(det_char_b)
#print('differential', d_det_char_b)
boundary = 1000
ans = [boundary * 2 for _ in range(n * 2)]
idx = -1
for start in range(-boundary, boundary + 1):
    res = newton(det_char_b, d_det_char_b, start, 0.001)
    flag = True
    tmp = -1
    for i in range(idx + 1):
        if abs(res - ans[i]) < 0.1:
            flag = False
            tmp = i
            break
    if idx == -1 or flag:
        ans[idx + 1] = res
        idx += 1
    else:
        ans[tmp] = (ans[tmp] + res) / 2
ans.sort()
print('eigenvalue:')
for i in range(n):
    if ans[i] == boundary * 2:
        break
    print(i + 1, round(ans[i], 4))



'''
def det(a):
    n = len(a)
    if n == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    res = 0
    for i in range(n):
        pm = -1 if i % 2 else 1
        cofactor = [[0 for _ in range(n - 1)] for _ in range(n - 1)]
        y = 0
        x = 0
        for j in range(n):
            if j == 0:
                continue
            for k in range(n):
                if k == i:
                    continue
                cofactor[y][x] = a[j][k]
                x += 1
            x = 0
            y += 1
        res += pm * a[0][i] * det(cofactor)
    return res
'''
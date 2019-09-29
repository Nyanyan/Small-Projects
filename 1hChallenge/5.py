import math
import itertools

l = list(range(1,10))
cal = list(range(8))

def a(i, num, n, plus):
    out = 0
    tmp = 0
    if plus > 0:
        tmp = plus * 10 + l[i]
    else:
        tmp = l[i]
    if n == 0:
        num += tmp
    elif n == 1:
        num -= tmp
    return [num, tmp]

def b(start, stop):
    out = 0
    for j in range(start, stop + 1):
        out = a(j, 0, 2, out)[1]
    return out


print(l)

for i in range(len(l) - 2):#演算子の数
    n = list(itertools.combinations(cal,i)) #演算子の組み合わせ
    for j in range(len(n)):
        n[j] = list(n[j])
        n[j].append(8)
    for j in range(len(n)): #一つの演算子配列 len(n)
        first = 0
        if len(n[j]) != 0: #最初の数字
            first = b(0,n[j][0])
        else:
            first = b(0,8)
        num = [first]
        pm = [[0]]
        #print(num)
        #print(n[j])
        for k in range(len(n[j]) - 1): #一つの演算子
            #print(n[j][k])
            t = 0
            if k > 0:
                t = n[j][k-1]
            plus = 0
            for m in range(t, len(l)):
                if n[j][k+1] == m:
                    tmp = len(num)
                    for o in range(tmp):
                        num.append(num[o])
                        num[o] += plus
                        num[tmp + o] -= plus
                        pm.append(pm[o])
                        pm[o].append('+')
                        pm[tmp + o].append('-')
                    break
                elif n[j][k] <= m:
                    plus = a(m + 1, 0, 0, plus)[1]
                
        for k in range(len(num)):
            if num[k] == 100:
                print(n[j],num[k], pm[k], k)
        #print(n[j], num)
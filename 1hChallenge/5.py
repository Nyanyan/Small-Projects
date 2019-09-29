import math
import itertools

l = list(range(1,10))
cal = list(range(8))

def a(i, num, n, plus):
    out = 0
    tmp = 0
    if plus > 0:
        tmp = plus + l[i] * 10 ** int(math.log10(plus) + 1)
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
        out = a(stop-j, 0, 2, out)[1]
    return out


print(l)

for i in range(len(l) - 2):#演算子の数
    n = list(itertools.combinations(cal,i)) #演算子の組み合わせ
    for j in range(1): #一つの演算子配列 len(n)
        if len(n[j]) != 0: #最初の数字
            num = b(0,n[j][0])
        else:
            num = b(0,8)
        #print(num)
        #print(n[j])
        for k in range(len(n[j])): #一つの演算子
            #print(n[j][k])
            t = 0
            if k > 0:
                t = n[j][k-1]
            plus = 0
            for m in range(t, len(l) - 2):
                if n[j][k] == m:
                    num = a(m + 1, num, 0, plus)[0]
                    print(plus)
                else:
                    plus = a(m + 1, num, 2, plus)[1]

        print(n[j], num)
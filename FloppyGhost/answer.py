def stay_in_range(i):
    start = 0
    end = 4
    if i > end:
        a = i - end
        i = start + a - 1
    elif i < start:
        a = start - i
        i = end - a + 1
    return i

n = int(input())
a = [int(i) for i in input().split()]

if n == 1:
    print('Yes')
    exit()

arr = list(range(5))
flag = True
moved = [True for _ in range(5)]
moved[a[0]] = False
for i in range(1, n):
    while not moved[a[i]]:
        a[i] = stay_in_range(a[i] + 1)
        flag = False
    moved[a[i]] = False
    moved[stay_in_range(a[i] + 1)] = True
    moved[stay_in_range(a[i] - 1)] = True

if flag:
    print('Yes')
else:
    print(' '.join(map(str, a)))

import math
l = [50,2,1,9]
lmax = []
for i in range(len(l)):
    lmax.append([l[i],i])
for i in range(len(lmax)):
    while lmax[i][0] >= 10:
        lmax[i][0] = lmax[i][0] // 10

lmax.sort()

num = 0
for i in range(len(l)):
    if num != 0:
        num += l[lmax[i][1]] * 10 ** (int(math.log10(num)) + 1)
    else:
        num += l[lmax[i][1]]

print(num)

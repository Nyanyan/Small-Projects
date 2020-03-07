'''
3の倍数と3のつく数字を言う時にあほになる人がいます。
この人が1から正整数nまでの数字を1回ずつ全て言った時、あほになった回数は何回でしょうか。
制約: 1<=n<=10^(10^5)くらい
'''
def stay_in_range(start, end, i):
    if i > end:
        a = i - end
        i = start + a - 1
    elif i < start:
        a = start - i
        i = end - a + 1
    return i

def make_arr(i):
    arr = [[0, 6, 9], [1, 4, 7], [2, 5, 8]]
    for j in range(3):
        k = 0
        while len(arr[j]) > k:
            if arr[j][k] >= i:
                del arr[j][k]
                k -= 1
            k += 1
    return arr

n = input()
l = len(n)
n0 = int(n[0])

#3のつく数の個数(桁dp)
dp1 = [[0, 0] for _ in range(l)] #dp1[i] i桁目まで決めたときの、3がつかない([0]未満決定、[1]未満未決定)の個数
dp1[0][0] = n0 - 1 if n0 > 3 else n0
dp1[0][1] = 1 if n0 != 3 else 0
for i in range(1, l):
    ni = int(n[i])
    a = [0, 0]
    a[0] = dp1[i-1][0] * 9 #未満決定のとき ->3 以外をつける
    a[1] = dp1[i-1][1] * ni if ni <= 3 else dp1[i-1][1] * (ni - 1) #未満未決定のとき、3以外で未満を確定させられるものをつける
    dp1[i][0] = sum(a)

    dp1[i][1] = dp1[i-1][1] if ni != 3 else 0

num_without_3 = dp1[l-1][0] + dp1[l-1][1] - 1 #0を含むので-1
num_with_3 = int(n) - num_without_3

#3の倍数かつ各桁に3がつかない
dp2 = [[[0, 0, 0, 0], [0, 0, 0, 0]] for _ in range(l)] #dp2[i] i桁目まで決めたときの、([0]未満決定、[1]未満未決定)各桁の和%3が[j]である数の個数
arr = make_arr(n0)
for i in range(3):
    dp2[0][0][i] = len(arr[i])
arr2 = [[0, 6, 9], [1, 4, 7], [2, 5, 8]]
for i in range(3):
    if n0 in arr2[i]:
        dp2[0][1][i] = 1

for i in range(1, l):
    ni = int(n[i])
    arr = make_arr(ni)

    for j in range(3):
        a = [0, 0, 0, 0]
        a[0] = sum(dp2[i-1][0]) * 3
        a[1] = dp2[i-1][1][0] * len(arr[j])
        a[2] = dp2[i-1][1][1] * len(arr[stay_in_range(0, 2, j + 2)])
        a[3] = dp2[i-1][1][2] * len(arr[stay_in_range(0, 2, j + 1)])
        dp2[i][0][j] = sum(a)
    
    index = 0 #i-1桁目までの和%3
    for j in range(3):
        if dp2[i][1][j] > 0:
            index = j
    for j in range(3):
        if ni in arr2[j]:
            dp2[i][1][stay_in_range(0, 2, index + j + 1)] = 1

num_multiple_3 = dp2[l-1][0][0] + dp2[l-1][1][0] - 1 #0を含むので-1

print(num_with_3 + num_multiple_3)
print(pow(10, l - 1) - 2 * pow(9, l - 1) // 3 - 1) #ナベアツ方程式(n == pow(10, int m)で成立)
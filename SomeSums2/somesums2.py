'''
問題
0以上N以下の整数を10進数で表した時、各桁の和がA以上B以下である数の個数を10^9+7で割った余りを求めよ。
制約
0 <= N <= 10^30
0 <= A <= B <= 9*(Nの桁数)
制限時間
2秒
入力
N A B
入力例1
20 2 5
出力例1
9
入力例2
314159265 35 89
出力例2
192064520
'''

import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, acos, atan, asin, log, log10
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
def debug(*args):
    if debugmode:
        print(*args)
def input(): return sys.stdin.readline().strip()
def STR(): return input()
def INT(): return int(input())
def FLOAT(): return float(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
inf = sys.maxsize
mod = 10 ** 9 + 7
dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
debugmode = False

n, a, b = MAP()
l = len(str(n))
m = [int(i) for i in str(n)]
dp = [[[0, 0] for _ in range(b + 1)] for _ in range(l)] #dp[i桁目][各桁和がj][未満, 未満未決定]
for j in range(m[0] + 1):
    dp[0][j][0] = 1 if j < m[0] else 0
    dp[0][j][1] = 1 if j == m[0] else 0
for i in range(1, l):
    for j in range(b + 1):
        for k in range(min(10, j + 1)): #i桁目に入れる数字
            dp[i][j][0] += dp[i - 1][j - k][0]
            if k < m[i]:
                dp[i][j][0] += dp[i - 1][j - k][1]
            dp[i][j][0] %= mod
        if dp[i - 1][j][1] and j + m[i] <= b:
            dp[i][j + m[i]][1] = 1
for i in range(l):
    debug(dp[i])
ans = sum([sum(i) % mod for i in dp[l - 1][a:b + 1]]) % mod
print(ans)

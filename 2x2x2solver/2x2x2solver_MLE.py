'''
arr[その位置にあるパーツの番号][ステッカーの向き]
U面
        B
L [0, 0] [1, 0] R
L [2, 0] [3, 0] R
        F
D面
        F
L [4, 0] [5, 0] R
L [6, 0] [7, 0] R
        B

向きは揃っている方向(白黄ステッカー)から時計回りに1, 2となる
'''

from numpy import matrix, rot90
from copy import deepcopy
from collections import deque
move_candidate = ["U", "U2", "U'", "F", "F2", "F'", "R", "R2", "R'"] #回転の候補

puzzle = [[i, 0] for i in range(8)] #パズルの状態

puzzle_back = [[i, 0] for i in range(8)] #パズルの状態

solved = [[i, 0] for i in range(8)]

surface = [[0, 1, 2, 3], [2, 3, 4, 5], [3, 1, 5, 7]]

def move(n_arr, num):
    idx = num // 3
    rot_arr1 = matrix([[n_arr[surface[idx][i]][0] for i in range(j * 2, j * 2 + 2)] for j in range(2)])
    rot_arr2 = matrix([[n_arr[surface[idx][i]][1] for i in range(j * 2, j * 2 + 2)] for j in range(2)])
    rot_arr1 = rot90(rot_arr1, 3 - num % 3).tolist()
    rot_arr2 = rot90(rot_arr2, 3 - num % 3).tolist()
    tmp = [[[2, 1], [1, 2]], [[0, 0], [0, 0]], [[2, 1], [1, 2]]]
    if num // 3 != 0:
        rot_arr2 = [[(rot_arr2[j][i] + tmp[num % 3][j][i]) % 3 for i in range(2)] for j in range(2)]
    for i in range(4):
        n_arr[surface[idx][i]][0] = rot_arr1[i // 2][i % 2]
        n_arr[surface[idx][i]][1] = rot_arr2[i // 2][i % 2]
    return n_arr

def scrm(n_arr, move_num):
    if len(scramble_arr) == move_num:
        return n_arr
    n_arr = move(n_arr, scramble_arr[move_num])
    n_arr = scrm(n_arr, move_num + 1)
    return n_arr

def num2moves(arr):
    res = ''
    for i in arr:
        res += move_candidate[i] + ' '
    return res

def moves2num(arr):
    res = []
    for i in arr:
        res.append(move_candidate.index(i))
    return res

def arr2num(arr):
    res1 = 0
    res2 = 0
    for i in range(8):
        res1 *= 3 ** i
        res1 += arr[i][0]
    for i in range(7):
        res2 *= 3
        res2 += arrr[i][1]
    return res1, res2


scramble = list(input().split(' '))

scramble_arr = moves2num(scramble)
print('scramble:', num2moves(scramble_arr))
puzzle = scrm(puzzle, 0)
print('scrambled:', puzzle)

que = deque([[deepcopy(puzzle), 0, [], 0], [deepcopy(puzzle_back), 0, [], 1]])

marked = [[[[] for _ in range(3 ** 7)] for _ in range(9 ** 8)] for _ in range(2)]

print('start!')

while len(que):
    tmp = que.popleft()
    arr = tmp[0]
    num = tmp[1]
    moves = tmp[2]
    mode = tmp[3]
    print(tmp)
    if arr == solved:
        print(num2moves(moves), mode)
        exit()
    if num < 6:
        for i in range(9):
            if num != 0 and i // 3 == moves[-1] // 3:
                continue
            n_arr = move(deepcopy(arr), i)
            n_moves = deepcopy(moves)
            n_moves.append(i)
            idx1, idx2 = arr2num(n_arr)
            marked[mode][idx1][idx2] = n_moves
            if len(marked[(mode + 1) % 2][idx1][idx2]):
                print(moves, marked[(mode + 1) % 2][idx1][idx2])
                exit()
            elif len(marked[mode][idx1][idx2]):
                continue
            que.append([n_arr, num + 1, n_moves, mode])

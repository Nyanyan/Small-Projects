'''
cards
ForkBomb    ライフを2減らし、フラグ取り除く
Bug         ライフを1減らす
MoveFlag    一個のフラグを別のコマンドカードの末尾に追加
RemoveFlag  1個のフラグを取り除く
AddFlag     任意のコマンドカードの末尾にフラグを追加
ライフ5、プレイヤー2
'''
import random
import matplotlib.pyplot as plt #グラフ作成
flagnum = 4
cmdcard = ['F','B','M','R','A']
cmdnum = list(range(len(cmdcard)))
winner = [0,0]
countavg = 0

tim = 1000

rate = []

for c in range(tim):
    life = [5,5]
    random.shuffle(cmdnum) #コマンドカード配置を作成
    print(cmdnum)
    cmd = []
    for i in range(len(cmdcard)):
        cmd.append(cmdcard[cmdnum[i]])
    print(cmd)

    flag = [[],[]] #初期フラグ配置を作成
    for k in range(2):
        while True:
            tmp = random.randint(0,len(cmdcard) - 1)
            tmpflag = False
            for j in range(len(flag[k])):
                if flag[k][j] == tmp:
                    tmpflag = True
            if tmpflag == False:
                flag[k].append(tmp)
            if len(flag[k]) == flagnum:
                break
    print(flag)
    flagstat = [] #初期フラグ配置を反映
    for i in range(len(cmdcard)):
        flagstat.append([])
    for i in range(flagnum):
        flagstat[flag[0][i]].append(0)
        flagstat[flag[1][i]].append(1)
    print(flagstat)

    game = True
    flagcount = [flagnum,flagnum]
    print('start')
    print(cmd)
    print(flagstat)
    counttmp = 0
    while game == True: #ゲーム処理
        count = 0
        flagsum = 0
        for i in range(len(flagstat)):
            flagsum += len(flagstat[i])
        #print(flagsum,cmd,flagstat)
        while count < flagsum:
            tmp1 = 0 #すべき処理を見つける
            tmp2 = 0
            for i in range(len(flagstat)):
                tmp1 += len(flagstat[i])
                if tmp1 - 1 >= count:
                    tmp2 = i
                    break
            #print(count,tmp2,len(flagstat[tmp2]) - (tmp1 - count),flagstat[tmp2][len(flagstat[tmp2]) - (tmp1 - count)],life)
            if cmd[tmp2] == 'F':
                life[flagstat[tmp2][len(flagstat[tmp2]) - (tmp1 - count)] % 2] -= 2 #相手のライフを2減らす
                del flagstat[tmp2][len(flagstat[tmp2]) - (tmp1 - count)] #自分のフラグを消す
                count -= 1
                flagsum -= 1
            elif cmd[tmp2] == 'B':
                life[flagstat[tmp2][len(flagstat[tmp2]) - (tmp1 - count)] % 2] -= 1 #相手のライフを1減らす
            elif cmd[tmp2] == 'M':
                while True:
                    movefrom = random.randint(0,len(flagstat) - 1)
                    if len(flagstat[movefrom]) != 0:
                        break
                moveto = random.randint(0,len(flagstat) - 1)
                #print(flagstat)
                move = flagstat[movefrom].pop()
                flagstat[moveto].append(move)
                #print(flagstat)
            elif cmd[tmp2] == 'R':
                remove1 = 0
                remove2 = 0
                while True:
                    remove2 = random.randint(0,len(flagstat) - 1)
                    if len(flagstat[remove2]) != 0:
                        break
                remove1 = random.randint(0,len(flagstat[remove2]) - 1)
                #print(remove2,remove1,flagstat)
                del flagstat[remove2][remove1]
                #print(flagstat)
                if remove2 <= tmp2 and remove1 <= len(flagstat[tmp2]) - (tmp1 - count):
                    count -= 1
                flagsum -= 1
            elif cmd[tmp2] == 'A':
                add = random.randint(0,len(flagstat) - 1)
                flagstat[add].append(flagstat[tmp2][len(flagstat[tmp2]) - (tmp1 - count)])
                if add < tmp2:
                    count += 1
                flagsum += 1
            print(life,flagstat)
            tmp3 = 0
            tmp4 = 0
            for i in range(len(flagstat)):
                for j in range(len(flagstat[i])):
                    if flagstat[i][j] == 0:
                        tmp3 += 1
                    else:
                        tmp4 += 1
            flagcount = [tmp3,tmp4]
            for i in range(2):
                if life[i] < 0:
                    life[i] = 0
            counttmp += 1
            if life[0] <= 0 or life[1] <= 0 or flagcount[0] == 0 or flagcount[1] == 0:
                game = False
                break
            count += 1

    print(life,flagcount)
    win = 0
    if life[0] == 0 or flagcount[0] == 0:
        win = 1
    print('player ' + str(win) + ' won!')
    winner[win] += 1
    countavg += counttmp
    rate.append(winner[0] / (winner[0] + winner[1]))
ratex = list(range(1,tim + 1))

fig = plt.figure(figsize=(10,6))
plt.rcParams["font.family"] = "IPAexGothic" # フォントの種類
plt.plot(ratex, rate, '-', label="先攻の勝率")
plt.xlabel('回数', fontsize=15)     #x軸ラベル
plt.ylabel('勝率', fontsize=15)    #y軸ラベル
plt.title('スパゲッティコードでの先攻の勝率', fontsize=16) #題名
plt.grid() #グリッド表示
plt.legend(fontsize=15) #凡例表示
plt.xlim(0) #x軸の最小値を0に設定
plt.ylim(0,1) #x軸の最小値を0に設定
#plt.savefig(str(i)+'.png')
plt.show()
plt.close()

print(winner,countavg / tim)

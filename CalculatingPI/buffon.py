import sys
import tkinter
import random
import math
import matplotlib.pyplot as plt #グラフ作成

d=100
l=50
line=10


root = tkinter.Tk()
root.title("Buffon's needle problem")
root.geometry("1000x1000")



canvas = tkinter.Canvas(root, width = d*(line-1), height = d*(line-1))
canvas.create_rectangle(0, 0, d*(line-1), d*(line-1), fill = 'gray')
for i in range(line):
    canvas.create_line(0,100*i,900,100*i)

#キャンバスバインド
canvas.place(x=50, y=50)


cnt = 0
num = 1000
piarray=[[],[]]
pitheory = [[],[]]
pi=0

for i in range(num):
    placeX = random.uniform(d,d*(line-2))
    placeY = random.uniform(d,d*(line-2))
    theta = random.uniform(0,2*math.pi)
    area1=0
    area2=0
    flag = False
    for j in range(line):
        if j*d < placeY and (j+1)*d > placeY:
            area1=j
        if j*d < placeY+l*math.sin(theta) and (j+1)*d > placeY+l*math.sin(theta):
            area2=j
        if j*d == placeY or j*d == placeY+l*math.sin(theta):
            flag = True
    if area1-area2 != 0 or flag:
        cnt+=1
    if cnt != 0:
        pi=2*l/cnt*(i+1)/d
    else:
        pi=0
    piarray[0].append(i+1)
    piarray[1].append(pi)
    pitheory[0].append(i+1)
    pitheory[1].append(math.pi)
    print(i,placeX,placeY,theta,area1,area2,cnt,pi)
    canvas.create_line(placeX,placeY,placeX+l*math.cos(theta),placeY+l*math.sin(theta))


plt.rcParams["font.family"] = "IPAexGothic" # フォントの種類
plt.plot(piarray[0], piarray[1], "r-", label="円周率")
plt.plot(pitheory[0], pitheory[1], "b-", label="理論値") #理論値
plt.title("ビュフォンの針による円周率の算出", fontsize=16) #題名
plt.xlabel("回数", fontsize=12)     #x軸ラベル
plt.ylabel("円周率", fontsize=12)    #y軸ラベル
plt.grid() #グリッド表示
plt.legend(fontsize=10) #凡例表示
plt.xlim(0) #x軸の最小値を0に設定
plt.show()


print(pi)
root.mainloop()

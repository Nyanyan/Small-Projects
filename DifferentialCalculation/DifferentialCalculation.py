import matplotlib.pyplot as plt

equation = "ma = -kx - k'(v^2)*(v/|v|)"

dt = 0.00001
x0 = 1
v0 = 0
a0 = -x0

time = 100

xarray = []
varray = []
aarray = []

xarray.append(x0)
varray.append(v0)
aarray.append(a0)
tarray = [0]

t = int(time // dt)

for i in range(t):
    varray.append(varray[i] + aarray[i] * dt)
    xarray.append(xarray[i] + varray[i] * dt)
    aarray.append(-(varray[i+1] ** 3) / abs(varray[i+1]) - xarray[i+1])
    tarray.append(tarray[i] + dt)

plt.rcParams["font.family"] = "Times New Roman" # フォントの種類
plt.plot(tarray, xarray, '-', label="result")
plt.title(equation, fontsize=16) #題名
plt.xlabel("x", fontsize=12)     #x軸ラベル
plt.ylabel("y", fontsize=12)    #y軸ラベル
plt.grid() #グリッド表示
plt.legend(fontsize=10) #凡例表示
plt.xlim(0) #x軸の最小値を0に設定
plt.show()
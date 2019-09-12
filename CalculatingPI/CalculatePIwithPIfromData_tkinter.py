import sys
import tkinter

root = tkinter.Tk()
root.title("モンテカルロ法")
root.geometry("100x100")

canvas = tkinter.Canvas(root, width = 100, height = 100)
canvas.create_rectangle(0, 0, 100, 100, fill = 'gray')
canvas.place(x=0, y=0)

num = 1000
r = 99/2
count=0

path = 'pi.txt'

with open(path) as f:
    a = f.read()

pirandom = [0]*4
i=0
j=1
b = 200
c = 0
countnum=0
while countnum<=num:
    if ord(a[i]) >= 48 and ord(a[i]) <= 57:
        pirandom[c] = int(a[i])
        c+=1
    if c == 4:
        x = pirandom[0]*10 + pirandom[1]
        y = pirandom[2]*10 + pirandom[3]
        canvas.create_oval(x,y,x,y)
        if (x-r)**2 + (y-r)**2 <= r**2:
            count+=1
        countnum+=1
        c=0
        if countnum % (num // b) == 0:
            sys.stdout.write("\r")
            for k in range(j):
                sys.stdout.write("=")
            for k in range(b - j):
                sys.stdout.write(" ")
            sys.stdout.write("|")
            sys.stdout.flush()
            j+=1
    i+=1

pi = 4 * count / num
print('')
print(count,num,pi)

root.mainloop()

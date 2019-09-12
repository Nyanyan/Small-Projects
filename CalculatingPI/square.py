import sys
import random

num = 100000000
r = 99/2
count=0
b = 200
j=1
for i in range(num):
    x = random.uniform(0,2*r)
    y = random.uniform(0,2*r)
    #print(x,y)
    if (x-r)**2 + (y-r)**2 <= r**2:
        count+=1
    if i % (num // b) == 0:
        sys.stdout.write("\r")
        for k in range(j):
            sys.stdout.write("=")
        for k in range(b - j):
            sys.stdout.write(" ")
        sys.stdout.write("|")
        sys.stdout.flush()
        j+=1

pi = 4 * count / num
print('')
print(count,num,pi)

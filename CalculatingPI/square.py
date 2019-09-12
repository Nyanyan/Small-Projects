import random

num = 1000
r = 50
count=0
for i in range(num):
    x = random.uniform(0,2*r)
    y = random.uniform(0,2*r)
    print(x,y)
    if (x-r)**2 + (y-r)**2 <= r**2:
        count+=1

pi = 4 * count / num
print(count,num,pi)

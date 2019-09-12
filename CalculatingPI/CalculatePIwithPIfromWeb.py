import sys
import mechanize

num = 10000
r = 99/2
count=0

# ブラウザをエミュレート
browser = mechanize.Browser()
response = browser.open('http://www.tstcl.jp/ja/randd/pi.php')
a = str(response.read())

start = a.find('3.')

pirandom = []
i=start
j=1
b = 50
while len(pirandom)<=num*4:
    if ord(a[i]) >= 48 and ord(a[i]) <= 57:
        pirandom.append(int(a[i]))
    if len(pirandom) % (num*4 // b) == 0:
        sys.stdout.write("\r")
        for k in range(j):
            sys.stdout.write("=")
        for k in range(b - j):
            sys.stdout.write(" ")
        sys.stdout.write("|")
        sys.stdout.flush()
        j+=1
    i+=1

print('')

j=1
for i in range(num):
    x = pirandom[4*i]*10 + pirandom[4*i+1]
    y = pirandom[4*i+2]*10 + pirandom[4*i+3]
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

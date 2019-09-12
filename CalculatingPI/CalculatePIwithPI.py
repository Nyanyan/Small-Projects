import mechanize

num = 250000
r = 50
count=0

# ブラウザをエミュレート
browser = mechanize.Browser()
response = browser.open('http://www.tstcl.jp/ja/randd/pi.php')
#HTMLを表示
a = str(response.read())
#print(a)


#print(soup)
start = a.find('141592653589')


pirandom = []
i=start
while len(pirandom)<=num*4:
    if ord(a[i]) >= 48 and ord(a[i]) <= 57:
        pirandom.append(int(a[i]))
    i+=1
#print(pirandom)

for i in range(num):
    x = pirandom[4*i]*10 + pirandom[4*i+1]
    y = pirandom[4*i+2]*10 + pirandom[4*i+3]
    print(x,y)
    if (x-r)**2 + (y-r)**2 <= r**2:
        count+=1

pi = 4 * count / num
print(count,num,pi)


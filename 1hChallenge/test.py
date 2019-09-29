import copy

a = [[1,2,3,4]]
a.append(copy.copy(a[0]))
print(a)
a[0].append(5)

print(a,id(a[0]),id(a[1]))
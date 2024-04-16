# saper
import numpy as np
s = [int(x) for x in input().split()]
n = s[0]
m = s[1]
mns = s[2]
minei = [0]*mns
minej = [0]*mns
for i in range(mns):
    minei[i], minej[i] = map(int, input().split())


def makefield(n, m,  minei, minej):
    field = []
    dx = (-1, -1, -1, 0, 0, 1, 1, 1)
    dy = (-1, 0, 1, -1, 1, -1, 0, 1)
    for k in range(n+2):
        field.append([0]*(m+2))
    for i in range(mns):
        for k in range(len(dx)):
            field[minei[i]+dx[k]+1][minej[i]+dy[k]] += 1
    for i in range(mns):
        field[minei[i]+1][minej[i]] = '*'
    return field


'''b = np.arange(1, 16)
a = np.asmatrix(b.reshape(3, 5))
print(a)
a = a[1:3, 1:3]
print(a)'''
field1 = []
field1 = makefield(n, m, minei, minej)
field1 = np.array(field1)
print(field1)
field1 = field1[1:m+1, 1:n+1]
print(field1)
print(field1[1][1])
# for row in field1:
# print(" ".join(map(str, row)))


a = [int(x)for x in input().split()]
b = [int(x)for x in input().split()]
sum = 0
if a[1]+b[1] > abs(a[0]-b[0]):
    sum += abs(a[0]-b[0])+1
    sum += a[1]+b[1]
else:
    sum += a[1]*2+1+b[1]*2+1
print(sum)
'''
if a[0] < a[1]:
    sum += a[0]+1+a[1]
else:
    sum += a[1]*2+1

if b[0] < b[1]:
    sum += b[0]+1+b[1]
else:
    sum += b[1]*2+1'''

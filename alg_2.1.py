def findmax2(seq):
    if len(seq) <= 1:
        return ("imp")
    else:
        max1 = max(seq[0], seq[1])
        max2 = min(seq[0], seq[1])
        for i in range(len(seq)):
            if seq[i] > max1:
                max2 = max1
                max1 = seq[i]
            elif seq[i] > max2:
                max2 = seq[i]
    return (max1, max2)


def findmineven(seq):
    ans = -1
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (ans == -1 or ans > seq[i]):
            ans = seq[i]
    return (ans)


seq = [int(x)for x in input().split()]
print(seq)
mineven = findmineven(seq)
print(mineven)
max1, max2 = findmax2(seq)
print(max1, max2)

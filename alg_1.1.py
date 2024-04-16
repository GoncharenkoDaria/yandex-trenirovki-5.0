print("sortirovka puzirkom")
a = [0]*5


def nedin_array(a):
    print("enter massiv")
    for i in range(5):
        a[i] = int(input())
        if a[i] == 0:
            break
    print(a)
    return (a)


def din_array(a):
    print("enter massiv")
    data = str(input())
    s = data.split()
    a = [int(x) for x in s]

    return (a)


def din_array2(a):
    print("enter massiv")
    a = [int(x)for x in input().split()]
    # a.append(map(int, input().split()))
    return (a)


a = din_array2(a)
print(a)
for j in range(4):
    for i in range(4):
        if a[i] > a[i+1]:
            x = a[i+1]
            a[i+1] = a[i]
            a[i] = x
print(a)

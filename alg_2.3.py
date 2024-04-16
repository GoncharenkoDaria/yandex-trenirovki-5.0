mode = "r+"
try:
    f = open("alg_2.3.txt")
except FileNotFoundError:
    print("Ошибка: Файл не найден")
else:
    print("Файл открыт успешно")
text = f.readline()
f.close()
result = [int(x) for x in text.split(', ')]
# print(f"Текст из файла: {text}")
print(result)
maxi = result.index(max(result))


def islandwater(result):
    maxi = result.index(max(result))
    ans = 0
    maxel = 0
    for i in range(0, maxi, 1):
        if result[i] > maxel:
            maxel = result[i]
        else:
            ans += maxel-result[i]

    maxel = 0
    for i in range(len(result)-1, maxi, -1):

        if result[i] > maxel:
            maxel = result[i]
        else:
            ans += maxel-result[i]
    return (ans)


ans_isl = islandwater(result)
print(ans_isl)

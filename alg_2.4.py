mode = "r+"
try:
    f = open("alg_2.4.txt")
except FileNotFoundError:
    print("no file")
else:
    print("file opened nicely")
text = f.readline()
symbols = []
for x in text:
    symbols.append(x)
symbols = list(text)
print(f" Your file contains: \n {text}")


def sokrat(symbols):
    lastsym = symbols[0]
    ans = []
    for i in range(len(symbols)):
        if symbols[i] != lastsym:
            ans += lastsym
            lastsym = symbols[i]
    ans += lastsym
    return (ans)


news = sokrat(symbols)
str1 = ''
for x in news:
    str1 += str(x)
print(str1)

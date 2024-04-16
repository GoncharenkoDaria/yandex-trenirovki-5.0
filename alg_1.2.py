'''
s = input()
ans = ''
anscount = 0
for x in set(s):
    xcount = 0
    for j in range(len(s)):
        if x == s[j]:
            xcount += 1
    if xcount > anscount:
        ans = x
        anscount = xcount
print(ans)
'''

'''
c = input()
ans = ''
anscount = 0
spisok = {}
for j in c:
    if j not in spisok:
        spisok[j] = 0
    spisok[j] += 1
    if spisok[j] > anscount:
        anscount = spisok[j]
        ans = j
print(ans)
print(anscount)
'''

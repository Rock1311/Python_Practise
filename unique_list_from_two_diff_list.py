##print unique list from 2 different lists

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2,2, 3, 4,5, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c= []
d=[]
for x in a:
    for y in b:
        if (x==y):
            c.append(x)
print(c)

for x in c:
    if (x not in d):
        d.append(x)

print(d)

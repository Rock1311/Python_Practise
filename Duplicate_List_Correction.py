## Create new list of unqine item.


##Using Loop
list = [1,2,3,4,4,5,5,6,3,2,7,8,5,8,8,9,10]
a = []

for x in list:
    if x not in a:
        a.append(x)

print(a)

"""
##Method using set
list = [1,2,3,4,4,5,5,6,3,2,7,8,5,8,8,9,10]
new = set()

for x in list:
    new.add(x)
print(new)
"""
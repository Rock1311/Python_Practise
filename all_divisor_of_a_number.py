##print(all divisor of a number)

num = int(input('Please enter any number: ' ))
list = []

for x in range (1,num):
    remainder = num%x
    if (remainder == 0):
        list.append(x)
print (list)
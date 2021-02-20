##palindrom
string = input("Enter any string: ")
reverse = string [::-1]
##ASAM
for x in string:
    for y in reverse:
        if (x==y):
            value = True
        else:
            value = False

if (value == True ):
    print('It is a palindrom')

else:
    print('It is not a palindrom string')

input('Press any key to exit')

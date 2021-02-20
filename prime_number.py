num = int(input('Enter your number: '))
count = 0
for x in range(2,num):
    if (num%x == 0):
        count += 1

if count >=1 :
    print ('It is not a prime number')
else:
    print('It is a  prime number')

input ('Press anything to exit: ')
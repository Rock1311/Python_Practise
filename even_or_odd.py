##Ask a number and let know it is even or odd.

number = int(input('Enter any number: '))
remainder = number % 2

if (number == 1 or remainder == 1):
    print ('Your '+str(number)+' is a odd number')
else:
    print ('Your number ' +str(number)+' is a even number')


input ('Press anything to exit')

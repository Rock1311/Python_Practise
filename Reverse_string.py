## reverse string

string = input('Enter string you want to reverse: \n ')
splitted_list = string.split( )
reversed_list = splitted_list[::-1]
reversed_string = ' '.join(reversed_list)
print(reversed_string)
input('Press anything to exit')

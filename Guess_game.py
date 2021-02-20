import random

number = random.randrange(1,10)

guess = int (input("Guess a number between 1 to 10: "))

if ( guess == number ):
    print('Congratualte you guess correct number')


elif ( guess > number ):
    print('Oops your guess was too high')

else:
    print('Oops your guess was too low')

input('Press anything to exit: ')

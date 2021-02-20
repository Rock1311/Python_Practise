##Rock_Paper_Scissor_Game

print('Welcome to Rock Paper Game \n')
print('It is a two player Game \n')
print('Select anything between "Rock" "Paper" "Scissor" \n')

cond = True
while (cond):
    player_one = input("Enter player_one choice: ").lower()
    player_two = input("Enter player_two choice: ").lower()

    if (player_one == player_two):
        print("Tie")
        cont = input('If you want to cont playing press y: ')
        if ( cont.lower() != 'y'):
            cond = False
        else:
            continue
    elif ( (player_one == 'scissor' and player_two == 'rock') or (player_one == 'rock' and player_two == 'paper') or (player_one == 'paper' and player_two == 'scissor') ):
        print ("Player_Two Won ")
        cont = input('If you want to cont playing press y: ')
        if ( cont.lower() == 'y'):
            continue
        else:
            cond = False
    elif ( (player_two == 'scissor' and player_one == 'rock') or (player_two == 'rock' and player_one == 'paper') or (player_two == 'paper' and player_one == 'scissor') ):
        print ("Player_One Won ")
        cont = input('If you want to cont playing press y: ')
        if ( cont.lower() == 'y'):
            continue
        else:
            cond = False
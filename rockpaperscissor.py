import random

choices = ['rock', 'paper', 'scissors']

winPlayer = 0
winBot = 0

def get_winner(a, b):
    if a == b:
        print('tie!')
        return 0

    elif (a == 'rock' and b == 'scissor') or \
         (a == 'paper' and b == 'rock') or \
         (a == 'scissor' and b == 'paper'):
        print("you win!")
        return 1
    
    else:
        print("computer win!")
        return -1

while winBot < 3 and winPlayer < 3:
    a = input("input: ")
    if a not in choices:
        print('wrong input')
        break
    b = random.choice(choices)
    result = get_winner(a,b)
    if result == 1:
        winPlayer +=1
    elif result == -1:
        winBot +=1

    print("You win ",winPlayer," times")
    print("Computer win ",winBot," times")
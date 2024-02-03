import random

computer_guess=random.randint(1,10)

user_guess=0

while user_guess!=computer_guess:
    user_guess=int(input('Enter your guess-> '))

    if(user_guess < computer_guess):
        print('you guess is smaller number')
    elif(user_guess > computer_guess):
        print('you guessed larger number')
    else:
        print('you guessed correctly')

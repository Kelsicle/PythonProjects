import random

print('-----------------------------')
print('      Guess the Number')
print('-----------------------------')
print()

the_number = random.randint(0,100)

guess = -1

while guess != the_number:
    text_guess = input('Guess a number between 0 and 100: ')
    guess = int(text_guess)
    if guess < the_number:
        print('Too low!')
    elif guess > the_number:
        print('Too high!')
    else:
        print('You win!')


import random

print('Number Guessing Game')

number = random.randint(1,9)
chances = 0
print('Guess a Number between 1 and 9:')

while chances < 5: 
    guess = int(input('Enter your Guess:'))
    if guess == number:
        print('You won!')
        break
    elif guess < number:
        print('Your number was too low, guess a higher number:')
    else: 
        print('Your guess was too high, guess a lower number')
    chances += 1
if not chances < 5:
    print('You lose')


    
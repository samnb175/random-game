from random import randint
import sys


your_name = input('What is your name? ')
start = int(sys.argv[1])
end = int(sys.argv[2])
correct_num = randint(start, end)

print('starting game...')
print('')
print(f'Hi {your_name}, a number has been generated between {start} to {end}')

while True:
    try:
        your_num = int(input('Try guess the number: '))
        if 0 < your_num < 11:
            if your_num == correct_num:
                print(f'You guessed it right {your_name}!')
                break
            else:
                print('Wrong guess. Please try again loser!')
                continue
        else:
            print(f'Fool! Please enter a number between {start} to {end} (inclusive) again')
    except ValueError:
        print('Can you read? Enter a "NUMBER"!')
        continue


    

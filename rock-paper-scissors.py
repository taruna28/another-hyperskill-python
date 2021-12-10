import math
import random


user_name = input('Enter your name: ')
print(f'Hello, {user_name}')
list_of_items = input()
if list_of_items == '':
    list_of_items = ['rock', 'paper', 'scissors']
else:
    list_of_items = list_of_items.split(',')
print("Okay, let's start")

rating = 0
with open('rating.txt', 'r') as records:
    lines = records.readlines()
    for i in lines:
        if i.strip('\n').split(' ')[0] == user_name:
            rating = int(i.strip('\n').split(' ')[1])
            break

while True:
    user_input = input()
    if user_input == '!exit':
        print('Bye!')
        break
    elif user_input == '!rating':
        print(f'Your rating: {rating}')
        continue
    elif user_input not in list_of_items:
        print('Invalid input')
        continue
    computer_turn = random.choice(list_of_items)
    index = list_of_items.index(user_input)

    list_of_items_without_user_input = list_of_items[index + 1:] + list_of_items[:index]
    first_half = list_of_items_without_user_input[:math.ceil(len(list_of_items_without_user_input) / 2)]
    second_half = list_of_items_without_user_input[math.ceil(len(list_of_items_without_user_input) / 2):]
    if user_input == computer_turn:
        rating = rating + 50
        print(f'There is a draw ({computer_turn})')
    elif computer_turn in first_half:
        print(f'Sorry, but the computer chose {computer_turn}')
    elif computer_turn in second_half:
        rating = rating + 100
        print(f'Well done. The computer chose {computer_turn} and failed')
    else:
        raise Exception

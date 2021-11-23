# write your code here
import random

def generate_simple_task():
    operations = ['+', '-', '*']

    number_1 = random.randint(2, 9)
    number_2 = random.randint(2, 8)

    operation = random.choice(operations)

    if operation == '+':
        result = number_1 + number_2
    elif operation == '-':
        result = number_1 - number_2
    elif operation == '*':
        result = number_1 * number_2

    print(number_1, operation, number_2)

    return result

def generate_integral_task():
    number = random.randint(11, 29)

    print(number)

    return number ** 2

def save_result_to_file(username, level, result, tasks):
    if level == 1:
        level_description = 'simple operations with numbers 2-9'
    elif level == 2:
        level_description = 'integral squares 11-29'

    file_output = f'{name}: {result}/{tasks} in level {level} ({level_description}).\n'
    file = open('results.txt', 'a')
    file.write(file_output)
    file.close()

    print('The results are saved in "results.txt".')


TASKS = 5
task_count = 0
mark = 0

while True:
    try:
        print('Which level do you want? Enter a number:')
        print('1 - simple operations with numbers 2-9')
        print('2 - integral squares of 11-29')
        level = int(input())
        if level not in [1, 2]:
            print('Incorrect format.')
    except ValueError:
        print('Incorrect format.')
    else:
        # print("masuk ")
        break

while task_count < TASKS:
    task_count += 1
    if level == 1:
        correct_answer = generate_simple_task()
    elif level == 2:
        correct_answer = generate_integral_task()
    while True:
        try:
            user_answer = int(input())
        except ValueError:
            print('Incorrect format.')
        else:
            if correct_answer == user_answer:
                print('Right!')
                mark += 1
            else:
                print('Wrong')
            break

print(f'Your mark is {mark}/{TASKS}')
print('Would you like to save your result to the file? Enter yes or no.')
save_file_answer = input()
if save_file_answer in ['YES', 'yes', 'Yes', 'y']:
    print('What is your name?')
    name = input()
    save_result_to_file(name, level, mark, TASKS)

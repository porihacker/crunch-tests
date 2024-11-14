from functions.functions import *


if __name__ == '__main__':
    while True:
        id_number = input('Enter your ID number or "quit" to exit: ')
        if id_number.lower() == 'quit':
            break
        elif len(id_number) == 13 and id_number.isdigit():
            print(f'Date of birth: {get_date_of_birth(id_number )}')
            print(f'Gender:    {get_gender(id_number )}')
            print(f'Citizenship: {get_citizenship(id_number )}')
        else:
            print('Invalid ID number')
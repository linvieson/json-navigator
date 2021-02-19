'''
This module gets the json file from the user. It asks a user, which part of
the json object he or she wants to see and outputs its value.
'''
import json

def get_json() -> dict:
    '''
    Make a get request on a server. Return json object as a python dictionary.
    '''
    path = input('Enter a path to json file: ')
    files = open(path, 'r', encoding = 'utf-8')
    data = json.load(files)
    return data


def check_list(dates: list, num: int) -> str:
    '''
    Recursive function that gets the data requested by user. Return string
    value, list or json object if the user enters ALL.
    '''
    num = int(num)
    if isinstance(dates[num], dict):
        print('It is an object. Enter one of the available values or enter\
 ALL if you want to see the whole object: ')

        keys = list(iter(dates.keys()))
        for key in keys:
            if key != keys[-1]:
                print(key, end=', ')
            else:
                print(key)
        return check_input(dates[num])

    if isinstance(dates[num], list):
        print(f'It is a list. Enter index from 0 to {len(dates[num])} or enter\
 ALL if you want to see the whole list: ')
        return check_input(dates[num])

    return dates[num]


def check_input(data: dict) -> str:
    '''
    Recursive function that gets the data requested by user. Return string
    value, list or json object if the user enters ALL.
    '''
    user = input()

    if user == 'ALL':
        return json.dumps(data, indent = 4, ensure_ascii = False)

    if isinstance(data, dict) and user in data.keys():

        if isinstance(data[user], dict):
            print('It is an object. Enter one of the available values or enter\
 ALL if you want to see the whole object: ')

            keys = list(iter(data[user]))
            for key in keys:
                if key != keys[-1]:
                    print(key, end=', ')
                else:
                    print(key)
            return check_input(data[user])

    if isinstance(data[user], list):
        dates = data[user]
        length = len(dates)
        print(f'It is a list. Enter index from 0 to {length} or enter\
 ALL if you want to see the whole list: ')
        num = input()

        if num == 'ALL':
            return data[user]
        return check_list(dates, num)

    return str(user) + ': ' + str(data[user])


def main() -> str:
    '''
    Main function that runs the whole program.
    '''
    data = get_json()
    print('To navigate through the file, enter one of the available\
 values.')
    print('Available keys: ')
    keys = list(iter(data.keys()))
    for key in keys:
        if key != keys[-1]:
            print(key, end=', ')
        else:
            print(key)
    try:
        result = check_input(data)
        return result
    except KeyError:
        return 'Incorrect value. Try again!'

if __name__ == '__main__':
    print(main())

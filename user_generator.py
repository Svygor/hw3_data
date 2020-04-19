import json
import csv
from csv import DictReader


def get_books_from_csv (csv_file='./data/books-39204-271043.csv'):
    with open(csv_file, newline='') as f:
        books = [book for book in csv.DictReader(f)]

    return books


def get_users_from_json(json_file='./data/users.json.py'):

    # Считываем массив пользователей
    with open(json_file, 'r') as f:
        users_list = json.loads(f.read())

    # Преобразовываем каждого пользователя в формат из example.json.py
    my_users = []
    my_keys = ['name', 'gender', 'address']
    for user in users_list:
        my_user = {}
        for key in my_keys:
            my_user[key] = user[key]
        my_user['books'] = []
        my_users.append(my_user)

    return my_users


def add_books_to_users(users, books):
    books = books[:10]
    print('кол-во людей:' + str(len(users)))
    print('кол-во книг:' + str(len(books)))
    for user, book in zip(users, books):
        user['books'].append(book)

    return users


users_new = get_users_from_json()
books_new = get_books_from_csv()
print(add_books_to_users(users_new, books_new))

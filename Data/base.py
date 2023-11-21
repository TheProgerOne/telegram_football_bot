import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error


def add_user(chat_id, name):
    try:
        with connect(
                host="localhost",
                user="root",
                password="",
                database="test",
                port=3307
        ) as connection:
            print("Connect Database")

            select_movies_query = f"INSERT INTO `users` (`user_id`, `name`, `tell_number`) VALUES ('{chat_id}', '{name}', '');"
            with connection.cursor() as cursor:
                cursor.execute(select_movies_query)

    except Error as e:
        print(e)

add_user(777, 'jamshid')
"""
    this code on local hast...
    soo please tern on your MySql first(XAMPP Control Panel)

"""

import mysql.connector


def create_database():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password=""
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE user_search")


def create_table():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="user_search"
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE userconnect (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")


# for add users in database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="user_search"
    )

def user_exists(cursor, username):
    cursor.execute("SELECT COUNT(*) FROM userconnect WHERE username = %s", (username,))
    return cursor.fetchone()[0] > 0

def insert_users_from_file(connection, file_path):
    cursor = connection.cursor()
    with open(file_path, 'r') as file:
        for line in file:
            username = line.strip()
            if username:
                if not user_exists(cursor, username):
                    cursor.execute("INSERT INTO userconnect (username) VALUES (%s)", (username,))
                    print(f"Added: {username}")
                else:
                    print(f"Skipped (already exists): {username}")
    connection.commit()


def start_database():
    try:
        create_database()
        print("Database created successfully")
    except:
        print('The database has been created.')
    try:
        create_table()
        print("Table created successfully")
    except:
        print('The table has been created.')

    # db_connection = connect_to_db()
    # insert_users_from_file(db_connection,'../usernames.txt')


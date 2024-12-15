"""
    this code on local hast...
    soo please tern on your MySql first(XAMPP Control Panel)

"""
"create_database.py"

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

    # اصلاح دستور SQL برای بستن پرانتز
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS userconnect (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE
        )
    """)
    mydb.close()


# for add users in database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="user_search"
    )

def add_username(username):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_search"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            query = "SELECT * FROM userconnect WHERE username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            if result:
                print(f"The username is {username} duplicate and could not be saved.")
            else:

                insert_query = "INSERT INTO userconnect (username) VALUES (%s)"
                cursor.execute(insert_query, (username,))
                connection.commit()
                print(f"{username} saved successfully.")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("The connection to the database was closed.")

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
        print("Database created successfully.")
    except Exception as e:
        print(f"The database has been created or an error occurred: {e}")

    try:
        create_table()
        print("Table created successfully.")
    except Exception as e:
        print(f"The table has been created or an error occurred: {e}")

# db_connection = connect_to_db()
# insert_users_from_file(db_connection,'../usernames.txt')



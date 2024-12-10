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

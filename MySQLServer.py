import mysql.connector

my_db =  mysql.connector.connect(
    host = 'localhost',
    user = "root",
    password = "@Eminemshady16"
)

if my_db.is_connected():
    print("Database 'alx_book_store' created successfully!")
else:
    print("Failed")

cursor = my_db.cursor()

my_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
cursor.execute(my_query)



cursor.close()
my_db.close()
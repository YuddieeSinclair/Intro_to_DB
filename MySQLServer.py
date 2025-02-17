import mysql.connector

my_db =  mysql.connector.connect(
    host = 'localhost',
    user = "root",
    password = "@Eminemshady16"
)

try:
    if not my_db.is_connected():
        raise mysql.connector.Error("connection failed!")
    else:
        print("Database 'alx_book_store' created successfully!")
    cursor = my_db.cursor()
    my_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
    cursor.execute(my_query)
except mysql.connector.Error as e: print(f"Error:{e}")
finally:
    cursor.close()
    my_db.close()
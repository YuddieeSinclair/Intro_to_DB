import mysql.connector

my_db =  mysql.connector.connect(
    host = 'localhost',
    user = "root",
    password = "@Eminemshady16"
)

try:
    my_db.is_connected()
    print("Database 'alx_book_store' created successfully!")
except:
    my_db.connector.Error()
    print("Failed")
else:
    cursor = my_db.cursor()
    my_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
    cursor.execute(my_query)

finally:
    cursor.close()
    my_db.close()
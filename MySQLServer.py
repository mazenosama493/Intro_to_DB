import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="01099589582mM@",  # Leave empty
        port=3307,
        database="alx_book_store"
    )
    if mydb.is_connected():
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as err:
    print(err)
finally:
    mycursor.close()
    mydb.close()
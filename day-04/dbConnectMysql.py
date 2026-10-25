import mysql.connector

try:
    # 1. Establish the connection to the MySQL Server
    # Change user, password, and port if your settings are different
    connection = mysql.connector.connect(
        host="localhost",      # Your database server address (127.0.0.1)
        user="root",           # Your MySQL username (default is root)
        password="",           # Your MySQL password (often empty for XAMPP)
        database="test_db"     # Name of the database you want to connect to
    )
    
    if connection.is_connected():
        print("Successfully connected to the MySQL database!")
        
        # 2. Create a cursor object to execute SQL commands
        cursor = connection.cursor()
        
        # 3. Example query: Fetch and print the server version
        cursor.execute("SELECT VERSION();")
        db_version = cursor.fetchone()
        print(f"MySQL Database Version: {db_version[0]}")
        
except mysql.connector.Error as error:
    print(f"Failed to connect to MySQL: {error}")

finally:
    # 4. Always close the connection when finished
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is now closed.")

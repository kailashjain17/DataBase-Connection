import mysql.connector
from urllib.parse import urlparse

# Define the connection parameters
mysql_url = "mysql://root:my-secret-pw@localhost:3307/mydatabase"

# Parse the MySQL URL using urllib.parse.urlparse
url_parts = urlparse(mysql_url)

# Extract connection parameters from the parsed URL
db_config = {
    'user': url_parts.username,
    'password': url_parts.password,
    'host': url_parts.hostname,
    'port': url_parts.port,
}

try:
    # Create a connection using the parsed parameters
    connection = mysql.connector.connect(**db_config)

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # Create a new database (if not using an existing one)
    cursor.execute("USE mydatabase;")
    print("Using database 'mydatabase'.")

    # Create a table in the new database (if not existing)
    cursor.execute("CREATE TABLE IF NOT EXISTS example_table ("
                   "id INT AUTO_INCREMENT PRIMARY KEY,"
                   "name VARCHAR(255) NOT NULL);")
    print("Table 'example_table' created successfully.")

    # Insert values into the table
    insert_query = "INSERT INTO example_table (name) VALUES (%s);"
    data = [("John",), ("Alice",), ("Bob",)]


    cursor.executemany(insert_query, data)
    connection.commit()
    print(f"{cursor.rowcount} row(s) inserted.")

    # Fetch and print the inserted data
    cursor.execute("SELECT * FROM example_table;")
    rows = cursor.fetchall()

    print("\nData in 'example_table':")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()

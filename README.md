# DataBase-Connection

Task: To Connect Docker MariaDB Container with Python


#Docker: To my best knowledge Docker is a Lightweight, Isolated, and Easily Accessible Software Technology. By Lightweight it means it is resource effective and #compatible, by isolated it is like an independent system under your host system, and lastly,by easily accessible it depicts scalability & accessibility.
#Installation:  go to https://docs.docker.com/docker-for-windows/install/
#Installation Docker according to your OS
#Complete the next steps using the default settings

#DataBase: To be specific Relational Database, it helps storing data in a structured manner. With respect to our project, it will help us store the user, machine and other related data in a controlled systematic way. 
	
	-MariaDB: MariaDB a MySQL sibling and an alternative to DBMS. 

#Terminal Connection To MariaDB Docker Container: 

#Image and Container: Image is like an OS system(in our case all things required to run MariaDB), they provide the blueprint for the program(containers) to run. Containers are the programs/ instances under Image running the actual purpose of DataBase(in our case). 

-Open Terminal
#Commands Used:
‘docker pull mariadb’  creates an image of mariadb
‘docker run -d -p 3307:3306 --name my-mariadb-container -e MYSQL_ROOT_PASSWORD=my-secret-pw mariadb’ makes a container named my-maria-container with a mysql root user password. 
‘docker image ls’ gives the list of the images
‘docker container ls’ gives the list of the containers
‘docker ps -a’ gives the status of the containers running 
‘docker exec -it my-mariadb-container bash’ this command opens an interactive bash shell for running mysql in the container
‘mysql -u root -p’  this command is used to connect to the mysql database


#Steps:
#Create an image: ‘docker pull mariadb’

#Create a Container: ‘docker run -d -p 3307:3306 --name my-mariadb-container -e MYSQL_ROOT_PASSWORD=my-secret-pw mariadb’
“-d = runs the container in the background
 -p = local port: remote port (3307 as 3306 the default port isn’t free)
“my-mariadb-container = name of the container
-e MYSQL_ROOT_PASSWORD=my-secret-pw = sets the MySQL root password”
	
#Check the Status: ‘docker ps -a’
	“ps = used to list docker containers
-a = used to showcase all the docker containers”


#Open an Interactive bash shell: ‘docker exec -it my-mariadb-container bash’
	“ exec = helps to executes the command
  it = allows to interact with the container
 bash = opens the interactive bash shell for accessing mysql ”

#Connect to MySQL server: ‘mysql -u root -p’
	“Used to connecting to the mysql server”

#Enter the Root Password: In this case, “my-secret-pw”

#Run Queries



#Python Connection To MariaDB Docker Container:

#Installation:
‘pip install mysql-connector-python’ used to connect mysql to database
‘pip install urlparse’ used to parse the mysql url’

#Code: 
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
Code: 

'''import mysql.connector
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
  '''

#This code uses the MySQL connector library to connect to the mariadb container using the  MySQL url. The urllib.parse is used to parse the url according to the database connection requirements. Cursor is used to execute MySQL commands.  

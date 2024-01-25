Sure, I'll help you improve the readability of your README content by adding relevant Markdown syntax. Here's an enhanced version:

```markdown
# Database Connection

## Task: Connect Docker MariaDB Container with Python

### Docker
Docker is a Lightweight, Isolated, and Easily Accessible Software Technology:
- **Lightweight**: Resource-effective and compatible.
- **Isolated**: Acts like an independent system under your host system.
- **Easily Accessible**: Depicts scalability & accessibility.

### Installation
1. Go to [Docker installation page](https://docs.docker.com/docker-for-windows/install/).
2. Install Docker according to your OS.
3. Complete the next steps using the default settings.

### Database
A relational database helps store data in a structured manner. For our project, MariaDB, a MySQL sibling, serves as an alternative to DBMS.

### Terminal Connection To MariaDB Docker Container
#### Commands Used:
```bash
docker pull mariadb        # creates an image of mariadb
docker run -d -p 3307:3306 --name my-mariadb-container -e MYSQL_ROOT_PASSWORD=my-secret-pw mariadb   # creates a container
docker image ls            # lists images
docker container ls        # lists containers
docker ps -a               # shows container status
docker exec -it my-mariadb-container bash   # opens an interactive bash shell
mysql -u root -p           # connects to the MySQL database
```

#### Steps:
1. **Create an image:** `docker pull mariadb`
2. **Create a Container:**
   ```bash
   docker run -d -p 3307:3306 --name my-mariadb-container -e MYSQL_ROOT_PASSWORD=my-secret-pw mariadb
   ```
   - `-d`: runs the container in the background
   - `-p`: local port: remote port (3307 as 3306 the default port isn’t free)
   - `my-mariadb-container`: name of the container
   - `-e MYSQL_ROOT_PASSWORD=my-secret-pw`: sets the MySQL root password

3. **Check the Status:** `docker ps -a`
   - `ps`: used to list docker containers
   - `-a`: used to showcase all the docker containers

4. **Open an Interactive bash shell:** `docker exec -it my-mariadb-container bash`
   - `exec`: helps to execute the command
   - `it`: allows interaction with the container
   - `bash`: opens the interactive bash shell for accessing mysql

5. **Connect to MySQL server:** `mysql -u root -p`
   - Used to connect to the MySQL server
6. **Enter the Root Password:** In this case, “my-secret-pw”

7. **Run Queries**

### Python Connection To MariaDB Docker Container
#### Installation:
```bash
pip install mysql-connector-python    # used to connect mysql to the database
pip install urlparse    # used to parse the MySQL URL
```

#### Code:
```python
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
```

This improved version uses Markdown for better structure and readability. Feel free to adjust it further based on your preferences.

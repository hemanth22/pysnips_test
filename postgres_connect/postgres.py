import psycopg2
import os

postgres_hostname = os.environ.get('postgres_hostname')
postgres_database = os.environ.get('postgres_database')
postgres_port = os.environ.get('postgres_port')
postgres_username = os.environ.get('postgres_username')
postgres_password = os.environ.get('postgres_password')

# Establishing the connection
conn = psycopg2.connect(
   database=postgres_database, user=postgres_username, password=postgres_password, host=postgres_hostname, port=postgres_port
)
# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ", data)

# Closing the connection
conn.close()

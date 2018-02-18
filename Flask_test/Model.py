import psycopg2

class Model():
    """description of class"""

    # Update connection string information obtained from the portal
    host = "localhost"
    user = "postgres"
    dbname = "Test"
    password = "info123"
    sslmode = "allow"

    # Construct connection string
    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string) 
    print ("Connection established")

    cursor = conn.cursor()

    def drop():
        # Drop previous table of same name if one exists
        cursor.execute("DROP TABLE IF EXISTS userTable;")
        print ("Finished dropping table (if existed)")

    def create():
        # Create table
        cursor.execute("CREATE TABLE userTable (id serial PRIMARY KEY, username VARCHAR(15), email VARCHAR(50), password VARCHAR(80));")
        print ("Finished creating table")


    def insert(username, email, password):
        # Insert some data into table
        hash_Pass = generate_password_hash(password)
        cursor.execute("INSERT INTO userTable (username, email, password) VALUES (%s, %s, %s);", (username, email , hash_Pass))
        print ("Inserted data into table")


    def read (id):
        cursor.execute("SELECT username FROM userTable WHERE id = %s;", (id))
        rows = cursor.fetchall()
        return rows


    def clean():
        # Cleanup
        conn.commit()
        cursor.close()
        conn.close()
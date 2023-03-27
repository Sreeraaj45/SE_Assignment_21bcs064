import mysql.connector

# Establish a connection to the database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='CulturalDestination'
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query to create a table
cur.execute("""
    CREATE TABLE artists (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        art_type VARCHAR(50),
        description TEXT
    )
""")

# Commit the transaction
conn.commit()

# Insert data into the table
cur.execute("""
    INSERT INTO artists (name, art_type, description)
    VALUES ('Riya Singh', 'Visual Art', 'Contemporary paintings'),
           ('Amit Patel', 'Music', 'Indian classical music'),
           ('Ravi Kumar', 'Theater', 'Regional theater performances'),
           ('Priya Sharma', 'Dance', 'Bharatanatyam dance performances')
""")

# Commit the transaction
conn.commit()

# Query the table for artist data
cur.execute("SELECT * FROM artists")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()

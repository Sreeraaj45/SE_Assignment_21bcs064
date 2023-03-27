import mysql.connector
import tkinter as tk

# Establish a connection to the database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='CulturalDestination'
)

# Define a function to fetch all data from the table
def fetch_data():
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query to fetch all data from the table
    cur.execute("SELECT * FROM artists")

    # Fetch all rows
    rows = cur.fetchall()

    # Create a new window to display the data
    data_window = tk.Toplevel(window)
    data_window.title("Artist Data")

    # Create a table to display the data
    table = tk.Frame(data_window, padx=10, pady=10)
    table.grid(row=0, column=0)

    # Create headers for the table
    id_label = tk.Label(table, text="ID", font=("bold", 12))
    id_label.grid(row=0, column=0, padx=5, pady=5)

    name_label = tk.Label(table, text="Name", font=("bold", 12))
    name_label.grid(row=0, column=1, padx=5, pady=5)

    art_type_label = tk.Label(table, text="Art Type", font=("bold", 12))
    art_type_label.grid(row=0, column=2, padx=5, pady=5)

    description_label = tk.Label(table, text="Description", font=("bold", 12))
    description_label.grid(row=0, column=3, padx=5, pady=5)

    # Loop through the rows and insert data into the table
    for i, row in enumerate(rows):
        id_label = tk.Label(table, text=row[0])
        id_label.grid(row=i+1, column=0, padx=5, pady=5)

        name_label = tk.Label(table, text=row[1])
        name_label.grid(row=i+1, column=1, padx=5, pady=5)

        art_type_label = tk.Label(table, text=row[2])
        art_type_label.grid(row=i+1, column=2, padx=5, pady=5)

        description_label = tk.Label(table, text=row[3])
        description_label.grid(row=i+1, column=3, padx=5, pady=5)

    # Close the cursor
    cur.close()

# Create a GUI window
window = tk.Tk()
window.title("Fetch Data")

# Create a button to fetch data from the table
fetch_button = tk.Button(window, text="Fetch Data", command=fetch_data)
fetch_button.pack(padx=10, pady=10)

# Run the GUI loop
window.mainloop()

import mysql.connector
import tkinter as tk

# Establish a connection to the database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='CulturalDestination'
)

# Define a function to sort data by art type
def sort_by_art_type():
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query to fetch data from the table and sort by art type
    cur.execute("SELECT * FROM artists ORDER BY art_type")

    # Fetch all rows
    rows = cur.fetchall()

    # Create a new window to display the sorted data
    sorted_window = tk.Toplevel(window)
    sorted_window.title("Artists Sorted by Art Type")

    # Create a table to display the sorted data
    table = tk.Frame(sorted_window, padx=10, pady=10)
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
window.title("Sort Data")

# Create a button to sort data by art type
sort_button = tk.Button(window, text="Sort by Art Type", command=sort_by_art_type)
sort_button.pack(padx=10, pady=10)

# Run the GUI loop
window.mainloop()

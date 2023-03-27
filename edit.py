import mysql.connector
import tkinter as tk

# Establish a connection to the database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='CulturalDestination'
)

# Define a function to retrieve data from the table and display it in a table
def show_data():
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query to fetch data from the table
    cur.execute("SELECT * FROM artists")

    # Fetch all rows
    rows = cur.fetchall()

    # Clear the table widget before inserting new rows
    clear_table()

    # Insert the retrieved data into the table
    for i, row in enumerate(rows):
        id_label = tk.Label(table, text=row[0])
        id_label.grid(row=i+1, column=0, padx=5, pady=5)

        name_entry = tk.Entry(table)
        name_entry.insert(0, row[1])
        name_entry.grid(row=i+1, column=1, padx=5, pady=5)

        art_type_entry = tk.Entry(table)
        art_type_entry.insert(0, row[2])
        art_type_entry.grid(row=i+1, column=2, padx=5, pady=5)

        description_entry = tk.Entry(table)
        description_entry.insert(0, row[3])
        description_entry.grid(row=i+1, column=3, padx=5, pady=5)

    # Close the cursor
    cur.close()

# Define a function to clear the table widget
def clear_table():
    for widget in table.winfo_children():
        widget.destroy()

# Define a function to update the data in the database
def update_data():
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Loop through the table rows and update the data in the database
    for widget in table.winfo_children():
        if isinstance(widget, tk.Entry):
            column = widget.grid_info()['column']
            row = widget.grid_info()['row'] - 1
            if column == 1:
                cur.execute("UPDATE artists SET name=%s WHERE id=%s", (widget.get(), row+1))
            elif column == 2:
                cur.execute("UPDATE artists SET art_type=%s WHERE id=%s", (widget.get(), row+1))
            elif column == 3:
                cur.execute("UPDATE artists SET description=%s WHERE id=%s", (widget.get(), row+1))

    # Commit the changes to the database
    conn.commit()

    # Close the cursor
    cur.close()

# Create a GUI window
window = tk.Tk()
window.title("Edit Data")

# Create a button to show the data in the table
show_button = tk.Button(window, text="Show Data", command=show_data)
show_button.pack(padx=10, pady=10)

# Create a table to display the data
table = tk.Frame(window, padx=10, pady=10)
table.pack()

# Create headers for the table
id_label = tk.Label(table, text="ID", font=("bold", 12))
id_label.grid(row=0, column=0, padx=5, pady=5)

name_label = tk.Label(table, text="Name", font=("bold", 12))
name_label.grid(row=0, column=1, padx=5, pady=5)

art_type_label = tk.Label(table, text="Art Type", font=("bold", 12))
art_type_label.grid(row=0, column=2, padx=5, pady=5)

description_label = tk.Label(table, text="Description", font=("bold", 12))
description_label.grid(row=0, column=3, padx=5, pady=5)

# Create a button to update the data in the database
update_button = tk.Button(window, text="Update Data", command=update_data)
update_button.pack(padx=10, pady=10)

# Run the GUI loop
window.mainloop()

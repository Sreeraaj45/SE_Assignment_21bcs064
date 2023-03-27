import mysql.connector
import tkinter as tk

# Establish a connection to the database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='CulturalDestination'
)

# Create a global variable for the number of rows in the table
num_rows = 0

# Define a function to retrieve data from the table and display it in a table
def show_data():
    global num_rows
    
    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query to fetch data from the table
    cur.execute("SELECT * FROM artists")

    # Fetch all rows
    rows = cur.fetchall()
    
    # Get the number of rows in the table
    num_rows = len(rows)

    # Clear the table widget before inserting new rows
    clear_table()

    # Insert the retrieved data into the table
    for i, row in enumerate(rows):
        id_label = tk.Label(table, text=row[0])
        id_label.grid(row=i+1, column=0, padx=5, pady=5)
        
        name_label = tk.Label(table, text=row[1])
        name_label.grid(row=i+1, column=1, padx=5, pady=5)

        art_type_label = tk.Label(table, text=row[2])
        art_type_label.grid(row=i+1, column=2, padx=5, pady=5)

        description_label = tk.Label(table, text=row[3])
        description_label.grid(row=i+1, column=3, padx=5, pady=5)
        
        delete_button = tk.Button(table, text="Delete", command=lambda x=i+1: delete_row(x))
        delete_button.grid(row=i+1, column=4, padx=5, pady=5)

    # Close the cursor
    cur.close()

# Define a function to clear the table widget
def clear_table():
    for widget in table.winfo_children():
        if isinstance(widget, tk.Button):
            continue
        widget.destroy()

# Define a function to delete a row from the database
def delete_row(row_num):
    # Open a cursor to perform database operations
    cur = conn.cursor()
    
    # Execute a query to delete the row from the database
    cur.execute("DELETE FROM artists WHERE id=%s", (row_num,))
    
    # Decrement the IDs of rows after the deleted row
    for i in range(row_num+1, num_rows+1):
        cur.execute("UPDATE artists SET id=%s WHERE id=%s", (i-1, i))

    # Commit the changes to the database
    conn.commit()

    # Close the cursor
    cur.close()
    
    # Update the table display
    show_data()

# Create a GUI window
window = tk.Tk()
window.title("Delete Data")

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

# Run the GUI loop
window.mainloop()

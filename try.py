import mysql.connector
import tkinter as tk

# Establish a connection to the database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='CulturalDestination'
)

# Define a function to submit the form
def submit_form():
    # Get the values entered in the form
    name = name_entry.get()
    art_type = art_type_entry.get()
    description = description_entry.get()

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query to insert data into the table
    cur.execute("""
        INSERT INTO artists (name, art_type, description)
        VALUES (%s, %s, %s)
    """, (name, art_type, description))

    # Commit the transaction
    conn.commit()

    # Display a success message
    success_label.config(text="Form submitted successfully!")

    # Close the cursor
    cur.close()

# Create a GUI window
window = tk.Tk()
window.title("Submit Form")

# Create a form for the user to enter details
name_label = tk.Label(window, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=5, pady=5)

art_type_label = tk.Label(window, text="Art Type:")
art_type_label.grid(row=1, column=0, padx=5, pady=5)
art_type_entry = tk.Entry(window)
art_type_entry.grid(row=1, column=1, padx=5, pady=5)

description_label = tk.Label(window, text="Description:")
description_label.grid(row=2, column=0, padx=5, pady=5)
description_entry = tk.Entry(window)
description_entry.grid(row=2, column=1, padx=5, pady=5)

submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.grid(row=3, column=1, padx=5, pady=5)

success_label = tk.Label(window, text="")
success_label.grid(row=4, column=1, padx=5, pady=5)

# Run the GUI loop
window.mainloop()
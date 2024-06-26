# Address book application

# Connect to Database

def intialize_database():
    cursor.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, mobile_number TEXT, email_address TEXT, address TEXT)")


# Function to create a new contact
def add_contact():
    first_name = input("First name = ")
    last_name = input("Last name = ")
    mobile_number = input("Mobile number = ")
    email_address = input("Email address = ")
    address = input("Address = ")

    cursor.execute("INSERT INTO contacts (first_name, last_name, mobile_number, email_address, address) VALUES (?, ?, ?, ?, ?)", (first_name, last_name, mobile_number, email_address, address))
    connection.commit()
    print(f"Contact '{name} added successfully")

# Function to search for contact
def search_contact():
    name = input("Enter name to search: ")
    cursor.execute("SELECT * FROM contacts WHERE first_name = ? OR last_name = ?", (name, name))
    contacts = cursor.fetchall()

    if contacts:
        for contact in contacts:
            print("\nContact details:")
            print(f"First name: {contact[1]}")
            print(f"Last name: {contact[2]}")
            print(f"Mobile number: {contact[3]}")
            print(f"Email address: {contact[4]}")
            print(f"Address: {contact[5]}")
    else:
        print(f"No contact found with name '{name}'")

# Function to edit contact
def edit_contact():
    name = input("Enter name to edit: ")
    cursor.execute("SELECT * FROM contacts WHERE first_name = ? OR last_name = ?", (name, name))
    contacts = cursor.fetchall()

    if contacts:
        for contact in contacts:
            print("\nContact details:")
            print(f"First name: {contact[1]}")
            print(f"Last name: {contact[2]}")
            print(f"Mobile number: {contact[3]}")
            print(f"Email address: {contact[4]}")
            print(f"Address: {contact[5]}")

        print("\nEdit contact:")
        first_name = input("First name = ")
        last_name = input("Last name = ")
        mobile_number = input("Mobile number = ")
        email_address = input("Email address = ")
        address = input("Address = ")

        cursor.execute("UPDATE contacts SET first_name = ?, last_name = ?, mobile_number = ?, email_address = ?, address = ? WHERE first_name = ? OR last_name = ?", (first_name, last_name, mobile_number, email_address, address, name, name))
        connection.commit()
        print(f"Contact '{name}' updated successfully")
    else:
        print(f"No contact found with name '{name}'")

# Function to delete contact
def delete_contact():
    name = input("Enter name to delete: ")
    cursor.execute("SELECT * FROM contacts WHERE first_name = ? OR last_name = ?", (name, name))
    contacts = cursor.fetchall()

    if contacts:
        for contact in contacts:
            print("\nContact details:")
            print(f"First name: {contact[1]}")
            print(f"Last name: {contact[2]}")
            print(f"Mobile number: {contact[3]}")
            print(f"Email address: {contact[4]}")
            print(f"Address: {contact[5]}")

        confirm = input("Are you sure you want to delete this contact? (y/n): ")

        if confirm == "y":
            cursor.execute("DELETE FROM contacts WHERE first_name = ? OR last_name = ?", (name, name))
            connection.commit()
            print(f"Contact '{name}' deleted successfully")
    else:
        print(f"No contact found with name '{name}'")


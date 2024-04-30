# Address book application

# Connect to Database

def intialize_database():
    cursor.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, mobile_number TEXT, email_address TEXT, address TEXT)")



# Address Book Name
print("My Address Book")

# Address book input
first_name = input("First name = ")
last_name = input("Last name = ")
mobile_number = input("Mobile number = ")
email_address = input("Email address = ")
address = input("Address = ")

def main():
    initialize_database()

    while True:
        print("\nAddress Book List:")
        print("1. Add Contact")
        print("2. Search Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            break
        else:
            print("Invalid choice")
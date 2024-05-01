# System packages
import os.path

# External packages
from colored import Fore, Back, Style

# Imports of our own functions
from archive.todo_functions import *

print(f"{Fore.red}{Back.green}Address Book{Style.reset}")

def create_menu():
    print("1. Add contact")
    print("2. Search contact")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. Exit")

    user_choice = input("Enter your selection: ")
    return user_choice

file_name = "list.csv"

# if the file doesn't exist
if (not os.path.isfile(file_name)):
    print("Creating file as it doesn't exist")
    # Create the file
    todo_file = open(file_name, "w")
    # we will enter the headings into the file
    todo_file.write("first_name, last_name, mobile, email_address, address\n")
    # Close the file
    todo_file.close()

choice = ""

while choice != "5":
    choice = create_menu()

    if (choice == "1"):
        add_todo(file_name)
    elif (choice == "2"):
        remove_todo(file_name)
    elif (choice == "3"):
        mark_todo(file_name)
    elif (choice == "4"):
        view_todo(file_name)
    elif (choice == "5"):
        print("You entered 5.")
    else:
        print("Please only enter the options shown above.")
    


print("Thank you for using our todo list application")
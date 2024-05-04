# Python packages - will already be installed within Python
import os.path


# External packages to be installed
from colored import Fore, Back, Style


# Creating the menu for the Task List


# Imports of the terminal application
from tasklist_functions import create_task_list, create_add_task, create_edit_task, create_view_tasks, create_delete_task, create_delete_task_list


print(f"{Style.bold}{Fore.magenta}💻 Plan Your Life | Task List 💻{Style.reset}")

# Terminal application menu
def create_menu():
    print("1. Create a List")
    print("2. Add Task to List")
    print("3. Edit a Task")
    print("4. View Lists")
    print("5. Delete Task")
    print("6. Delete List")
    print("7. Exit")

    user_choice = input("Enter your selection (1-7): ")
    return user_choice

file_name = "list.csv"

# create the file if it doesn't exist - need to test as I have this as option 1. Hopefully both dont count the other out.
if (not os.path.isfile(file_name)):
    print("Creating file as it doesn't exist")
    # Create the file (or list)
    tasklist = open(file_name, "w")
    # headings in the file
    tasklist.write("Task, Status")
    # closing the file
    tasklist.close()

choice = ""
# menu options
while choice != "7":
    choice = create_menu()

    if (choice == "1"):
        create_task_list(file_name)
    elif (choice =="2"):
        create_add_task(file_name)
    elif (choice =="3"):
        create_edit_task(file_name)
    elif (choice =="4"):
        create_view_tasks(file_name)    
    elif (choice =="5"):
        create_delete_task(file_name)
    elif (choice =="6"):
        create_delete_task_list(file_name)
    elif (choice =="7"):
        print("Exiting Plan Your Life | Task List.")    
        break
    else:
        print("Invalid option. Please select between 1-7.")

print(f"{Style.bold}{Fore.light_magenta}👋 Thank you and have a great day 👋")

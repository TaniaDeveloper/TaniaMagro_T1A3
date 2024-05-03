import os.path

# Creating the menu for the Task List

from tasklist_functions import create_task_list, create_add_task, create_edit_task, create_view_tasks, create_delete_task, create_delete_task_list

print("Plan Your Life | Task List")

def create_menu():
    print("1. Create a List")
    print("2. Add Task to List")
    print("3. Edit a Task")
    print("4. View Lists")
    print("5. Delete Task")
    print("6. Delete List")
    print("7. Exit")

    user_choice = input("Enter your selection (1-7): ")
    print(create_menu())
    return user_choice

file_name = "list.csv"

choice = ""
# menu options
while choice != "7":
    choice = create_menu()

    if (choice == "1"):
        create_task_list()
    elif (choice =="2"):
        create_add_task()
    elif (choice =="3"):
        create_edit_task()
    elif (choice =="4"):
        create_view_tasks()    
    elif (choice =="5"):
        create_delete_task()
    elif (choice =="6"):
        create_delete_task_list()
    elif (choice =="7"):
        print("Exiting Plan Your Life | Task List.")    
        break
    else:
        print("Invalid option. Please select between 1-7.")

print("Thank you and have a great day")
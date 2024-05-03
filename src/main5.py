# Creating the menu for the Task List

from tasklist_functions import create_task_list, add_task_list, edit_task_list, view_list, delete_task, delete_list

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

choice = ""

while choice != "7":
    choice = create_menu()

    if (choice == "1"):
        print("Entered 1.")
    elif (choice =="2"):
        print("Entered 2.")
    elif (choice =="3"):
        print("Entered 3.")
    elif (choice =="4"):
        print("Entered 4.")    
    elif (choice =="5"):
        print("Entered 5.")
    elif (choice =="6"):
        print("Entered 6.")
    elif (choice =="7"):
        print("Entered 7.")    
    else:
        print("Invalid option. Please select between 1-7.")

print("Thank you and have a great day")
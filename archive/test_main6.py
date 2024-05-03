import csv
import os

# Function to create a new task list
def create_task_list():
    list_name = input("Enter the name for your new task list: ")
    filename = list_name.lower().replace(" ", "_") + ".csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Task", "Status"])

# Function to add a task to a list
def add_task():
    list_name = input("Enter the name of the task list: ")
    filename = list_name.lower().replace(" ", "_") + ".csv"
    task_name = input("Enter the task to add: ")
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([task_name, "Pending"])

# Function to edit a task
def edit_task():
    list_name = input("Enter the name of the task list: ")
    filename = list_name.lower().replace(" ", "_") + ".csv"
    task_name = input("Enter the task to edit: ")
    new_status = input("Enter the new status (e.g., 'Completed', 'Pending'): ")
    
    # Read current tasks and update the specified task
    tasks = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        tasks = [row for row in reader]
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for task in tasks:
            if task[0] == task_name:
                task[1] = new_status
            writer.writerow(task)

# Function to view tasks in a list
def view_tasks():
    list_name = input("Enter the name of the task list: ")
    filename = list_name.lower().replace(" ", "_") + ".csv"
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]} - Status: {row[1]}")

# Function to delete a task
def delete_task():
    list_name = input("Enter the name of the task list: ")
    filename = list_name.lower().replace(" ", "_") + ".csv"
    task_name = input("Enter the task to delete: ")
    
    # Read current tasks and filter out the specified task
    tasks = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        tasks = [row for row in reader if row[0] != task_name]
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow(task)

# Function to delete a task list
def delete_task_list():
    list_name = input("Enter the name of the task list to delete: ")
    filename = list_name.lower().replace(" ", "_") + ".csv"
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Task list '{list_name}' has been deleted.")
    else:
        print("Task list not found.")

# Main function to run the task list program
def main():
    while True:
        print("\nTask List Manager")
        print("1. Create a List")
        print("2. Add Task to List")
        print("3. Edit a Task")
        print("4. View Lists")
        print("5. Delete Task")
        print("6. Delete List")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            create_task_list()
        elif choice == '2':
            add_task()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            view_tasks()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            delete_task_list()
        elif choice == '7':
            print("Exiting Task List Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()

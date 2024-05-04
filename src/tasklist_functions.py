import csv

# creating the task list

def create_task_list(file_name):
    list_name = input("Create your new list: ")           
    file_name = list_name.lower().replace(" ", "_") + ".csv"
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Task", "Status"])


# Adding a task to a list
def create_add_task(file_name):
    list_name = input("Enter the name of the Task List: ")
    file_name = list_name.lower().replace(" ", "_") + ".csv"
    task_name = input("Add the task to your list: ")
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([task_name, "Pending"])
    

# retrieving the list to edit a task
def create_edit_task(file_name):
    list_name = input("Enter the name of the task list:")
    file_name = list_name.lower().replace(" ", "_") + ".csv"
    task_name = input("Enter the task to edit: ")
    new_status = input("Enter the new status: ")
    print("edit_task")


    # Read and update a specified task
    tasks = [file_name]
    with open(file_name, 'r', newline= '') as file:
        reader = csv.reader(file)
        tasks = [row for row in reader]
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for task in tasks:
            if task[0] == task_name:
                task[1] = new_status
            writer.writerow(task)
    

# function to view tasks in a list
def create_view_tasks(file_name):
    list_name = input("Enter the name of the task list: ")
    file_name = list_name.lower().replace(" ", "_") + ".csv"
    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"{row[0]} - Status: {row[1]}")


# Deleting tasks from a specified list
def create_delete_task(file_name):
    list_name = input("Enter the name of the task list: ")
    file_name = list_name.lower().replace(" ", "_") + ".csv"
    task_name = input("Enter the task to delete:")

    # Read and delete a specified task
    tasks = [file_name]
    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file)
        tasks = [row for row in reader if row[0] != task_name]

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow(task)


# Deleting lists
def create_delete_task_list(file_name):
    list_name = input("Enter the name of the task list: ")
    file_name = list_name.lower().replace(" ", "_") + ".csv"
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"Task list '{list_name}' has been deleted.")
    else:
        print("Task list not found.")



import csv

# creating the task list

def create_task_list(file_name):
    list_name = input("Create your new list")           # Should this be called list_name or Todo_name???
    file_name = list_name.lower().replaced(" ", "_") + ".csv"
    with open(file_name, 'w', newline=) as f:
        writer = csv.writer(f)
        writer.writerow(["Task", "Status"])

# creating add task
def create_add_task():
    list_name = input("Enter the name of the Task List: ")
    file_name = list_name.lower()replace(" ", "_") + ".csv"
    task_name = input("Add the task to your list: ")
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([task_name, "Pending"])
    

# function to edit task
def create_edit_task():
    print("edit_task")


# function to view tasks in a list
def create_view_tasks(file_name):
    list_name = input("Enter the name of the task list: ")
    
    print("view_tasks")


# creating delete tasks
def create_delete_task():
    print("delete_task")


# creating delete tasks list
def create_delete_task_list():
    print("delete_task_list")


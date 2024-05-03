# creating the task list

def create_task_list():
    list_name = input("Create your new list")
    filename = list_name.lower().replaced(" ", "_") + ".csv"
# creating 
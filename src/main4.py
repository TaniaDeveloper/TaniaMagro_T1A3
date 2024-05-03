

tasks = []

# creating add task function
def addTask():
    task = input ("Please enter a task: ")         
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

# creating list of tasks
def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")


# creating delete task function
def deleteTask():
    listTasks()
    try:
        taskToDelete - int(input("Enter the # to delete: "))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(tasksToDelete)
            print(f"Task {taskToDelete} has been removed")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except:
        print("Invalid option.")

if __name__ == "__main__":
# Create a loop to run the application
    print ("Plan Your Life - Task List")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("_________________________________")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Created functions 
        if(choice == "1")
            addTask()
        elif(choice == "2")
            deleteTask()
        elif(choice == "3")
            listTasks()
        elif(choice == "4")
            break

else:
    print("Invalid selction. Please try again.")



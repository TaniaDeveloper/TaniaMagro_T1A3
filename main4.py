tasks = []

if __name__ == "__main__":

# Create a loop to run the application

print ("Welcome to your task list")
while True:
    print("\n")
    print("Please select one of the following options")
    print("_________________________________")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List tasks")
    print("4. Exit")

choice = input("Enter your choice: ")

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


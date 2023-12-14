import os
# List to store tasks
tasks = []
# Function to display the main menu
def show_menu():
    print("--To-Do-List Menu--")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Save and Quit")
# Function to add a task to the list
def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")
# Function to view all tasks in the list
def view_tasks():
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{i}. {task['task']} - {status}")
# Function to update the status of a task
def update_task():
    view_tasks()
    index = int(input("Enter the task number to update: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = not tasks[index]["completed"]
        print("Task updated successfully!")
    else:
        print("Invalid task number.")
# Function to save tasks to a text file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['completed']}\n")
# Function to load tasks from a text file
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                task_info = line.strip().split("|")
                tasks.append({"task": task_info[0], "completed": task_info[1] == "True"})
# Entry point of the script
if __name__ == "__main__":
    # Load tasks from the file when the script starts
    load_tasks()
    # Main loop for user interaction
    while True:
        # Display the menu and get user input
        show_menu()
        choice = input("Enter your choice (1-4): ")
        # Perform actions based on user choice
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            # Save tasks to the file and exit the loop
            save_tasks()
            print("Tasks saved. Quitting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

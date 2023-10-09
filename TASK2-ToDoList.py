tasks = []

filename = "task_list.txt"

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

def delete_task(task_index):
    try:
        del tasks[task_index]
        print("Task deleted successfully!")
    except IndexError:
        print("Invalid task index. Task not deleted.")

def view_tasks():
    if tasks:
        print("Task List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("Task list is empty.")

def save_tasks():
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")
        print("Tasks saved successfully!")

def load_tasks():
    try:
        with open(filename, "r") as file:
            global tasks
            tasks = [line.strip() for line in file]
        print("Tasks loaded successfully!")
    except FileNotFoundError:
        print("Task list file not found.")

while True:
    print("\nTO-D0 LIST MENU:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Save Tasks")
    print("5. Load Tasks")
    print("6. Exit")

    choice = input("Enter your choice (1 | 2 | 3 | 4 | 5 | 6 ): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
        task_index = int(input("Enter the index of the task to delete: ")) - 1
        delete_task(task_index)
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        save_tasks()
    elif choice == "5":
        load_tasks()
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

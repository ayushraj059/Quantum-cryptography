import os

tasks = []

def show_menu():
    print("\n📋 TO-DO LIST MENU")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Save Tasks to File")
    print("5. Load Tasks from File")
    print("6. Exit")

def view_tasks():
    if not tasks:
        print("\n✅ No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added ✅")

def remove_task():
    view_tasks()
    try:
        index = int(input("Enter task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Removed task: {removed} ❌")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    print("Tasks saved to tasks.txt 💾")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            loaded = f.readlines()
            global tasks
            tasks = [task.strip() for task in loaded]
        print("Tasks loaded from file 📂")
    else:
        print("No saved tasks found.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        save_tasks()
    elif choice == '5':
        load_tasks()
    elif choice == '6':
        print("Exiting... Bye! 👋")
        break
    else:
        print("Invalid option. Try again.")

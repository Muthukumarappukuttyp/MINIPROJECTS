def display_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Display Live Tasks")
    print("4. Display Completed Tasks")
    print("5. Exit")

def add_task(tasks):
    tasks.append(input("Enter task description: "))
    print("Task added successfully!")

def view_tasks(tasks, message="Live Tasks"):
    print(f"\n{message}:")
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print(f"No {message.lower()}.")

def update_task(tasks, completed_tasks):
    if tasks:
        view_tasks(tasks)
        index = int(input("Enter task index to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            completed_tasks.append(tasks.pop(index))
            print("Task marked as done.")
        else:
            print("Invalid task index.")
    else:
        print("No tasks to mark as done.")

def save_tasks(tasks, completed_tasks):
    with open("tasks.txt", "w") as f:
        f.write("Live Tasks:\n" + "\n".join(tasks) + "\n\nCompleted Tasks:\n" + "\n".join(completed_tasks))

def load_tasks():
    tasks, completed_tasks = [], []
    try:
        with open("tasks.txt", "r") as f:
            lines = f.read().splitlines()
            if "Live Tasks:" in lines:
                tasks = lines[lines.index("Live Tasks:") + 1 : lines.index("Completed Tasks:")]
                completed_tasks = lines[lines.index("Completed Tasks:") + 1:]
    except FileNotFoundError:
        pass
    return tasks, completed_tasks

def main():
    tasks, completed_tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            update_task(tasks, completed_tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            view_tasks(completed_tasks, "Completed Tasks")
        elif choice == '5':
            save_tasks(tasks, completed_tasks)
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
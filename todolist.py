# to_do_list

def show_tasks():
    try:
        file = open("tasks.txt", "r")
        tasks = file.readlines()
        file.close()

        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            index = 1
            for task in tasks:
                print(str(index) + ". " + task.strip())
                index += 1
    except FileNotFoundError:
        print("No tasks yet. Start by adding some!")

def add_task():
    task = input("Enter a new task (or 0 to cancel): ").strip()
    if task == "0":
        print("Add task cancelled.")
        return

    file = open("tasks.txt", "a")
    file.write(task + "\n")
    file.close()
    print("Task added!")

def delete_task():
    show_tasks()
    try:
        choice = input("Enter task number to delete (or 0 to cancel): ")
        task_number = int(choice)

        if task_number == 0:
            print("Delete cancelled.")
            return

        file = open("tasks.txt", "r")
        tasks = file.readlines()
        file.close()

        if task_number >= 1 and task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            file = open("tasks.txt", "w")
            file.writelines(tasks)
            file.close()
            print("Deleted: " + removed.strip())
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

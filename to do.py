import os

# Function to display the command menu
def display_menu():
    print("Command Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Edit task")
    print("4. Delete task")
    print("5. Mark task as complete")
    print("6. Sort tasks")
    print("7. Save and Quit")

# Function to load tasks from tasks.txt file
def load_tasks():
    tasks = []
    try:
        with open('tasks.txt', 'r') as f:
            for line in f:
                description, completed = line.strip().split(',')
                tasks.append({'description': description, 'completed': completed == 'True'})
    except FileNotFoundError:
        pass  # File will be created when saving tasks for the first time
    return tasks

# Function to save tasks to tasks.txt file
def save_tasks(tasks):
    with open('tasks.txt', 'w') as f:
        for task in tasks:
            f.write(f"{task['description']},{task['completed']}\n")

# Function to view tasks
def view_tasks(tasks):
    print("Tasks:")
    if not tasks:
        print("No tasks.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['description']} {'(Complete)' if task['completed'] else ''}")

# Function to add a new task
def add_task(tasks):
    description = input("Enter task description: ")
    tasks.append({'description': description, 'completed': False})
    print("Task added.")

# Function to edit a task
def edit_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter task number to edit: "))
    if 1 <= task_number <= len(tasks):
        new_description = input("Enter new description: ")
        tasks[task_number - 1]['description'] = new_description
        print("Task edited.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter task number to delete: "))
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        print("Task deleted.")
    else:
        print("Invalid task number.")

# Function to mark a task as complete
def complete_task(tasks):
    view_tasks(tasks)
    task_number = int(input("Enter task number to mark as complete: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

# Function to sort tasks alphabetically by description
def sort_tasks(tasks):
    tasks.sort(key=lambda x: x['description'].lower())
    print("Tasks sorted alphabetically.")

# Main function to run the To-Do List application
def main():
    tasks = load_tasks()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            complete_task(tasks)
        elif choice == '6':
            sort_tasks(tasks)
        elif choice == '7':
            save_tasks(tasks)
            print("Tasks saved. Quitting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()

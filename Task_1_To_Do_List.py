# Simple To-Do List

# Choice 1: function To display the to-do list
def display_todo_list(todo_list):
    print("\nYour To-Do List:")
    print("*****************************************")
    if not todo_list:
        print("No tasks in your list.")
    else:
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    print("*****************************************")

# Choice 2: function to add task
def add_task(todo_list):
    task = input("Enter the task you want to add: ")
    print("*****************************************")
    todo_list.append(task)
    print(f"Task '{task}' added to your list.")
    print("*****************************************")

# Choice 3: function to update task
def update_task(todo_list):
    display_todo_list(todo_list)   
    try:
        task_number = int(input("Enter the number of the task you want to update: "))     
        print("*****************************************")  
        if 1 <= task_number <= len(todo_list):
            new_task = input("Enter the new task: ")
            todo_list[task_number - 1] = new_task
            print("*****************************************")  
            print(f"Task {task_number} updated to '{new_task}'.")
        else:            
            print("Invalid task number.")           
    except ValueError:
        print("Please enter a valid number.")
    print("*****************************************")

# Choice 4: function to remove task
def remove_task(todo_list):
    display_todo_list(todo_list)  #display the existing task
    try:
        task_number = int(input("Enter the number of the task you want to remove: "))
        print("*****************************************")
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"Task '{removed_task}' removed from your list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    print("*****************************************")

# main function which include choices
def main():
    todo_list = [] # empty list
    while True:
        print("\nMenu:")
        print("1. View To-Do List")
        print("2. Add a Task")
        print("3. Update Task")
        print("4. Remove a Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            display_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            update_task(todo_list)
        elif choice == '4':
            remove_task(todo_list)
        elif choice == '5':
            print("************** Thank you ****************")
            print("Exiting the To-Do List application.")
            print("*****************************************")
            break
        else:
            print("Invalid choice. please select a valid option.")

#by using this program the script can run directly
if __name__ == "__main__":
    main()

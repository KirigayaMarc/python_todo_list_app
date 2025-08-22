# Marc
# First python application

tasks = []
#creating a function here to use for the view option.
def view_tasks(tasks_list):
    for task in tasks_list:
        print(f"Tasks: {task}")
#creating a function here to use for the add option.      
def add_task(tasks_list):
    new_task = input("What task do you want to add?: ")
    tasks_list.append(new_task)
    
while True:
    choice = input("What would you like to do? (add, view, quit): ")
    if choice == "quit":
        break
    elif choice == "view":
        view_tasks(tasks)
    elif choice == "add":
        add_task(tasks)
    else:
        print("Not a valid selection! Try Again")

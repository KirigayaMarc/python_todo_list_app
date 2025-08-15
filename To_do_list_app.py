# Marc
# First python application

tasks = []

while True:
    choice = input("What would you like to do? (add, view, quit): ")
    if choice == "quit":
        break
    elif choice == "view":
        for task in tasks:
            print(f"Tasks: {task}")
    elif choice == "add":
        new_task = input("What task do you want to add?: ")
        tasks.append(new_task)
    else:
        print("Not a valid selection! Try Again")
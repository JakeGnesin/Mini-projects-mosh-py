
# # loop
# #  A
# #  if not valid 1-4 print 'not valid chocie'
# # if 1 show task list
# # if 2 add if 3 remove if 4 break and exit program.

# OPTIONS = [
#     '1. View tasks',
#     '2. Add task',
#     '3. Remove task',
#     '4. Exit'
# ]

# choice = int(input('Enter choice: '))
# Tasks = []

# while True:
#     def menu():
#         print(OPTIONS)

#     def choose_option():
#         if choice == 1:
#             print(Tasks)
#         elif choice == 2:
#             new_task = input('Enter task: ')
#             Tasks[new_task]
#         elif choice == 3:
#             remove_choice = input("Enter task to remove: ")
#             Tasks[remove_choice]
#         elif choice == 4:
#             print('bye')
#         else:
#             print('Invalid choice')

def main():
    # Define options as a list
    OPTIONS = [
        '1. View tasks',
        '2. Add task',
        '3. Remove task',
        '4. Exit'
    ]

    # Initialize empty tasks list
    Tasks = []

    # Main loop
    while True:
        # Display menu
        def menu():
            for option in OPTIONS:
                print(option)

        # Handle user choice
        def choose_option(choice):
            if choice == 1:
                if Tasks:
                    print("Current tasks:")
                    for i, task in enumerate(Tasks, 1):
                        print(f"{i}. {task}")
                else:
                    print("No tasks yet!")
            elif choice == 2:
                new_task = input('Enter task: ')
                Tasks.append(new_task)  # Use append() to add to list
                print(f"Added: {new_task}")
            elif choice == 3:
                if Tasks:
                    print("Current tasks:")
                    for i, task in enumerate(Tasks, 1):
                        print(f"{i}. {task}")
                    remove_choice = input("Enter task number to remove: ")
                    try:
                        index = int(remove_choice) - 1
                        # Use pop() to remove from list
                        removed_task = Tasks.pop(index)
                        print(f"Removed: {removed_task}")
                    except (ValueError, IndexError):
                        print("Invalid task number")
                else:
                    print("No tasks to remove!")
            elif choice == 4:
                print("Goodbye!")
                return True  # Signal to break the loop
            else:
                print('Invalid choice')
            return False

        # Display menu and get choice
        menu()
        try:
            choice = int(input('Enter choice: '))
            if choose_option(choice):
                break
        except ValueError:
            print("Please enter a valid number")


if __name__ == '__main__':
    main()

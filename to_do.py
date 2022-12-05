
# Real world example of a to_do list.

from functions import getTasks, writeTask

print("Welcome to your TO DO LIST\n") 
count = 0

while True:
    start = input("""\n Main menu\n
Add - Add task (i.e add clean shoes)
Show- Show to do list
Edit- Edit task (i.e edit 4)
Complete- Mark task as complete (i.e complete 4)
Exit- Exit\n""").lower().strip(" ")
    
        
    if start.startswith("add"):
        to_do = start[4:]

        to_do_list = getTasks()

        to_do_list.append(to_do + "\n")

        with open("tasks.txt", "w") as file:
            file.writelines(task for task in to_do_list)

    elif "show" in start:

        to_do_list = getTasks()
        
        to_do_list = [task.replace("\n", "") for task in to_do_list]

        for i, task in enumerate(to_do_list):
            task = task.title()
            print(f"{i+1}. {task}")
    
    elif start.startswith("edit"):
        try:
            to_do_list = getTasks()

            to_do_list = [task.replace("\n", "") for task in to_do_list]
            print("To Do List\n")
            for i, task in enumerate(to_do_list):
                task = task.title() 
                print(f"{i+1}. {task}")
            task_no = int(start[5:])
            task_no = task_no -1
            edited_task = input("Add new Task Description: ")
            to_do_list.__setitem__(task_no, edited_task)
            print(f"Task Number {task_no} has been edited.")
            writeTask("tasks.txt", to_do_list)
        except IndexError: 
            print("Please select the number of the task you wish to edit. i.e edit 2")
            continue
    
    elif "complete" in start:
        try:
            to_do_list = getTasks()
            

            to_do_list = [task.replace("\n", "") for task in to_do_list]
            
            for i, task in enumerate(to_do_list):
                task = task.title()
                print(f"{i+1}. {task}")
            task_index = int(start[9:])
            task_no = task_index -1
            to_do_list.pop(task_no)
            print(f"Task {task_index} has been Marked as Complete.")
            writeTask("tasks.txt", to_do_list)
        except ValueError:
            print("Please select the number of the task you wish to mark as complete. i.e complete 2")
            continue

    elif "exit" in start:
        print("Goodbye!")
        break

    else:
        print("Invalid input, please try again")

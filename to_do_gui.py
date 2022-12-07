import functions
import PySimpleGUI as gui


label = gui.Text("Please enter a task...")
input = gui.InputText(tooltip="i.e Clean the car", key="Task")

add_button = gui.Button("Add")
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")

task_list = gui.Listbox(values=functions.getTasks(),
 key="Task List", enable_events=True, size=[45, 10])

# Layout expects a list, in this case object instances. 
window = gui.Window("To Do List",
                    layout=[[label], [input, add_button],[task_list, edit_button]],
                    font=("any", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values["Task List"])
    match event:
        case "Add":
            tasks = functions.getTasks()
            to_do_list = values["Task"] + "\n"
            tasks.append(to_do_list)
            functions.writeTask(tasks)

            # Update list box in real time. 
            window["Task List"].update(values=tasks)

        case "Edit":
            task_edit = values["Task List"][0]
            new_task = values["Task"]

            to_do_list = functions.getTasks()
            index = to_do_list.index(task_edit)
            to_do_list[index] = new_task
            functions.writeTask(to_do_list)

            # Update list box in real time. 
            window["Task List"].update(values=to_do_list)

        case "Task List":
            # Update input box in real time. 
            window["Task"].update(value=values["Task List"][0])
            

        # WIN_CLOSED exits program without error. 
        case gui.WIN_CLOSED:
            break




window.close()






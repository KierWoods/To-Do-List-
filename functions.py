def getTasks(file = "tasks.txt"):
    with open(file, "r") as file:
        to_do_list = file.readlines()
    return to_do_list


def writeTask(file, to_do_list):
    with open ("tasks.txt", "w") as file:
        file.writelines(task + "\n" for task in to_do_list)


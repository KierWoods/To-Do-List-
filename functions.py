
import datetime

def getTasks(file = "tasks.txt"):
    with open(file, "r") as file:
        to_do_list = file.readlines()
    return to_do_list


def appendTask(to_do_list, file ="tasks.txt"):
    with open (file, "a") as file:
        file.writelines(to_do_list)

def writeTask(to_do_list, file ="tasks.txt"):
    with open (file, "w") as file:
        file.writelines(to_do_list)
    
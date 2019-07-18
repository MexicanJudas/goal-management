from challenges import challenge_path
from habits import habit_path
from projects import project_path
from goals import goal_path
from file_handle import *


path_dict = {"CHALLENGE": challenge_path,
            "HABIT": habit_path,
            "GOAL" : goal_path,
            "PROJECT": project_path}

def link_project(project_name, other_name, type):
    project_location = path_dict["PROJECT"]
    other_location = path_dict[type]
    project_exist = dict_in_file(project_location, "PROJECTS", project_name)
    other_exist = dict_in_file(other_location, type, other_name)
    if(project_exist and other_exist):
        project_file = load_file(project_location)
        other_file = dict_in_file(other_location, type, other_name)
        if other_file == False or project_file == None:
            print("One of the files doesn't exist")
        else:
            project_file["PROJECTS"][project_name]["LINKS"][type].append(other_name)
            save_file(project_location, project_file)


    else:
        print("Some of this doesn't add up...")


def link_handler(type):
    if type == "PROJECT":
        path = path_dict[type]
        name = input("Enter the name of your project\nQ:Back")
        if name == "Q":
            return()
        if(dict_in_file(path, type, name)):
            receive_input = True
            while receive_input is True:
                choice = input("Enter the type of object to be linked!\nQ:Back\n").upper()
                if choice == "Q":
                    return()
                if choice in path_dict.keys():
                    other_path = path_dict[choice]
                    while receive_input is True:
                        other_name = input("Enter the name of this object!\nQ:Back")
                        if other_name == "Q":
                            return()
                        if(dict_in_file(other_path, choice, other_name)):
                            link_project(name, other_name, choice)
                            return()
                        else:
                            print("This is not a field try again!")
                else:
                    print("This is not a type!")
        else:
            print("This project doesn't exist!")
    else:
        #Other case



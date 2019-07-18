global project_path
goal_path = 'goals.json'
import json
from file_handle import *

project_path = 'projects.json'
def project_handler():
    option = int(input("1: Add project\n2:List projects\n3:Edit Project\n4:Remove Project\n5:Link Project\n6:Back"))
    if option == 1:
        declare_project()
    if option == 2:
        list_all(project_path, "PROJECTS")
    if option == 3:
        edit_project()
    if option == 4:
        remove_project()
    if option == 5:
        link_handler("PROJECT")
    if option == 6:
        return()

def remove_project():
    print(does_file_exist(project_path))
    list_all(project_path, "PROJECTS")
    if does_file_exist(project_path):
        proj_delete = input("Enter the name of the project you would like to delete")
        with open(project_path) as project_file:
            projects = json.load(project_file)
        try:
            del projects["PROJECTS"][proj_delete]
        except KeyError:
            pass
        with open(project_path, 'w') as project_file:
            json.dump(projects, project_file)
    else:
        print("This file does not exist.")



def declare_project():
    print(does_file_exist(project_path))
    print("You've declared your project")
    project = input("Enter your project name")
    project_purpose = input("What's the purpose of this project?")
    project_principles = input("What're your principles of this project?")
    project_outcome = input("If you  suspend your disbelief, what's the best possible result of this?")
    project_brainstorm = input("Brainstorm this one, full quantity, mindmapping with pen and paper.")
    project_organise = input("What're the steps or milestones you can identify for this project, how do you know you're meeting them?")
    project_actions = input("What're the next actions for this project?")

    current_project = {"PROJECTS" : {
                            project : {
                            "PURPOSE": project_purpose,
                            "PRINCIPLES": project_principles,
                            "OUTCOME": project_outcome,
                            "BRAINSTORM": project_brainstorm,
                            "ORGANISATION": project_organise,
                            "ACTIONS": project_actions,
                            "LINKS": { "HABITS" : [], "GOALS" : [], "CHALLENGES" : []
                            }
                            }
                        }}
    if does_file_exist(project_path):
        try:
            with open(project_path) as project_file:
                projects = json.load(project_file)
            with open(project_path, 'w') as project_file:
                projects["PROJECTS"][project] = current_project["PROJECTS"][project]
                json.dump(projects, project_file)
        except:
            with open(project_path, 'w+') as project_file:
                json.dump(current_project, project_file)
    else:
        with open(project_path, 'w+') as project_file:
            json.dump(current_project, project_file)



def edit_project():
    project_edit = True
    if does_file_exist(project_path):
        list_all(project_path, "PROJECTS")
        while project_edit == True:
            project_name = input("Enter a project name to edit the field of!")
            if dict_in_file(project_path, "PROJCETS", project_name):
                project_type = input("Enter which field you would like to change \n\
                                     PURPOSE: Purpose\n\
                                     PRINCIPLES: Principles\n\
                                     OUTCOME: Outcome\n\
                                     BRAINSTORM: Brainstorm\n\
                                     ORGANISATION: Organisation\n\
                                     ACTIONS: Actions\n\
                                     LINKS: Links\n\
                                     EXIT: Exit\n")
                project_type = project_type.upper()
                input_check = field_in_dict(project_path, "PROJECTS", project_name, project_type)
                if input_check == True:
                    result = return_field(project_path, "PROJECTS", project_name, project_type)
                    project_change = input("Please enter what you would like to change %s to!" % result)
                    field_change(project_path, "PROJECTS", project_name, project_type, project_change)
                    print("%s changed to %s", result, project_change)
                    project_edit = False

                else:
                    if project_type == "EXIT":
                        project_edit = False
                        break
                    print("This is not a field")

    else:
        print("You have not set projects!")

# FINISH HERE

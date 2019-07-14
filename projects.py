import json
from file_handle import *

project_path = 'projects.json'
def project_handler():
    option = int(input("1: Add project\n2:List projects\n3:Remove project\n4:Back"))
    if option == 1:
        declare_project()
    if option == 2:
        list_projects()
    if option == 3:
        remove_project()
    if option == 4:
        return()

def remove_project():
    list_projects()
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
                            "ACTIONS": project_actions
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
def list_projects():
    with open(project_path) as project_file:
        output = json.load(project_file)
        print(json.dumps(output))

def edit_project():
    project_edit = True
    if does_file_exist(project_path):
        list_projects()

        while project_edit == True:
            project_name = input("Enter a project name to edit the field of!")





def validate_project(project_name, project_field):
    with open(project_path) as project_file:
        projects = json.load(project_path)
    return(project_field in projects["PROJECTS"][project_name])
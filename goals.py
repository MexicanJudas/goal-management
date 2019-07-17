import json
from file_handle import *

goal_path = 'goals.json'
def goal_handler():
    option = int(input("1: Add goal\n2: List goals\n3: Remove goal\n4: Back"))
    if option == 1:
        declare_goal()
    if option == 2:
        list_all(goal_path, "PROJECTS")
    if option == 3:
        edit_goal()
    if option == 4:
        return ()

def remove_goal():

    list_all(goal_path, "PROJECTS")
    if does_file_exist(goal_path):
        goal_delete = input("Enter the name of the habit you would like to delete")
        with open(goal_path) as goal_file:
            goals = json.load(goal_file)
        try:
            del goals["GOALS"][goal_path]
        except KeyError:
            pass
        with open(goal_path, 'w') as goal_file:
            json.dump(goals, goal_file)
    else:
        print("This file does not exist.")

def declare_goal():
    print(does_file_exist(goal_path))
    print("You've declared a goal, this consists of challenges and projects and habits")
    goal = input("What is your goal?")
    goal_purpose = input("What is the point of this habit?")
    goal_habits = input("What habits does this conist of?")
    goal_projects = input("What projects does this consist of?")
    goal_challenge = input("What challenges does this consist of?")
    #Handle if this don't exist.

    current_goal = {"GOALS": {
                        goal : {
                         "PURPOSE":goal_purpose,
                         "HABITS":goal_habits,
                         "PROJECTS":goal_projects,
                         "CHALLENGES":goal_challenge
                         }
                    }
    }



    if does_file_exist(goal_path):
        try:
            with open(goal_path) as goal_file:
                    goals = json.load(goal_file)
            with open (goal_path, 'w') as goal_file:
                goals["GOALS"][goal] = current_goal["GOALS"][goal]
                json.dump(goals, goal_file)
        except:
            with open(goal_path, 'w+') as goal_file:
                json.dump(current_goal, goal_file)
    else:
        with open(goal_path, 'w+') as goal_file:
            json.dump(current_goal, goal_file)

def edit_goal():
    goal_edit = True
    if does_file_exist(goal_path):
        list_all(goal_path, "PROJECTS")

        while goal_edit == True:
            goal_name = input("Enter goal name to edit field of")
            if dict_in_file(goal_path, "GOALS", goal_name):
                    goal_type = input("Enter which field you would like to change\n\
                                    PURPOSE: Purpose\n\
                                    HABITS: Habits\n\
                                    PROJECTS: Projects\n\
                                    CHALLENGES: Challenges\n\
                                    EXIT: Exits\n")
                    goal_type = goal_type.upper()
                    input_check = field_in_dict(goal_path, "GOALS", goal_name, goal_type)

                    if input_check == True:
                        result = return_field(goal_path, "GOALS", goal_name, goal_type)
                        goal_change = input("Please enter what you would like to change %s to!" % result)
                        field_change(goal_path, "GOALS", goal_name, goal_type, goal_change)
                        print("%s changed to %s" % result, goal_change)
                        goal_edit = False

                    else:
                        if goal_type == "EXIT":
                            goal_edit = False
                            break
                        print("This is not a field")

    else:
        print("You have not set any goals")





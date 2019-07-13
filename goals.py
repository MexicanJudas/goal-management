import json
from file_handle import *

goal_path = 'goals.json'
def goal_handler():
    option = int(input("1: Add goal\n2: List goals\n3: Remove goal\n4: Back"))
    if option == 1:
        declare_goal()
    if option == 2:
        list_goals()
    if option == 3:
        remove_goal()
    if option == 4:
        return ()

def remove_goal():

    list_goals()
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
                         "Purpose":goal_purpose,
                         "habits":goal_habits,
                         "Projects":goal_projects,
                         "Challenges":goal_challenge
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
def list_goals():
    with open(goal_path) as goal_file:
        output = json.load(goal_file)
        print(json.dumps(output))
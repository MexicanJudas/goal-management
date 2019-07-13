import json
from file_handle import *
habit_path = 'habits.json'

def habit_handler():
    habit_handler = True
    while habit_handler == True:
        option = int(input("1: Add habit\n2: List habits\n3:Remove habit\n4: Back"))
        if option == 1:
            declare_habit()
        if option == 2:
            list_habits()
        if option == 3:
            edit_habit()
        if option == 4:
            return()

def remove_habit():

    list_habits()
    if does_file_exist(habit_path):
        habit_delete = input("Enter the name of the habit you would like to delete")
        with open(habit_path) as habit_file:
            habits = json.load(habit_file)
        try:
            del habits["HABITS"][habit_delete]
        except KeyError:
            pass
        with open(habit_path, 'w') as habit_file:
            json.dump(habits, habit_file)
    else:
        print("This file does not exist.")







def declare_habit():

    print("You've declared a habit, what needs to be done, what needs to be maintained, how do you remind yourself and how do you fight for this? In the trenches.")
    habit = input("Enter the name of this habit")
    habit_type = input("Are you trying to stop or build this habit?")
    habit_purpose = input("Why do you want this habit?")
    habit_principle = input("If you were fair to yourself, how far could you go?")
    habit_achieve = input("How are you going to achieve this?")
    habit_primer = input("What can you do to remind yourself of this habit?")
    habit_record = input("What advice do you have for yourself to stay on track for the desired outcome?")

    current_habit = {"HABITS":{
                    habit : {
                    "Type":habit_type,
                    "Purpose":habit_purpose,
                    "Princple":habit_principle,
                    "Plan":habit_achieve,
                    "Primer":habit_primer,
                    "Path":habit_record
    }}}

    if does_file_exist(habit_path):
        try:
            with open(habit_path) as habit_file:
                    habits = json.load(habit_file)
            with open (habit_path, 'w') as habit_file:
                habits["HABITS"][habit] = current_habit["HABITS"][habit]
                json.dump(habits, habit_file)
        except:
            with open(habit_path, 'w+') as habit_file:
                json.dump(current_habit, habit_file)
    else:
        with open(habit_path, 'w+') as habit_file:
            json.dump(current_habit, habit_file)
def list_habits():
    with open(habit_path) as habit_file:
        output = json.load(habit_file)
        print(json.dumps(output))

def edit_habit():
    if does_file_exist(habit_path):
        list_habits()

        while True:
            habit_name = input("Enter habit name to edit field of")
            if habit_in_file(habit_name):
                habit_type = input("Enter which field you would like to change\n \
                                TYPE: Type\n \
                                PURPOSE: Purpose\n \
                                PRINCIPLE: Principle\n \
                                PLAN: Plan\n \
                                PRIMER: Primer\n \
                                PATH: Path\n")
                habit_type = habit_type.upper()
                input_check = validate_habit(habit_name, habit_type)

                if input_check == True:
                    result = return_field(habit_path, "HABITS", habit_name, habit_type)
                    habit_change = input("Please enter what you would like to change %s to!" % result)
                    field_change(habit_path, "HABITS", habit_name, habit_type)
                    print("%s changed to" % result, habit_path, "HABITS", habit_name, habit_type)


                else:
                    print("This is not an input field.")
    else:
        print("You have not set habits!")

def validate_habit(habit_name, habit_field):
    with open(habit_path) as habit_file:
        habits = json.load(habit_file)
    return (habit_field in habits["HABITS"][habit_name])


def habit_in_file(habit_name):
    with open(habit_path) as habit_file:
        habits = json.load(habit_file)
    return(habit_name in habits["HABITS"])



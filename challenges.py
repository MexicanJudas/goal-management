import json
from file_handle import *

challenge_path = 'challenges.json'
def challenge_handler():
    option = int(input("1: Add challenge\n2: List challenges\n3: Remove challenge\n4: Back"))
    if option == 1:
        declare_challenge()
    if option == 2:
        list_challenges()
    if option == 3:
        edit_challenge()
    if option == 4:
        return ()

def remove_challenge():
    list_challenges()
    if does_file_exist(challenge_path):
        challenge_delete = input("Enter the name of the challenge you would like to delete")
        with open(challenge_path) as challenge_file:
            challenges = json.load(challenge_file)
        try:
            del challenges["CHALLENGES"][challenge_delete]
        except KeyError:
            pass
        with open(challenge_path, 'w') as challenge_file:
            json.dump(challenges, challenge_file)
    else:
        print("This file does not exist.")
def declare_challenge():
    print(does_file_exist(challenge_path))
    print("You've declared a challenge")
    challenge = input("What is this challenge?")
    challenge_time = input("What is the time frame for this challenge?")
    challenge_purpose = input("Why, what do you need to achieve this challenge?")
    challenge_achieveable = input("Is this challenge currently possible? Y/N")

    #Hande data inputs

    current_challenge = {"CHALLENGES" : {
                        challenge : {
                         "Frame": challenge_time,
                         "Purpose":challenge_purpose,
                         "Achievable?":challenge_achieveable
                         }
    }
    }
    if does_file_exist(challenge_path):
        try:
            with open(challenge_path) as challenge_file:
                goals = json.load(challenge_file)
            with open(challenge_path, 'w') as challenge_file:
                goals["CHALLENGES"][challenge] = current_challenge["CHALLENGES"][challenge]
                json.dump(goals, challenge_file)
        except:
            with open(challenge_path, 'w+') as challenge_file:
                json.dump(current_challenge, challenge_file)
    else:
        with open(challenge_path, 'w+') as challenge_file:
            json.dump(current_challenge, challenge_file)

def edit_challenge():
    challenge_edit = True
    if does_file_exist(challenge_path):
        list_challenges()
    while challenge_edit == True:
        challenge_name = input("Enter the name of the goal you would like to edit")
        if dict_in_file(challenge_path, "CHALLENGES", challenge_name):
            challenge_type = input("Enter which field you would like to change \n\
                                   FRAME: Frame\n\
                                   PURPOSE: Purpose\n\
                                   ACHIEVEABLE: Achieveable\n")
            challenge_type = challenge_type.upper()
            input_check = field_in_dict(challenge_path,"CHALLENGES",challenge_name, challenge_type)
            if input_check == True:
                result = return_field(challenge_path, "CHALLENGES", challenge_name, challenge_type)
                challenge_change = input("Please enter what you would like to change %s to!" % result)
                field_change(challenge_path, "CHALLENGES", challenge_name, challenge_type, challenge_change)
                print("%s changed to %s" % result, challenge_change)
                challenge_edit = False




    #Handle if this doesn't or does exist



def list_challenges():
    with open(challenge_path) as challenge_file:
        output = json.load(challenge_file)
        print(json.dumps(output))

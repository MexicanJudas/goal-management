

from projects import *
from challenges import *
from goals import *
from habits import *
from file_handle import *


#Python file for each case.

def main():
    project_exit = False
    while (project_exit == False):

        try:
            choice = int(input("Pick your poison \n1: Project\n2: Goal\n3: Challenge\n4: Habit\n5: Exit"))
            if (choice > 5) or (choice < 0):
                raise
            else:
                project_exit = True
        except:
            print("Only give me integers between 0 and 4!")


    if choice == 1:
        project_handler()
    if choice == 2:
        goal_handler()
    if choice == 3:
        challenge_handler()
    if choice == 4:
        habit_handler()
    if choice == 5:
        exit_program = True






if __name__ == "__main__":
    exit_program = False
    while exit_program is False:
        main()
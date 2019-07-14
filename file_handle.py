import os.path
from os import path
import json

def does_file_exist(path):
    test_path = "/"+path
    return(os.path.isfile(path))

def return_field(file_path, type, name, field):
    with open(file_path) as input_file:
        input = json.load(input_file)
        input_file.close()
    return(input[type][name][field])

def field_change(file_path, type, name, field, change_to):
    with open(file_path) as input_file:
        file_read = json.load(input_file)
        input_file.close()
    file_read[type][name][field] = change_to
    with open(file_path, 'w') as output_file:
        json.dump(file_read, output_file)

def dict_in_file(file_path, file_type, dict_name):
    with open(file_path) as dict_file:
        file_struct = json.load(dict_file)
    return(dict_name in file_struct[file_type])
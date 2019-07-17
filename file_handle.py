import os.path
import json

def does_file_exist(path):
    try:
        with open(path) as test_file:
            output = json.load(test_file);
    except:
        return(False)
    dict_list = ["HABITS", "PROJECTS", "GOALS", "CHALLENGES"]
    for item in dict_list:
        if item in output:
            return(True)
    return(False)

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

def field_in_dict(file_path, file_type, dict_name, dict_field):
    if dict_in_file(file_path, file_type, dict_name):
        with open(file_path) as input_file:
            input = json.load(input_file)
            input_file.close()
        if dict_field in input[file_type][dict_name]:
            return True
        else:
            return False
    else:
        return(False)

def list_all(file_name, file_type):
    with open(file_name) as out_file:
        output = json.load(out_file)
        print("Your file is %s" % json.dumps(output))

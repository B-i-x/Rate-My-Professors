import re

INPUT_FILE_PATH = r"C:\Users\alexr\Documents\Projects\RateMyProfessorBot\inputs\initial.txt"

def read_file():

    with open(INPUT_FILE_PATH) as f:
        lines = f.readlines()

        return lines

def parse_file_for_professor_names(file_contents: list):

    s = ''

    for line in file_contents:
        s += line

    #print(s)

    not_r2 = re.findall("Instructor[\r\n]+([^\r\n]+)", s)

    r2 = {}

    testing = {}

    for result in not_r2:
        
        if "To be Announced" == result or "    To be Announced" == result:
            continue
        
        if result not in r2:
            r2[result] = 1

    for value in r2:

        print(value)
    

file_contents = read_file()

parse_file_for_professor_names(file_contents)
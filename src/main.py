import re
import crawler

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

    r3 = {}
    for value in r2:

        prof = ''
        if " " == value[0]:

            prof = re.sub(r" ", "", value, count=4)

            if " " == prof[0]:

                prof = re.sub(r" ", "", prof, count=4)

        prof = prof.replace(",", "")

        if prof == "":
            continue

        if prof not in r3:
            r3[prof] = 1

    rlist = []
    
    for prof in r3:
        rlist.append(prof)

    return rlist

file_contents = read_file()

professor_names = parse_file_for_professor_names(file_contents)

driver = crawler.open_browser()

crawler.close_popup(driver)

for professor in professor_names:
    print(professor)
    if professor == professor_names[0]:
        crawler.get_rating_for_professor(driver, professor, "first")
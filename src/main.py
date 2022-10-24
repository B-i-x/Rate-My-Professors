import re
import crawler
import csv

INPUT_FILE_PATH = r"C:\Users\alexr\Documents\Projects\RateMyProfessorBot\inputs\initial.txt"
OUTPUT_FILE_PATH = r"C:\Users\alexr\Documents\Projects\RateMyProfessorBot\output\geneds_150s.csv"

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

def make_csv_file(data):

    header = ['name', 'rating']

    with open(OUTPUT_FILE_PATH, 'w', encoding='UTF8', newline='') as f:

        writer = csv.writer(f)

        writer.writerow(header)

        writer.writerows(data)


file_contents = read_file()

professor_names = parse_file_for_professor_names(file_contents)

professor_ratings = {}

driver = crawler.open_browser()

crawler.close_popup(driver)

crawler.switch_to_school(driver, "University of Arizona")

for professor in professor_names:
    rating = 'Unknown'

    crawler.lookup_professor(driver, professor)

    if (crawler.is_found(driver, "University of Arizona")):
        rating = crawler.get_rating(driver)

    crawler.clear_input(driver)

    print(f"{professor}'s rating is {rating}")
        
    
    professor_ratings[professor] = rating

sorted_ratings = [[k, v] for k, v in sorted(professor_ratings.items(), key = lambda item: item[1])]

make_csv_file(sorted_ratings)

for r in sorted_ratings:
    print(r)

print(professor_ratings)
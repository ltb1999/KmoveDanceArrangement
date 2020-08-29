## This read information from the members' preference survey and store them into
## instances of class Member
import csv
import re
from class_name import *

def read_member_file(number_of_songs):
    list_of_member = []
    with open("MemberSurvey.csv",'r') as f:
        readCSV = csv.reader(f, delimiter=',')
        next(f)
        for line in readCSV:
            # name is line[2]
            # preference is line[3-8]
            preference = []
            for i in range(4,4+number_of_songs):
                preference.append(line[i])
            # print([line[2],line[3],preference,line[9],True if line[10] =="First time" else False])
            list_of_member.append(Member(line[2],line[3],preference,line[9],True if line[10] =="First time" else False))
    return list_of_member

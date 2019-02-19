import pandas as pd
import sys
from sys import argv
import xlwt

name = argv[1]
gender = argv[2]
age = argv[3]
testscore = argv[4]

list1=[name, gender, age, testscore]

book = xlwt.Workbook(encoding="utf-8")

sheet1 = book.add_sheet("Test Score Sample")

sheet1.write(0, 0, "Name")
sheet1.write(0, 1, "Gender")
sheet1.write(0, 2, "Age")
sheet1.write(0, 3, "Test Score")

sheet1.write(1, 0, name)
sheet1.write(1, 1, gender)
sheet1.write(1, 2, age)
sheet1.write(1, 3, testscore)

book.save("testscore.xls")

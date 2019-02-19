import sys
import locale
import itertools
from decimal import Decimal

locale.setlocale( locale.LC_ALL, '' )


employees = [{"IDNumber" : "001", "Name" :  "Mary", "PayRate"  :  15.00, "HoursWorked"  : 40},
             {"IDNumber" : "002", "Name" :  "John", "PayRate"  :  15.00, "HoursWorked"  : 25},                
             {"IDNumber" : "003", "Name" :  "Bob",  "PayRate"  :  35.00, "HoursWorked"  :  4},                
             {"IDNumber" : "004", "Name" :  "Mel",  "PayRate"  :  43.00, "HoursWorked"  : 62},
             {"IDNumber" : "005", "Name" :  "Jen",  "PayRate"  :  17.00, "HoursWorked"  : 33},
             {"IDNumber" : "006", "Name" :  "Sue",  "PayRate"  :  29.00, "HoursWorked"  : 45},
             {"IDNumber" : "007", "Name" :  "Ken",  "PayRate"  :  40.00, "HoursWorked"  : 36},
             {"IDNumber" : "008", "Name" :  "Dave", "PayRate"  :  20.00, "HoursWorked"  : 17},
             {"IDNumber" : "009", "Name" :  "Beth", "PayRate"  :  37.00, "HoursWorked"  : 37},
             {"IDNumber" : "010", "Name" :  "Ray",  "PayRate"  :  16.50, "HoursWorked"  : 80}
]

for employee in employees:
    ID = employee['IDNumber']
    EmpName = employee['Name']
    hourlyWage = employee['PayRate']
    totalHours = employee['HoursWorked']
    overtimeHours = totalHours - 40
    overtimePay = overtimeHours * 1.5*hourlyWage
    if totalHours <= 40:
        totalWages = hourlyWage*totalHours
        print("ID\tName\tPayRate\t\tHoursWorked\t\tTotalPay")
        print(ID, "\t" + EmpName,"\t" + str(hourlyWage) + "\t\t" + str(totalHours) + "\t\t\t" +  str(totalWages))
    elif overtimeHours > 0:
        overtime = totalHours - 40
        totalWages = hourlyWage*40 + (1.5*hourlyWage)*overtime
        print("ID\tName\tPayRate\t\tHoursWorked\t\tTotalPay\tOvertime Hours\t\tOvertime Pay")
        print(ID, "\t" + EmpName,"\t" + str(hourlyWage) + "\t\t" + str(totalHours) + "\t\t\t" +  str(totalWages)
              + "\t\t" + str(overtimeHours) + "\t\t\t" + str(overtimePay))




                       



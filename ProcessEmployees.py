'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file

infile = open('employee_data.csv', 'r', newline = '')

reader = csv.reader(infile)

fieldnames = next(reader)

#create an empty dictionary

employee_dict = {}

#use a loop to iterate through the csv file
for row in reader:
    emp_id = row[0]
    first_name = row[1]
    last_name = row[2]
    department = row[3]
    title = row[4]
    salary = float(row[5])
    hire = row[6]
    birth = row[7]
    gender = row[8]
    clearance  = row[9]
    #check if the employee fits the search criteria
    if department == 'Marketing' and title == 'CSR':
        print('Manager Name: ', first_name, ' ', last_name, ' Current Salary: ', '$', format(salary, ',.2f'), sep='')

        bonus = salary * .1
        new_salary = salary + bonus
        new_salary = format(new_salary, ',.2f')
        employee_name = first_name + " " + last_name

        employee_dict[employee_name] = new_salary

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout

for employee in employee_dict:
    print(f"Manager Name: {employee} New Salary: ${employee_dict[employee]}")

infile.close()
    

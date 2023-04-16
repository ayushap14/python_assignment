import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state
        
    def __str__(self):
        return f"Name: {self.name}, DOB: {self.dob}, Height: {self.height}, City: {self.city}, State: {self.state}"

# read employee information from the JSON file
with open('employee.json', 'r') as f:
    data = json.load(f)

# create a list of Employee objects
employees = []
for employee_data in data['employees']:
    employee = Employee(employee_data['name'], employee_data['dob'], employee_data['height'], employee_data['city'], employee_data['state'])
    employees.append(employee)

# print the list of Employee objects
for employee in employees:
    print(employee)

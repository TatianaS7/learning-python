# Using Dictionaries to Represent Objects

employeeDirectory = {
    'number': 5,
    'departments': ['HR', 'IT', 'Accounting', 'Sales', 'Administration'],
    'employees':
        [
            {'name': 'Samantha Gardener', 'email': 'samantha@example.com', 'status': 'Full Time', 'department': 'HR'},
            {'name': 'Zeke Mayfield', 'email': 'zeke@example.com', 'status': 'Full Time', 'department': 'IT'},
            {'name': 'Monica Windsor', 'email': 'monica@example.com', 'status': 'Part Time', 'department': 'IT'},
            {'name': 'Luke Combs', 'email': 'luke@example.com', 'status': 'Part Time', 'department': 'Accounting'},
            {'name': 'Erica Lee', 'email': 'erica@example.com', 'status': 'Temporary', 'department': 'Sales'}
        ]
}

# print('Full Time Employees:')

# for employee in employeeDirectory['employees']:
#     if employee['status'] == 'Full Time':
#             print(employee['name'])


knowName = input('Do you know the employee by name?\n')

if knowName.lower() == 'yes':
    givenName = input('Enter their full name below:\n')
    found = False

    for employee in employeeDirectory['employees']:
        if employee['name'] == givenName:
            print(givenName, 'works in the', employee['department'], 'department')
            print('You can reach them at', employee['email'])
            found = True
            break
    if not found:
        print('No employees found with that name')    

elif knowName.lower() == 'no':
    knowDepartment = input('Do you know which department the employee works in?\n')

    if knowDepartment.lower() == 'yes':
        print('These are our departments:')
        for department in employeeDirectory['departments']:
            print('-', department)
        givenDepartment = input('Enter their department below:\n')

        found = False

        print('These are the current employees in', givenDepartment)
        for employee in employeeDirectory['employees']:
            if employee['department'] == givenDepartment:
                print('-', employee['name'], '|', employee['email'])
                found = True
    elif knowDepartment.lower() == 'no':
        print('Sorry, there is not enough information to find the employee.')
                


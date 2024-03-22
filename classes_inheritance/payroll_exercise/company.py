from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def addEmployee(self, new_employee):
        self.employees.append(new_employee)

    def getEmployees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname, i.lname)
    
    def payEmployee(self):
        print('Payroll:')
        for i in self.employees:
          print('Employee:', i.fname, i.lname)
          print(f'Weekly Pay: ${i.calculatePaycheck()}')
          print('---------------------')



def main():
    my_company = Company()

    employee1 = SalaryEmployee('Emma', 'Lacy', 100000)
    my_company.addEmployee(employee1)
    employee2 = HourlyEmployee('Arnold', 'Makers', 28, 35)
    my_company.addEmployee(employee2)
    employee3 = HourlyEmployee('Marie', 'Summerlin', 16, 25)
    my_company.addEmployee(employee3)
    employee4 = CommissionEmployee('Latisha', 'Green', 12, 32, 7, 30)
    my_company.addEmployee(employee4)
    
    # my_company.getEmployees()
    my_company.payEmployee()

main()
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    def calculatePaycheck(self):
        return round(self.salary/52, 2)


class HourlyEmployee(Employee):
    def __init__(self, fname, lname, rate, hours):
        super().__init__(fname, lname)
        self.rate = rate
        self.hours = hours

    def calculatePaycheck(self):
        return self.hours * self.rate
    

class CommissionEmployee(HourlyEmployee):
    def __init__(self, fname, lname, rate, hours, salesNum, comRate):
        super().__init__(fname, lname, rate, hours)
        self.salesNum = salesNum
        self.comRate = comRate

    def calculatePaycheck(self):
        regulary_salary = super().calculatePaycheck() 
        total_commission = self.salesNum * self.comRate
        return regulary_salary + total_commission
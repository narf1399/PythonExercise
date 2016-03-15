class Employee:

    # Class variable
    employeeCount = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employeeCount += 1
        
    def displayCount(self):
        print "There are %d employee(s)." % Employee.employeeCount
        
    def displayEmployee(self):
        print "I'm", self.name, "and make", self.salary
        
    @staticmethod
    def displayCountStatic():
        print "There are %d employee(s)." % Employee.employeeCount
        
        

myEmployee = Employee("Tim", 1000000)
myEmployee.displayCount()
myEmployee.displayEmployee()
Employee.displayCountStatic()
    
    
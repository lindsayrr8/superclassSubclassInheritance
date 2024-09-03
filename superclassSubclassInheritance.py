
# This program creates an Employee class with two subclasses,
# --- Manager & Executive;
# -
# --- Manager inherits from Employee;
# -
# --- Executive inherits from Manager;
# -
# Prints name, department, and salary;
# Tests the classes.




# Creates Employee class.
class Employee:
    
    def __init__(self, name, salary): # Employee attributes.
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee: {self.name}'s  salary is ${self.salary}"


# Creates Manager class.
class Manager(Employee):
    
    def __init__(self, name, salary, department): # Inheritable Employee attributes.
        super().__init__(name,salary)
        self.department = department # Manager only attribute.

    def __str__(self):
        return f"Manager: {self.name}'s salary is ${self.salary}, Department: {self.department}"


# Creates Executive class.
class Executive(Manager):
    
    def __str__(self): # Inherits Manager attributes.
        return f"Executive: {self.name}'s salary is: ${self.salary}, Department: {self.department}"




# Tests the classes.
def testClasses():
    
    employee = Employee("John", 55000)
    manager = Manager("Jane", 64000, "IT")
    executive = Executive("Bob", 82000, "Finance")

    print(employee)
    print(manager)
    print(executive)




testClasses()

    

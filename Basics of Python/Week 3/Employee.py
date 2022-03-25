from Person import Person

class Employee(Person):
    def __init__(self, name, surname, phone, email, department, salary):
        super().__init__(name, surname, phone, email)
        self.department=department
        self.salary=salary
    
    def display(self):
        super().display()
        print("Department :",self.department)
        print("Salary :",self.salary)
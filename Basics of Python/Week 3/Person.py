class Person:
    def __init__(self, name, surname, phone, email) :
        self.name=name
        self.surname=surname
        self.phone=phone
        self.email=email
    
    def display(self):
        print("Name :",self.name)
        print("Surname :",self.surname)
        print("Phone :",self.phone)
        print("Email :",self.email)
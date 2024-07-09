class Student:
    def __init__(self, name, university):
        self.name = name
        self.university = university
        self.course = 1 

    def get_name(self):
        return self.name
    
    def get_university(self):
        return self.university
    
    def get_year(self):
        return self.course
    
    def study(self):
        if self.course < 6:
            self.course += 1

    
class Employee:
    def __init__(self, name, company):
        self.positions = {1: 'junior', 2: 'middle', 3: 'senior', 4: 'lead'}
        self.name = name
        self.company = company
        self.position = 1
    
    def get_name(self):
        return self.name
    
    def get_company(self):
        return self.company
    
    def work(self):
        if self.position < 4:
            self.position += 1

    def get_position(self):
        return self.positions[self.position]


class Human:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

st_1 = Student("Petr", "MSU")
st_2 = Student("Sonya", "Cambridge")
h = Human("Shrek")
empl_1 = Employee("Ivan", "Yandex")
empl_2 = Employee("Ann", "Gazprom")
people = [st_1, empl_2, st_2, h, empl_1]
for person in people:
    if isinstance(person, Student):
        print(person.university)
    elif isinstance(person, Employee):
        print(person.company)
    else:
        print(person.name)
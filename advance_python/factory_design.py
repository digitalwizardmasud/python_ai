from abc import ABCMeta, abstractstaticmethod

class IPerson():
    def method(self):
        return f"No Method "

class Teacher(IPerson):
    def __init__(self):
        self.name = "Teacher Name"
    
    def method(self):
        return "I am teacher"
        
class Student(IPerson):
    def __init__(self):
        self.name = "Student Name"
    
    
    
class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "teacher":
            return Teacher()
        elif person_type == "student":
            return Student()
        else:
            raise ValueError("Invalid person type")

if __name__ == "__main__":
    choice = input("What type of person you want to create?\n")
    person = PersonFactory.build_person(choice)
    print(person.method())
class Person:
    def __init__(self, name, age, gender):
        self.__name=name
        self.__age= age
        self.__gender = gender
    
    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self, value):
        if value == 'masud':
            self.__name = "Masud (admin)"
        else:
            self.__name = value
    
    @staticmethod
    def mymethod():
        print("This is a static method")

p = Person("Masud", 20, "male")
p.Name = "masud"

print(p.Name)
p.mymethod()
Person.mymethod()
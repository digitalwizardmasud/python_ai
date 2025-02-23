

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __del__(self):
#         print("Object is being deconstructed")

# p1 = Person("masud", 10)
# del p1

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"X: {self.x} and Y: {self.y}"
    def __call__(self):
        print("Hello object called") 
    def __del__(self):
        print("Object is being deconstructed")
        
v1 = Vector(1, 2)
v2 = Vector(10, 20)
v3 = v1 + v2 # __add__
print(v3) # __repr__
v3() # __call__
del v1 # __del__




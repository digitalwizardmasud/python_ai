class Vehicle:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model
	# def move(self):
	# 	return "move"

class Car(Vehicle):
	def move(self):
		return "Drive"

class Plane(Vehicle):
    def move(self):
        return "Fly"



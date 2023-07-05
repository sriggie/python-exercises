class Car:
    def __init__(self, color, model, no_of_doors, no_of_wheels):
        self.color = color
        self.model = model
        self.no_of_doors = no_of_doors
        self.no_of_wheels = no_of_wheels

    def display_wheels(self):
        return self.no_of_wheels

    def display_model(self):
        return self.model

    def display_color(self):
        return self.color

    def display_doors(self):
        return self.no_of_doors


# inheritance
class Bus(Car):
    def __init__(self, color, model, no_of_doors, no_of_wheels, name):
        Car.__init__(self, color, model, no_of_doors, no_of_wheels)
        self.name = name


demio = Car("White", "Mazda", 4, 4)

scania = Bus("Silver", "Scania", 2, 8, "Garissa Coach")
print(scania.no_of_doors)

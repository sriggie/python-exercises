class Human:
    # properties/variables
    name = "Dennis"
    height = 178
    weight = 78
    complexion = "brown"
    eyes_color = "black"

    # methods/actions/behaviors
    def walk(self):
        print(f"{self.name} is Walking...")

    def run(self, name):
        print(f"{name} is Running...")

    def eat(self, name):
        print(f"{name} is Eating...")


dennis = Human() # instantiation
dennis.name = "John Doe"

dennis.walk()
dennis.name = "John Doe"
class Car:
    # Constructor to initialize the car object with make, model, and year
    def __init__(self, make, model, year):
        self.make = make    # Attribute for the car's make (e.g., Toyota)
        self.model = model  # Attribute for the car's model (e.g., Camry)
        self.year = year    # Attribute for the car's production year (e.g., 2020)

    # Method to display information about the car
    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}")

    # Method to simulate driving the car
    def drive(self):
        print(f"The {self.year} {self.make} {self.model} is now driving!")
    
    # Method to simulate stopping the car
    def stop(self):
        print(f"The {self.year} {self.make}  {self.model} has stopped.")

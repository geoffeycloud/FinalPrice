class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "Driving"

class Plane(Vehicle):
    def move(self):
        return "Flying"

class Boat(Vehicle):
    def move(self):
        return "Sailing"

# Function to demonstrate polymorphism
def vehicle_move(vehicle):
    print(vehicle.move())

# Example usage:
if __name__ == "__main__":
    car = Car()
    plane = Plane()
    boat = Boat()

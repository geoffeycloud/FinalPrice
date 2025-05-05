class Smartphone:
    def __init__(self, brand, model, price, battery_life):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery_life = battery_life

    def is_battery_low(self):
        return self.battery_life < 20

    def display_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}, Battery Life: {self.battery_life}%"

class FlagshipSmartphone(Smartphone):
    def __init__(self, brand, model, price, battery_life, camera_quality, processing_power):
        super().__init__(brand, model, price, battery_life)
        self.camera_quality = camera_quality
        self.processing_power = processing_power

    def display_details(self):
        base_details = super().display_details()
        return f"{base_details}, Camera Quality: {self.camera_quality}, Processing Power: {self.processing_power}"

# Example usage:
if __name__ == "__main__":
    smartphone = Smartphone("Samsung", "Galaxy A50", 350, 85)
    print(smartphone.display_details())
    print("Is battery low?", smartphone.is_battery_low())

    flagship = FlagshipSmartphone("Apple", "iPhone 14 Pro", 1099, 90, "48MP", "A16 Bionic")
    print(flagship.display_details())
    print("Is battery low?", flagship.is_battery_low())
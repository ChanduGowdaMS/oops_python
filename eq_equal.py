class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __eq__(self, other):
        
        return self.brand == other.brand and self.model == other.model
mobile1 = Mobile("Apple", "iPhone 14", 100999)
mobile2 = Mobile("Apple", "iPhone 14", 100999)
mobile3 = Mobile("Samsung", "Galaxy S23", 100899)
print(mobile1==mobile2)
print(mobile1==mobile3)
print(mobile2==mobile3)
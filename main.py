class Shoe:
    def __init__(self, brand, model, size, price):
        self.brand = brand
        self.model = model
        self.size = size
        self.price = price

    def display(self):
        return f"{self.brand} {self.model} Size: {self.size} Price: ฿{self.price}"


class TennisShoe(Shoe):
    def __init__(self, brand, model, size, price, court):
        super().__init__(brand, model, size, price)
        self.court = court

    def display(self):
        return f"{self.brand} {self.model} Size: {self.size} Court: {self.court} Price: ฿{self.price}"


shoe = Shoe("Nike", "Air Max", 42, 3200)
print(shoe.display())

tennis_shoe = TennisShoe("Adidas", "CourtJam Bounce", 42, 4500, "Clay")
print(tennis_shoe.display())

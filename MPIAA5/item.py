class Item:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.price_cooficient = self.weight / self.price
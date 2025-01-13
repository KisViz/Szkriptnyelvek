# Nev: Tóth-Vizhuzó Albert Pál
# Neptun: G9V7JU
# h: h378775

class Product():
    def __init__(self, name: str, price, weight = 1):
        self.name = name
        self.price = price
        self.weight = weight

    def apply_discount(self, percentage):
        return self.price * (1 - percentage / 100)

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, Weight: {self.weight}kg"

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price and self.weight == other.weight
        else:
            return False

    def __iadd__(self, other):
        if isinstance(other, Product):
            self.weight = self.weight + other.weight
            self.price = self.price if self.price > other.price else other.price
            return self
        return self

class FragileProduct(Product):
    def __init__(self, name: str, price, weight = 1, _fragility_level = 0):
        super().__init__(name, price, weight)
        self._fragility_level = _fragility_level

    @property
    def fragility_level(self):
        return self._fragility_level

    @fragility_level.setter
    def fragility_level(self, level):
        self._fragility_level = min(5,max(1,level))

    def apply_discount(self, percentage):
        return self.price * (1 - percentage / 100) if percentage <= 10 else self.price * 0.9

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, Weight: {self.weight}kg, Fragility Level: {self._fragility_level}"

class Order():
    def __init__(self):
        self.products = []

    def calculate_total(self):
        szaml = 0
        suly = 0
        for elem in self.products:
            szaml += elem.price
            suly += elem.weight

            if isinstance(elem, FragileProduct):
                szaml += 5

        return szaml + (suly / 2)

    def add_product(self, product: Product):
        if self.calculate_total() <= 1400:
            self.products.append(product)

    def view_order(self):
        if len(self.products) > 0:
            return "; ".join(product.__str__() for product in self.products)

        return "Empty order."
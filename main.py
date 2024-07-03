class Checkout:
    def __init__(self, rules):
        self.rules = rules
        self.items = {}

    def total(self):
        total = 0
        for item, quantity in self.items.items():
            unitPrice = self.rules.get(item)[0]
            total += quantity * unitPrice
        return total


    def scan(self, item):

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1
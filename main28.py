class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, table_number):
        self.table_number = table_number
        self.items = []

    def add_item(self, item, quantity=1):
        for _ in range(quantity):
            self.items.append(item)

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

if __name__ == "__main__":
    menu = [
        MenuItem("Pizza", 10),
        MenuItem("Burger", 8),
        MenuItem("Salad", 6),
        MenuItem("Pasta", 12)
    ]

    order1 = Order(1)
    order1.add_item(menu[0])
    order1.add_item(menu[2])
    order1.add_item(menu[1], quantity=2)

    print(f"Order for table {order1.table_number}:")
    for item in order1.items:
        print(f"- {item.name}: ${item.price}")

    print(f"Total: ${order1.calculate_total()}")

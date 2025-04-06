class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity=1):
        if price < 0 or quantity <= 0:
            raise ValueError("Price and quantity must be positive.")
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return
        raise ValueError("Item not found in the cart.")

    def get_total_price(self):
        return sum(item["price"] * item["quantity"] for item in self.items)

    def clear_cart(self):
        self.items = []

    def get_items(self):
        return self.items


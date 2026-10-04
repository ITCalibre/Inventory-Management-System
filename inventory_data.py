import json
import os

class Product:
    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = float(price)
        self.quantity = int(quantity)

    def to_dict(self):
        """Converts object data into a dictionary for JSON storage."""
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "quantity": self.quantity
        }

class InventoryManager:
    def __init__(self, filename="inventory.json"):
        self.filename = filename
        self.products = {}
        self.load_inventory()

    def load_inventory(self):
        """Loads inventory data from the JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    data = json.load(file)
                    for item in data.values():
                        self.products[item['product_id']] = Product(**item)
            except json.JSONDecodeError:
                print("⚠️ Error reading storage file. Starting with an empty inventory.")
        else:
            self.products = {}

    def save_inventory(self):
        """Saves current inventory data back to the JSON file."""
        with open(self.filename, 'w') as file:
            json_data = {pid: prod.to_dict() for pid, prod in self.products.items()}
            json.dump(json_data, file, indent=4)

    def add_product(self, product_id, name, category, price, quantity):
        """Creates a new product record."""
        if product_id in self.products:
            print(f"❌ Error: Product ID '{product_id}' already exists!")
            return False
        
        self.products[product_id] = Product(product_id, name, category, price, quantity)
        self.save_inventory()
        print(f"✅ Product '{name}' added successfully!")
        return True

    def view_all_products(self):
        """Displays all products in a structured layout."""
        if not self.products:
            print("\n📭 The inventory is currently empty.")
            return

        print("\n" + "="*70)
        print(f"{'ID':<10} {'Name':<20} {'Category':<15} {'Price ($)':<12} {'Quantity':<10}")
        print("="*70)
        for prod in self.products.values():
            print(f"{prod.product_id:<10} {prod.name:<20} {prod.category:<15} {prod.price:<12.2f} {prod.quantity:<10}")
        print("="*70)

    def update_stock(self, product_id, new_quantity):
        """Updates the stock level of a specific item."""
        if product_id in self.products:
            self.products[product_id].quantity = int(new_quantity)
            self.save_inventory()
            print(f"🔄 Stock updated for Product ID {product_id}.")
            return True
        print("❌ Product ID not found.")
        return False

    def delete_product(self, product_id):
        """Removes a product completely from the inventory."""
        if product_id in self.products:
            removed_product = self.products.pop(product_id)
            self.save_inventory()
            print(f"🗑️ Product '{removed_product.name}' removed from tracking.")
            return True
        print("❌ Product ID not found.")
        return False
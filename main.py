from inventory_data import InventoryManager
def main_menu():
    manager = InventoryManager()

    while True:
        print("\n--- INVENTORY MANAGEMENT SYSTEM ---")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Update Stock Level")
        print("4. Delete Product")
        print("5. Exit Application")
        print("6.Create Category")
        
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == '1':
            pid = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()
            cat = input("Enter Category: ").strip()
            while True:
                try:
                    price = float(input("Enter Unit Price ($): "))
                    qty = int(input("Enter Initial Quantity: "))
                    break
                except ValueError:
                    print("⚠️ Invalid numeric value. Please enter numbers for Price and Quantity.")
            manager.add_product(pid, name, cat, price, qty)

        elif choice == '2':
            manager.view_all_products()

        elif choice == '3':
            pid = input("Enter Product ID to update: ").strip()
            while True:
                try:
                    qty = int(input("Enter New Quantity Level: "))
                    break
                except ValueError:
                    print("⚠️ Quantity must be an integer.")
            manager.update_stock(pid, qty)

        elif choice == '4':
            pid = input("Enter Product ID to remove: ").strip()
            manager.delete_product(pid)

        elif choice == '5':
            print("👋 Exiting system. Inventory records saved securely.")
            break
        else:
            print("⚠️ Invalid choice. Please pick an option from 1 to 5.")

if __name__ == "__main__":
    main_menu()

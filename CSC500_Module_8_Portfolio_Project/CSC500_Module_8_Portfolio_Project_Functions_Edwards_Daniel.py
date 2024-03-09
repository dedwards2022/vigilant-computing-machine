"""
This program is for the CSC500 Module 8 Portfolio Project.
    
Author: Daniel Edwards
Version: 0.7
Date: 2024-03-08

Description: This is the functions file for the shopping cart program. It contains the ItemToPurchase and ShoppingCart classes.

Usage: Imported into CSC500_Module_8_Portfolio_Project_Edwards_Daniel.py
   
"""
# ItemToPurchase class
class ItemToPurchase:
    def __init__(self, item_name="none", item_quantity=0, item_price=0.0, item_description="none"):
        self.name = item_name
        self.quantity = item_quantity
        self.price = item_price
        self.description = item_description # Added description attribute

# ShoppingCart class        
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Method to add an item to the cart
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    # Method to remove an item from the cart
    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                item_found = True
                print(f"{item_name} removed from cart.")
                break
        if not item_found:
            print(f"{item_name} was not found in cart. Nothing removed.")

    # Method to modify an item in the cart
    def modify_item(self, ItemToPurchase):
        item_found = False
        for item in self.cart_items:
            if item.name == ItemToPurchase.name:
                item_found = True
                if ItemToPurchase.description != "none":
                    item.description = ItemToPurchase.description
                if ItemToPurchase.price != 0:
                    item.price = ItemToPurchase.price
                if ItemToPurchase.quantity != 0:
                    item.quantity = ItemToPurchase.quantity
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    # Method to get the total number of items in the cart
    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.quantity
        return total_quantity

    # Method to get the total cost of the items in the cart
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.price * item.quantity
        return total_cost

    # Method to print the total cost of the items in the cart
    def print_total(self):
        print("\nOUTPUT SHOPPING CART")
        total_cost = self.get_cost_of_cart()
        total_items = self.get_num_items_in_cart()
        print(f"\n{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print(f"Number of Items: {total_items}")
        if total_items == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item_total = item.price * item.quantity
                print(f"{item.name} {item.quantity} @ ${item.price:.2f} = ${item_total:.2f}")
            print(f"Total: ${total_cost:.2f}")
            
    # Method to print the descriptions of the items in the cart
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")


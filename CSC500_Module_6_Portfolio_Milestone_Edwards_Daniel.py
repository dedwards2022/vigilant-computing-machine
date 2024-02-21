"""
This program is for the CSC500 Module 6 Portfolio Milestone.
    
Author: Daniel Edwards
Version: 0.2
Date: 2024-02-10

Description: This program is show the initizalization of a class and its default constructor and method. The two 
             items are created and their costs are calculated and outputted. The total cost of the items is also 
             calculated and printed.

Usage: python3 CSC500_Module_6_Portfolio_Milestone_Edwards_Daniel.py
   
"""
print("\nFood Price Calculator")  # Print program title

items = {}  # Empty dictionary to store items

total_cost = 0  # Initialize total cost to 0

############################################################################################################
#                                   Part 1: Item To Purchase Class Definition                               #
############################################################################################################

class ItemToPurchase:
    def __init__(self, item_name="none", item_quantity=0, item_price=0.0, item_description="none"):
        self.name = item_name
        self.quantity = item_quantity
        self.price = item_price
        self.description = item_description

    # Method to print item cost    
    def print_item_cost(self):
        print(f"{self.name} {self.quantity} @ ${self.price:.2f} = ${(self.price * self.quantity):.2f}")
        
############################################################################################################
#                                   Part 4: Shopping Cart Class Definition                                 #
############################################################################################################
    
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")

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

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.price * item.quantity
        return total_cost

    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if total_cost == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"Total: ${total_cost}")

    def print_descriptions(self):
        print("Item Descriptions:")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")

    def print_menu():
        print('MENU')
        print("\na - Add Item To Cart")
        print("\nr - Remove Item From Cart")
        print("\nc - Change Item Quantity")
        print("\ni - Output Items' Descriptions")
        print("\no - Output Shopping Cart")
        print("\nq - Quit")
        print("\nChoose An Option: ")
        
def main():                
    
    
# # Collecting item information
# for item in range(2):  # Loop to add two items
#     item_name = input("\nEnter Item Name: ")
#     item_quantity = int(input("Enter Item Quantity: "))
#     item_price = float(input("Enter Item Price: "))
#     items[item_name] = ItemToPurchase(item_name, item_quantity, item_price)

# print("\nTOTAL COST")  # Print total cost of items

# # For loop to print item cost and calculate total cost
# for item_name, item in items.items():
#     item.print_item_cost()
#     total_cost += item.price * item.quantity

# print(f"\nTotal: ${total_cost:.2f}")  # Print total cost of items


if __name__ == "__main__":
    main()

"""
############################################################################################################
#                                           Program Pseudocode                                             # 
############################################################################################################

Output "Food Price Calculator"

Empty dictionary named items

Initialize total_cost = 0

Class named ItemToPurchase:
    Initialize class with item_name = "none", item_quantity = 0, and item_price = 0.0
        Set variables name = item_name, quantity = item_quantity, and price = item_price
        
    Define method to print item cost:
        Print item name, quantity, and price (With correct decimal point formatting)

For item in range(two items):
    User inputs item's name and stores it in item_name
    User inputs items quantity and stores it in item_quantity
    User inputs items price and stores it in item_price
    ItemToPurchase object stores user inputted items in dictionary

Output "TOTAL COST"

For each item_name and item in dictionary:
    Call print_item_cost method for each item
    Add the product name to the total_cost

Output formatted total_cost

"""
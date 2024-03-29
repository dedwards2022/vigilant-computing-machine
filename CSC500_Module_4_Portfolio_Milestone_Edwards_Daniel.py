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

# ItemToPurchase class definition
class ItemToPurchase:
    def __init__(self, item_name="none", item_quantity=0, item_price=0.0):
        self.name = item_name
        self.quantity = item_quantity
        self.price = item_price

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
    
    # Method to add item / items to cart
    def add_item(self, item_to_purchase):
    
        # Method to remove items from cart
        def remove_item(self, item_name):
            if item_name in self.cart_items:
                self.cart_items.remove(item_name)
            else:
                print("Item not found in cart. Nothing removed.") # Print if an item is not found in cart_items list
        
        def modify_item(self, item_to_purchase):
            if item_to_purchase in self.cart_items:
                self.cart_items.append(item_to_purchase)
            elif item_to_purchase not in self.cart_items:
                

# Collecting item information
for item in range(2):  # Loop to add two items
    item_name = input("\nEnter Item Name: ")
    item_quantity = int(input("Enter Item Quantity: "))
    item_price = float(input("Enter Item Price: "))
    items[item_name] = ItemToPurchase(item_name, item_quantity, item_price)

print("\nTOTAL COST")  # Print total cost of items

# For loop to print item cost and calculate total cost
for item_name, item in items.items():
    item.print_item_cost()
    total_cost += item.price * item.quantity

print(f"\nTotal: ${total_cost:.2f}")  # Print total cost of items

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
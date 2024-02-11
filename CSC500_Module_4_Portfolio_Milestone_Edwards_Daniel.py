"""
This program is for the CSC500 Module 4 Portfolio Milestone.
    
Author: Daniel Edwards
Version: 0.1
Date: 2024-02-10

Description: This program is show the initizalization of a class and its default constructor and method. The two 
             items are created and their costs are calculated and outputted. The total cost of the items is also 
             calculated and printed.

Usage: python3 CSC500_Module_4_Portfolio_Milestone_Edwards_Daniel.py
   
"""

# ItemToPurchase class definition
class ItemToPurchase:
    item_name = "none"
    item_quantity = 0
    item_price = 0.0

# Default constructor for the ItemToPurchase class which initializes ItemToPurchase object with default values
def __init__(self, item_name = "none", item_quantity = 0, item_price = 0.0):
    self.item_name = item_name
    self.item_quantity = item_quantity
    self.item_price = item_price
    
def print_item_cost(self):
    print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}")

print("Food Price Calculator\n")

# ItemToPurchase object creation   
item_one = ItemToPurchase()
item_two = ItemToPurchase()

# Gather data for item_one
item_one.item_name = input("Enter Item's Name:")
item_one.item_quantity = int(input("Enter Item's Quantity:"))
item_one.item_price = float(input("Enter Item's Price:"))

# Gather data for item_two
item_two.item_name = input("\nEnter Item's Name:")
item_two.item_quantity = int(input("Enter Item's Quantity:"))
item_two.item_price = float(input("Enter Item's Price:"))

# Print "TOTAL COST" then print the total cost of each item
print("\nTOTAL COST")
print(f"{item_one.item_name} {item_one.item_quantity} @ ${item_one.item_price:.2f} = ${item_one.item_price * item_one.item_quantity:.2f}")
print(f"{item_two.item_name} {item_two.item_quantity} @ ${item_two.item_price:.2f} = ${item_two.item_price * item_two.item_quantity:.2f}")

# Calculate and print the total cost
total_cost = (item_one.item_price * item_one.item_quantity) + (item_two.item_price * item_two.item_quantity)
format_total_cost = "{:.2f}".format(total_cost) # Format the total cost to two decimal places
print(f"\nTotal: ${format_total_cost}") # Print total cost of items

"""
Program Pseudocode

Class ItemToPurchase
    Define item_name as "none"
    Define item_quantity as 0
    Define item_price as 0.0

    Constructor(item_name = "none", item_quantity = 0, item_price = 0.0)
        Set item_name
        Set item_quantity
        Set item_price

    Method print_item_cost
        Print item_name, item_quantity, " @ $", item_price, " = $", (item_price * item_quantity)

End Class

Create item_one as ItemToPurchase
Create item_two as ItemToPurchase

Prompt user "Enter Item's Name:"
Read item_one.item_name
Prompt user "Enter Item's Quantity:"
Read item_one.item_quantity (integer)
Prompt user "Enter Item's Price:"
Read item_one.item_price (float)

Prompt user "\nEnter Item's Name:"
Read item_two.item_name
Prompt user "Enter Item's Quantity:"
Read item_two.item_quantity (integer)
Prompt user "Enter Item's Price:"
Read item_two.item_price (float)

Output "\nTOTAL COST"
Call print_item_cost for item_one
Call print_item_cost for item_two

Calculate total_cost as (item_one.item_price * item_one.item_quantity) + (item_two.item_price * item_two.item_quantity)
Format total_cost to two decimal places
Output "\nTotal: $", formatted total_cost
"""
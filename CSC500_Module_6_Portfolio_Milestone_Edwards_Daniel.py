"""
This program is for the CSC500 Module 6 Portfolio Milestone.
    
Author: Daniel Edwards
Version: 0.6
Date: 2024-02-24

Description: This program simulates a shopping cart system where a user can add, remove, or modify items in their shopping cart.

Usage: python3 CSC500_Module_6_Portfolio_Milestone_Edwards_Daniel.py
   
"""

############################################################################################################
#                                   Part 1: Item To Purchase Class Definition                               #
############################################################################################################

class ItemToPurchase:
    def __init__(self, item_name="none", item_quantity=0, item_price=0.0, item_description="none"):
        self.name = item_name
        self.quantity = item_quantity
        self.price = item_price
        self.description = item_description # Added description attribute
        
############################################################################################################
#                                   Part 4: Shopping Cart Class Definition                                 #
############################################################################################################

# Shopping Cart Class Definition    
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
        print("OUTPUT SHOPPING CART")
        total_cost = self.get_cost_of_cart()
        total_items = self.get_num_items_in_cart()
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
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

############################################################################################################
#                                   Part 5: Print Menu Static Method                                       #
############################################################################################################

    # Static Method to print the menu
    def print_menu():
        user_menu = (
            '\n---------MENU---------\n'
            "\na - Add Item To Cart"
            "\nr - Remove Item From Cart"
            "\nc - Change Item Quantity"
            "\ni - Output Items Description"
            "\no - Output Shopping Cart"
            "\nq - Quit\n"
        )
        print(user_menu)
        user_choice = input("Choose an option: ")
        return user_choice
                
############################################################################################################
#                         Part 6: Main Method (Shopping Cart Output Implementation)                        #
############################################################################################################        

# Main Method        
def main():               
    
    print("\nShopping Cart\n")  # Print program title

    items = {}  # Empty dictionary to store items
    total_cost = 0  # Initialize total cost to 0
    
    shopping_active = True # Flag to control shopping loop
    
    name = input("Enter Customer's Name: ")
    date = input("Enter Today's Date: ")
    customer_cart = ShoppingCart(name, date)
    
    # Shopping Loop
    while shopping_active:
        menu = ShoppingCart.print_menu()
        if menu == 'a': # Add Item To Cart
            print("Add Item To Cart")
            item_name = input("\nEnter Item Name: ")
            item_description = input("Enter Item Description: ")
            item_price = float(input("Enter Item Price: "))
            item_quantity = int(input("Enter Item Quantity: "))
            customer_cart.add_item(ItemToPurchase(item_name, item_quantity, item_price, item_description))
        elif menu == 'r': # Remove Item From Cart
            print("Remove Item From Cart")
            item_name = input("Enter Item Name To Remove: ")
            customer_cart.remove_item(item_name)
        elif menu == 'c': # Change Item Quantity
            print("Change Item Quantity")
            item_name = input("Enter Item Name: ")
            quantity = int(input("Enter New Quantity: "))
            customer_cart.modify_item(ItemToPurchase(item_name, quantity))
        elif menu == 'i': # Output Items Description
            customer_cart.print_descriptions()
        elif menu == 'o': # Output Shopping Cart
            customer_cart.print_total()
        elif menu == 'q': # Quit
            print("\nYou have quit the program.\n")
            shopping_active = False # Set flag to False to exit loop

# Call main method if program is executed directly    
if __name__ == "__main__":
    main()

"""
############################################################################################################
#                                           Program Pseudocode                                             # 
############################################################################################################

Class named ItemToPurchase:
    Initialize class with item_name = "none", item_quantity = 0, item_price = 0.0, and item_description = "none"
        Set variables name = item_name, quantity = item_quantity, price = item_price, and description = item_description

Class named ShoppingCart:
    Initilize class with customer_name = "none", current_date = "January 1, 2020", and cart_items = []
        Set variables customer_name = customer_name, current_date = current_date, and cart_items = cart_items

    Method add_item(ItemToPurchase)
        Add ItemToPurchase to cart_items list

    Method remove_item(item_name)
        Set item_found to False
        For each item in cart_items
            If item's name equals item_name
                Remove item from cart_items
                Set item_found to True
                Output (item_name) + " removed from cart."
                Exit loop

        If item_found is False
            Print (item_name) + " was not found in cart. Nothing removed."

    Method modify_item(ItemToPurchase)
        Set item_found to False
        For each item in cart_items
            If item's name equals ItemToPurchase's name
                Set item_found to True
                If ItemToPurchase's description is not "none"
                    Set item's description to ItemToPurchase's description
                If ItemToPurchase's price is not 0
                    Set item's price to ItemToPurchase's price
                If ItemToPurchase's quantity is not 0
                    Set item's quantity to ItemToPurchase's quantity
                Exit loop

        If item_found is False
            Output "Item not found in cart. Nothing modified."

    Method get_num_items_in_cart()
        Set total_quantity to 0
        For each item in cart_items
            Increase total_quantity by item's quantity
        Return total_quantity

    Method get_cost_of_cart()
        Set total_cost to 0
        For each item in cart_items
            Increase total_cost by item's price multiplied by item's quantity
        Return total_cost

    Method print_total()
        Set total_cost to result of get_cost_of_cart()
        If total_cost equals 0
            Output "SHOPPING CART IS EMPTY"
        Else:
            Output "Output Shopping Cart"
            Output "Total: $" + format total_cost to two decimal places

    Method print_descriptions()
        Output "Item Descriptions: "
        For each item in cart_items:
            Output (fstring) (item's name) : (item's description)

############################################################################################################

    Method print_menu:
        Define user_menu with options:
            "---------MENU---------"
            "a - Add Item To Cart"
            "r - Remove Item From Cart"
            "c - Change Item Quantity"
            "i - Output Items Description"
            "o - Output Shopping Cart"
            "q - Quit"

        Output user_menu

        Ask user to Choose an option:
        Read user_choice from user input
        Return user_choice
        
############################################################################################################

Main Program:

    Output Shopping Cart as program title

    Initialize 'items' empty dictionary
    total_cost equals 0
    Set 'shopping_active' to True (flag to control shopping loop)

    Input from user for 'name' of the customer
        Read & store 'name' of the customer
    Input from user for 'date' of today
        Read & store 'date' of today
    Create a new ShoppingCart instance 'customer_cart' with 'name' and 'date'

    While Loop shopping_active is True:
        Display menu and read user choice into menu
        
        If menu is 'a'
            Output "Add Item To Cart"
            Prompt for item_name
            Read and Store item_name
            Prompt for item_description
            Read and Store item_description
            Prompt for item_price
            Read, Store, and convert to float item_price
            Prompt for item_quantity
            Read, Store, and convert to integer item_quantity
            Add new item to customer_cart
        
        Else If menu is 'r'
            Output "Remove Item From Cart"
            Prompt for and read item_name
            Remove item from customer_cart
        
        Else If menu is 'c'
            Output "Change Item Quantity"
            Prompt user for item_name
            Read and store item_name
            Prompt user for quantity
            Read, convert to integer, and store quantity
            Modify item in customer_cart with new quantity
        
        Else If menu is 'i'
            Call customer_cart.print_descriptions to output item descriptions
        
        Else If menu is 'o'
            Call customer_cart.print_total to output total cost
        
        Else If menu is 'q'
            Output "You have quit the program."
            Set shopping_active flag to False to exit loop

If program is executed directly:
    Call main program
"""
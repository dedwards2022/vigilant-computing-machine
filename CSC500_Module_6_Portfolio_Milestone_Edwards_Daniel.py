"""
This program is for the CSC500 Module 6 Portfolio Milestone.
    
Author: Daniel Edwards
Version: 0.4
Date: 2024-02-20

Description: TODO: Add description

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
                print(f"{item_name} removed from cart.")
                break
        if not item_found:
            print(f"{item_name} was not found in cart. Nothing removed.")

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
            print("Output Shopping Cart")
            print(f"Total: ${total_cost:.2f}") # Added formatting to print total cost with 2 decimal places

    def print_descriptions(self):
        print("Item Descriptions:")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")

############################################################################################################
#                                   Part 5: Print Menu Static Method                                       #
############################################################################################################

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
        
def main():               
    
    print("\nFood Price Calculator\n")  # Print program title

    items = {}  # Empty dictionary to store items
    total_cost = 0  # Initialize total cost to 0
    
    shopping_active = True
    name = input("Enter Customer's Name: ")
    date = input("Enter Today's Date: ")
    customer_cart = ShoppingCart(name, date)
    
    while shopping_active:
        menu = ShoppingCart.print_menu()
        if menu == 'a':
            print("Add Item To Cart")
            item_name = input("\nEnter Item Name: ")
            item_description = input("Enter Item Description: ")
            item_price = float(input("Enter Item Price: "))
            item_quantity = int(input("Enter Item Quantity: "))
            customer_cart.add_item(ItemToPurchase(item_name, item_quantity, item_price, item_description))
        elif menu == 'r':
            print("Remove Item From Cart")
            item_name = input("Enter Item Name To Remove: ")
            customer_cart.remove_item(item_name)
        elif menu == 'c':
            print("Change Item Quantity")
            item_name = input("Enter Item Name: ")
            quantity = int(input("Enter New Quantity: "))
            customer_cart.modify_item(ItemToPurchase(item_name, quantity))
        elif menu == 'i':
            customer_cart.print_descriptions()
        elif menu == 'o':
            customer_cart.print_total()
        elif menu == 'q':
            print("\nYou have quit the program.\n")
            shopping_active = False
    
if __name__ == "__main__":
    main()

"""
############################################################################################################
#                                           Program Pseudocode                                             # 
############################################################################################################

To Do: Add pseudocode

"""
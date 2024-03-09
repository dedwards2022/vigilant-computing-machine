"""
This program is for the CSC500 Module 8 Portfolio Project.
    
Author: Daniel Edwards
Version: 0.8
Date: 2024-03-08

Description: This program simulates a shopping cart system where a user can add, remove, or modify items in their shopping cart.

Usage: python3 CSC500_Module_8_Portfolio_Project_Edwards_Daniel.py
   
"""

# Import ItemToPurchase and ShoppingCart classes from CSC500_Module_8_Portfolio_Project_Functions_Edwards_Daniel.py
from CSC500_Module_8_Portfolio_Project_Functions_Edwards_Daniel import ItemToPurchase, ShoppingCart

# Menu Function
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
    return input("Choose an option: ")

# Main Method        
def main():               
    
    # Print ASCII Art
    ascii_art = """
        ,,,,,,,,,+%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%+,,,,,,,,,
        ,,,,,,,;S@@%*++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*%@@S;,,,,,,,
        ,,,,,,+@@%:+%S#####################SSSSSSSSSSSSSSS#SS###SS#########SS#S####S##S#######S%;:S@@;,,,,,,
        ,,,,,:#@S,?@?;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;%@*:#@S:,,,,,
        ,,,,,;@@*:@@#S######S#######S###########################################################@#,%@@:,,,,,
        ,,,,,;@@*;@%;:;*@S;+@%;*@@?;:;?@@*;;:;+S@S;+#;;#+;S@?;:;?@@@@?;:;?@@?;:;?@@*;;:;?@*:;;;:;#:%@@:,,,,,
        ,,,,,;@@*;%.,*:.+%.:@?.:@*.,*:.*@+.:*;.:@%.,S,.*:.%*.:*,.?@@%.,*,.?%.,*,.?@;.:*:.??*:.:+*#:%@@:,,,,,
        ,,,,,;@@*;%.:@%;*%.:@%.;@+.+@*.+@+.+@?.,@%.:#,.,,.%+.+@?;?@@?.+@*;%*.+@+.*@;.*@+.*@@*.*@@#,%@#:,,,,,
        ,,,,,;@@*:@;.+@@@%.:@%.;@+.+@*.+@+.+@?.,@%.:#,....%+.+@@@@@@?.;@@@@*.+@+.*@;.*@+.*@@+.*@@#,%@#:,,,,,
        ,,,,,;@@%?@#,.%@@?.:@?.;@+.+@+.+@+.*@?.,@%.:#,....%+.+#?%S@@?.;@@@@*.+@+.*@;.+%:.*@@+.*@@@?S@@:,,,,,
        ,,,,,;@@@@@@?.,#@?.,:,.;@+.+@+.+@+.:?;.:@%.:#,....%+.*%..+@@?.;@@@@*.:?:.*@;.,..;#@@*.*@@@@@@#:,,,,,
        ,,,,,;@@@@@@@+,*@?,;*;,+@+,*@+,*@+.,,:*#@%,;#::;,:S+,*@+,?@@*,+@@@@*.,,,.*@+,?;.%@@@*,?@@@@@@#:,,,,,
        ,,,,,;@@@@@@@#::S%,+@%,+@+,*@*,*@+,?@@@@@%,+#:;%::S+,*@+,?@@*,*@@@@*,*@+,?@+,%?.;@@@*,?@@@@@@#:,,,,,
        ,,,,,;@@@@#?%@?,*%,+@%,+@+,*@*,*@+,?@@@@@%,;#::S::S+,?@+,?@@?,*@%?#*,*@+,?@+,%#,:S@@*,?@@@@@@#:,,,,,
        ,,,,,;@@@@?.,?;,*?,+@%,+@+,;?:,?@+,?@@@@@%,;#::S;:S+,;?:,?@@?,:?:,%*,*@+,?@;,?@;,?@@+,?@@@@@@#:,,,,,
        ,,,,,;@@@@#+:,:+S%:*@%:+@S+:,:+#@+:?@@@@@%:+#:;#+;SS+:,:+#@@#+:,:+#*:?@*:?@+:%@?:+@@*:?@@@@@@#:,,,,,
        ,,,,,;@@@@@@#S##@###@@#@@@@###@@@@#@@@@@@@#@@##@@#@@@###@@@@@@###@@@#@@##@@@#@@@###@###@@@@@@#:,,,,,
        ,,,,,;@@?+@@?++++++*#@@%?%#@@@########################################@@@S??S@@#+++++++%@#;%@#:,,,,,
        ,,,,,;@@*:@@%?????%@@S:...:?@@%;;++++;;;+;;+++;;;++++;;;++;++;++++;;;S@@*,..,;#@#??????S@#,%@#:,,,,,
        ,,,,,;@@*:@@%*???*?@@?....,+@@#SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS@@@:...,:%@@?*****S@#,%@#:,,,,,
        ,,,,,:#@S,%@S??????#@@*;:;+S@@%;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;%@@S+::;?@@S??????#@*:#@S,,,,,,
        ,,,,,,+@@%:+?SSSSSSSS##SSSS#SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS#SSSS#SSSSSSSSS?;;S@@+,,,,,,
        ,,,,,,,+#@@%*++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*%@@S;,,,,,,,
        ,,,,,,,,:+%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%+,,,,,,,,,
    """
    print(ascii_art) # Print ASCII Art

    items = {}  # Empty dictionary to store items
    total_cost = 0  # Initialize total cost to 0
    shopping_active = True # Flag to control shopping loop
    
    # Get Customer Name and Today's Date
    name = input("Enter Customer's Name: ")
    date = input("Enter Today's Date: ")
    customer_cart = ShoppingCart(name, date) # Create new ShoppingCart object
    
    # Shopping Loop
    while shopping_active:
        menu = print_menu()
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
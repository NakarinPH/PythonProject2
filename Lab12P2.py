# Nakarin Philangam
# 11/10/2021
# This program prompts the user to input the data into inventory file

from Inventory import Inventory
from book import Book
from magazine import Magazine
from inventory_item import InventoryItem


def main():
    # Create an inventory object
    inventory = Inventory()

    # Load inventories from inventory.dat
    inventory.load_from_file()

    # Display the output of current inventories
    print(inventory)

    # Start the loop to get the input from the user
    continues = 'y'

    while continues == 'y' or continues == 'Y':

        # Create 3 additional objects by asking the user
        item_type = int(input('What item type (1-Book, 2-Magazine, 3-Other)? '))

        # Type 1 Book
        if item_type == 1:
            item = Book()
            item.get_item_input()
        # Type 2 Magazine
        elif item_type == 2:
            item = Magazine()
            item.get_item_input()
        # Other
        else:
            item = InventoryItem()
            item.get_item_input()
        # Add item into inventory list
        inventory.add_item(item)

        # Prompt the user if still needs to input more
        continues = input('Do you want to enter more item? ')

    # Display the data in Inventory list
    print(Inventory)
    # Save the inventory list to the file
    inventory.save_to_file()


# Call the main function to execute the program
main()

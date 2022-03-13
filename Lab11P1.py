# Nakarin Philangam
# 11/02/2021
# This program creates another object by asking the user for the inout

from inventory_item1 import inventory_item


def main():
    print('Start of Lab11P1')

    # Create 3 objects
    book1 = inventory_item('Science Book', 10, 12.95)
    book2 = inventory_item('Math Book', 15, 13.95)
    book3 = inventory_item('Fiction Book', 32, 7.95)

    # Ask the user for another object
    book4 = inventory_item()
    book4.get_item_input()

    # Display the objects
    print('Item 1: ', book1)
    print('Item 2: ', book2)
    print('Item 3: ', book3)
    print('Item 4: ', book4)


main()

# Nakarin Philangam
# 11/10/2021
# This program contains a Book class the store value of a book and return the data into a string type

from inventory_item import InventoryItem


class Book(InventoryItem):

    # Create an addition default attribute
    def __init__(self, name='', count=0, cost=0.0, hardback=True):
        super().__init__(name, count, cost)
        self.hardback = hardback

    # Method to get input from the user
    def get_item_input(self):
        super().get_item_input()
        is_hard_back_book = input('Is this a hardback book (y/n)? ')
        if is_hard_back_book in ['y', 'Y']:
            self.hardback = True
        elif is_hard_back_book in ['n', 'N']:
            self.hardback = False
        else:
            print('Invalid')

    # Method to return the book information in string type
    def __str__(self):
        return super().__str__() + ', Hardback: ' + str(self.hardback)

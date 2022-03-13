# Nakarin Philangam
# 11/10/2021
# This program contains the Inventory class that has method to add item, load data from a file,
# and return the data in string type

import pickle
from os import path


class Inventory:

    def __init__(self):

        # Initialize the inventory_data to an empty list
        self.__inventory_data = []

    # Method to ass item into the inventory list
    def add_item(self, item):
        self.__inventory_data.append(item)

    # Method to lard data from the inventory.dat file
    def load_from_file(self):

        with open('inventory.dat', 'rb') as f:
            if path.exists('inventory.dat'):
                my_file = f.read()
                self.__inventory_data = pickle.loads(my_file)

    # Method to save data to the inventory.dat file
    def save_to_file(self):

        in_file = open('inventory.dat', 'wb')

        pickle.dump(self.__inventory_data, in_file)

        in_file.close()

        print('Inventory.dat file was created.')

    # Method to return data as string type
    def __str__(self):

        data = ''
        for i in self.__inventory_data:
            data += str(i)
        return data

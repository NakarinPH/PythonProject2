# Nakarin Philangam
# 11/04/2021
# This program contain a class named Inventory that hold a collection of inventory data
#

import pickle


class Inventory:

    # This method take only a self argument and initialize the inventory_data to an empty list
    def __init__(self):

        self.inventory_data = []

    # This method take one argument
    def add_item(self, item):

        # Add the item to the inventory_data list
        self.inventory_data.append(item)

    # This argument take no argument
    def load_from_file(self):

        try:

            # Use the pickle module to load inventory data from a file
            with open('inventory.dat', 'rb') as handle:
                data = handle.read()  # opening the file and storing the control to fhand

                # Loading data as list
                self.inventory_data = pickle.loads(data)

        except:

            # Do nothing if not present
            self.inventory_data = list()  # empty list

    def save_to_file(self):

        # opening file in write mode (binary)
        fhand = open("inventory.dat", "wb")

        pickle.dump(self.inventory_data, fhand)

        fhand.close()

        print("Inventory.dat file was created.\n")

    

    # to string method
    def __str__(self):

        # if no item in the inventory
        if len(self.inventory_data) == 0:
            return "\nInventory is empty"

        itemData = ""

        # get each item information in the inventory data list
        for item in self.inventory_data:
            itemData += "\nName: %s, Count: %d, Cost: %.2f\n" % (item["name"], item["count"], item["cost"])

        return itemData

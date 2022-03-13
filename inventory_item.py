# Nakarin Philangam
# 11/10/2021
# This program contains the Inventory class that has methods to get the item, calculate the retail value,
# and return the result into string type

class InventoryItem:

    # Initialize 3 default attributes
    def __init__(self, name='', count=0, cost=0.0):
        self.name = name
        self.count = count
        self.cost = cost

    def get_item_input(self):

        # Ask the user for data and set the object to the values
        self.name = input("Enter the item name: ")
        # Validating name
        while ',' in self.name:
            print("Item names cannot contain commas.")

            self.name = input("Enter the item name: ")
        # Validating item count
        while True:
            try:

                self.count = int(input("Enter the item count: "))
                if self.count < 0:
                    print("Item count must be 0 or greater.")
                else:
                    break
            except:
                print("Item count must be an integer.")

        # Validating unit cost
        while True:
            try:
                self.cost = float(input("Enter the unit cost: "))
                break
            except:
                print("Unit cost must be an integer.")

    # Method to calculate the retail value and return the result
    def get_retail_value(self):

        return self.count * self.cost

    def __str__(self):
        # Return a string that describes the object
        return f"Name: " + self.name + ", Count: " + str(self.count) + ", Cost: " + str(
            self.cost) + ", Retail Cost: " + str(self.get_retail_value())

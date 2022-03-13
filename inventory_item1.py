# Nakarin Philangam
# 11/02/2021
# This program contains a class named inventory_item to get and validate item name, count, and cost

# Create a class
class inventory_item:

    # This method accept 3 arguments
    # Set default arguments if the calling program does not provide an argument
    def __init__(self, name='', count=0, unit_cost=0.0):

        self.name = name
        self.count = count
        self.unit_cost = unit_cost

    def get_item_input(self):

        # Ask the user for data and set the object to the values
        self.name = input("Enter the item name: ")
        # Validating name
        while ',' in self.name:
            print("Item names cannot contain commas.")
            # Reading item name
            self.name = input("Enter the item name: ")
        # Validating item count
        while True:
            try:
                # Reading item count
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
                # Reading unit cost
                self.unit_cost = float(input("Enter the unit cost: "))
                break
            except:
                print("Unit cost must be an integer.")

    def __str__(self):
        # Return a string that describes the object
        return "Name: " + self.name + ", Count: " + str(self.count) + ", Cost: " + str(self.unit_cost)

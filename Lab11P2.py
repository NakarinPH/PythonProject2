# Nakarin Philangam
# 11/04/2021
# This program asks the user to provide the item name, item count, and unit cost


from Inventory1 import Inventory

if __name__ == "__main__":

    # create an Inventory object
    myInventory = Inventory()

    # read previous data from the dat file
    myInventory.load_from_file()

    print(myInventory)

    # adding new items to the inventory

    while True:

        name = input("\nEnter the item name: ")

        count = int(input("\nEnter the item count: "))

        cost = float(input("\nEnter the item cost: "))

        myInventory.add_item({
            "name": name,
            "count": count,
            "cost": cost

        })

        isCont = input("\nDo you want to enter more items? ").lower()

        if isCont == "y":

            continue

        elif isCont == "n":

            break

    print(myInventory)

    myInventory.save_to_file()

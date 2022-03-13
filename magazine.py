# Nakarin Phulangam
# 11/10/2021
# This program contain a Magazine class that has methods to get input from the user then return data into a string type

from inventory_item import InventoryItem


class Magazine(InventoryItem):

    # Initialize an extra default attribute that the magazine type required
    def __init__(self, name='', count=0, cost=0.0, issue_number=0, period=1):
        super().__init__(name, count, cost)
        self.hardback = False
        self.issue_number = issue_number
        self.period = period

    # Method to get input from the user
    def get_item_input(self):
        super().get_item_input()
        issue_num = int(input('What is the issue number? '))
        self.issue_number = issue_num
        period_input = int(input('How often (1-Weekly, 2-Monthly, 3-Other)? '))
        if period_input == 1:
            self.period = 'Weekly'
        elif period_input == 2:
            self.period = 'Monthly'
        else:
            self.period = 'Other'

    # Method to return the data in a string type
    def __str__(self):
        return super().__str__() + ', Issue: ' + str(self.issue_number) + ', Period: ' + str(self.period)

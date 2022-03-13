# David Langley
# 11/30/21

# This function calculates the course hours and cost of enrollment.  It has four parameters:
# id is the ID of the student
# s_in_state is a dictionary of in state students
# c_rosters is a dictionary of class rosters
# c_hours is a dictionary with the credit hours of each class

def calculate_hours_and_bill(id, s_in_state, c_rosters, c_hours):

    # Get course that id is registered
    hours = 0
    cost = 0
    for key in c_rosters:
        if id in c_rosters[key]:
            if key in c_hours:
                hours += c_hours[key]

    if id in s_in_state:
        result = s_in_state[id]
        if result:
            cost = 225 * hours
        else:
            cost = 850 * hours

    display_hours_and_bill(hours, cost)

# This function displays the course hours and the cost of enrollment. It has two parameters
# hours is the number of course hours
# cost is the total cost of enrollment
# This function displays the total number of credit hours and the total cost of enrollment.


def display_hours_and_bill(hours, cost):
    print("Course load:", hours)
    print("Enrollment cost: $", cost)

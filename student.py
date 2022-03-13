# -------------------------------------------------------------------------
# Author: Nakarin Philangam
#         David Langley
#         Kristen Dine
# Date: 11/23/2021
#
# +++++++++++++++++++++++++Additional Change+++++++++++++++++++++++++++++++
# <> This program is added more loops to ask if the user would like
# to add another course, drop another course and it runs the loop
# until the user enter 'n' then it takes the user back to the start menu <>
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -------------------------------------------------------------------------


# -------------------------------------------------------------------------
# This function displays and counts courses a student has
# registered for.  It has two parameters: id is the ID of the
# student; c_roster is the list of class rosters. This function
# has no return value.
# -------------------------------------------------------------------------
def list_courses(id, c_roster):
    print("Courses registered:")
    # Define count to 0
    count = 0
    # Start the loop to get all keys from c_roster dictionary
    for key, value in c_roster.items():
        # Get courses that the student enrolled by id
        if id in c_roster[key]:
            count += 1
            # Displays the course that the student enrolled
            print(key)
    # Displays the number of the course that the student enrolled
    print("Total number:", count)


# ------------------------------------------------------------------------
# This function adds a student to a course.  It has three
# parameters: id is the ID of the student to be added; c_roster is the
# list of class rosters; c_max_size is the list of maximum class sizes.
# This function asks user to enter the course he/she wants to add.
# If the course is not offered, display error message and stop.
# If student has already registered for this course, display
# error message and stop.
# If the course is full, display error message and stop.
# If everything is okay, add student ID to the course’s
# roster and display a message if there is no problem.  This
# function has no return value.
# ------------------------------------------------------------------------
def add_course(id, c_roster, c_max_size):
    loop = 'y'

    while loop == 'y' or loop == 'Y':
        # Asks the user to enter the course they want to add
        course_to_add = input("Enter course you want to add: ")

        # Check if the course exists
        if course_to_add in c_roster:

            # Checks if the course is full
            # Get the current size of course in course_roster
            max_size_value = c_roster[course_to_add]
            if len(max_size_value) == c_max_size[course_to_add]:
                print("Course already full")
                loop = input("Would you like to add another class? [y/n]: ")
            # Checks if student is already enrolled
            elif id in c_roster[course_to_add]:
                print("You are already enrolled in that course")
                loop = input("Would you like to add another class? [y/n]: ")
            # Class exists, not full or have not enrolled
            else:
                c_roster[course_to_add] = id
                print("Course added")
                loop = input("Would you like to add another class? [y/n]: ")
        else:
            print("Course not found")
            loop = input("Would you like to add another class? [y/n]: ")


# -------------------------------------------------------------------------
# This function drops a student from a course.  It has two
# parameters: id is the ID of the student to be dropped;
# c_roster is the list of class rosters. This function asks
# the user to enter the course he/she wants to drop.  If the course
# is not offered, display error message and stop.  If the student
# is not enrolled in that course, display error message and stop.
# Remove student ID from the course’s roster and display a message
# if there is no problem.  This function has no return value.
# -------------------------------------------------------------------------
def drop_course(id, c_roster):
    loop = 'y'

    while loop == 'y' or loop == 'Y':

        # Asks the user to enter the course they want to drop
        course_to_drop = input("Enter course you want to drop: ")

        # Checks if the course exists
        if course_to_drop in c_roster:

            # Checks if student is enrolled
            if id in c_roster[course_to_drop]:
                c_roster[course_to_drop].remove(id)
                print("Course dropped")
                loop = input("Would you like to drop another class? [y/n]: ")
            else:
                print("You are not enrolled in that course")
                loop = input("Would you like to drop another class? [y/n]: ")
        else:
            print("Course not found")
            loop = input("Would you like to drop another class? [y/n]: ")

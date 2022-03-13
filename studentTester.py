import student


def main():
    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444')]

    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False}

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5, 'CSC104': 3}
    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': []}
    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1, 'CSC104': 3}
    id1 = '1001'
    id2 = '1002'
    id3 = '1003'
    id4 = '1004'
    continues = 'y'

    while continues == 'y':
        picked = input("Enter [1] to add a class [2] to drop a class [3] to show the classes: ")

        if picked == '1':
            student.add_course(id1, course_roster, course_max_size)
        elif picked == '2':
            student.drop_course(id1, course_roster)
        elif picked == '3':
            student.list_courses(id1, course_roster)
        else:
            print("invalid")


main()

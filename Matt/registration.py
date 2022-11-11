# ----------------------------------------------------------------
# Author: Team C
# Date: November 10, 2022
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for. It also allows students to review the tuition
# # costs for their course roster.
# -----------------------------------------------------------------

import billing
import student


def main():
    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, in_state_list, course
    # list, max class size list and roster list.  It uses a loop to
    # serve multiple students. Inside the loop, ask student to enter
    # ID, and call the login function to verify student's identity.
    # Then let student choose to add course, drop course or list
    # courses. This function has no return value.
    # -------------------------------------------------------------

    # From the specs: The data given must be used in the program as specified
    # DO NOT CHANGE STUDENT_LIST, STUDENT_IN_STATE, COURSE_HOURS, COURSE_ROSTER, COURSE_MAX_SIZE

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

    # course_roster['ZZZ001'] = ['1001','1002','1003','1004'] # Test Data - Delete before implementation
    # course_hours['ZZZ001'] = 5 # Test Data - Delete before implementation

    while True:
        entered_id = input('Enter ID to login, or 0 to quit: ')
        if entered_id != '0':
            if login(entered_id, student_list):
                while True:
                    course_action = input('Enter 1 to add course, 2 to drop course, \n'
                                          '3 to list courses, 4 to show bill, 0 to exit: ')
                    if course_action == '0':
                        print('Session ended.\n')
                        break
                    elif course_action == '1':
                        student.add_course(entered_id, course_roster, course_max_size)
                    elif course_action == '2':
                        student.drop_course(entered_id, course_roster)
                    elif course_action == '3':
                        student.list_courses(entered_id, course_roster)
                    elif course_action == '4':
                        billing.display_bill(entered_id, student_in_state, course_roster, course_hours)
                    else:
                        print('Please enter a correct choice value.\n')
        else:
            break


def login(id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------

    while True:
        entered_pin = (input('Enter PIN: '))
        for ndx0 in range(len(s_list)):
            if id == s_list[ndx0][0] and entered_pin == s_list[ndx0][1]:  # matches id and pin
                print('ID and PIN verified\n')
                return True
        else:
            print('ID or PIN incorrect\n')
            return False


main()

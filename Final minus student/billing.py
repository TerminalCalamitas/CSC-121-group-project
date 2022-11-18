# ----------------------------------------------------------------
# Author: Team C
# Date: 11/15/2022
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
import datetime


def display_bill(id, s_in_state, c_rosters, c_hours):  # Caleb
    # ------------------------------------------------------------
    # This function displays the student's bill. It takes four
    # parameters: id, the student id; s_in_state, the list of
    # in-state students; c_rosters, the rosters of students in
    # each course; c_hours, the number of hours in each course.
    # The function has no return value.
    # ------------------------------------------------------------

    gen_time = datetime.now()
    time_str = gen_time.strftime("%Y-%m-%d %H:%M:%S")
    total_hours = 0
    total_cost = 0

    print()
    print("Tuition Summary")
    if s_in_state[id]:
        print(f"Student: {id}, In-State Student")
    else:
        print(f"Student: {id}, Out-of-State Student")
    print(time_str)
    print("Course    Hours    Cost  ")
    print("------    -----  --------")
    for key, value in c_rosters.items():
        if id in value:
            if s_in_state[id]:
                class_cost = 225 * c_hours[key]
            else:
                class_cost = 850 * c_hours[key]

            print(f"{key:6s}    {c_hours[key]:>5}  ${class_cost:>7.2f}")

            total_cost += class_cost
            total_hours += c_hours[key]
    print("        -------  --------")
    print(f"Total   {total_hours:>7}  ${total_cost:>7.2f}")

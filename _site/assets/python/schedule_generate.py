# Simple script to create yml data file for course calendar
# Why python? Because I already had a python script that kinda did this, if you must know

import time
from datetime import timedelta
from datetime import date
f = open('syllabus_schedule.yml', 'w')

theDay = date(2015, 8, 24)
week = 1
while theDay < date(2015, 12, 7):
    now = theDay.isoformat()
    f.write("- date: " + now + '\n')
    f.write("  readings: \n")
    f.write("  in_class: \n")
    f.write("  assignment: \n")
    f.write("  assignment_link: \n\n")
    if theDay.weekday() == 4:
        increment = timedelta(days = 3)
    else:
        increment = timedelta(days = 2)
    theDay = theDay + increment

"""
CTI 110
# P4HW1 - Grade
Ask user for six grades,  and store them in the list called "grade "
"""

grades = []
i = 1
for i in range (6):
    num = str(i)
    grade = int(input('Please enter grade for module' , num , ': '))
    grades.append(grade)

    average = sum(grade) / len(grade)
    print('The lowest grade is:', max(grade))
    print('The highest grade is:', min(grade))
    print('The average grade is:', min(grade))
"""
CTI 110
# P4HW1 - Grade
Ask user for six grades,  and store them in the list called "grade "
"""

grades = []

for i in range (6):
    num = str(i + 1)
    grade = int(input('Please enter grade for module' + num + ': '))
    grades.append(grade)

average = sum(grades) / len(grades)
print('The lowest grade is:', min(grades))
print('The highest grade is:', max(grades))
print('The sum grade is:', sum(grades))
print('The average grade is:', average)
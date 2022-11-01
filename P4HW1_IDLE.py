# CTI 110
# P4HW1 - Grade List
# Myra Williams
# 11/1/22

# Ask the user for the 6 grades for 6 modules.
# Add them to list.

#grades = [0, 0, 0, 0, 0, 0]
grades = []

for grade in range(6):
    grade = int(input("Enter grade: "))
    grades.append(grade)


print (" The grades are: ", grades)
# max (grades) and min (grades)
# to show lowest and highest in the list
print ("Highest grade: ", max(grades))
print ("Lowest grade: ", min(grades))


#Now the average - divide the sum by the length (count)
total = sum(grades)
count = len(grades)
average = total / count
print("Total is: ", total)
print("Average is: ", average)

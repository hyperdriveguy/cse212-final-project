# Initialize max attendance for different classes
chemistry = {'Joe', 'Bob', 'Squilliam', 'YeeYee', 'Annathen', 'Leet'}
parkour = {'Bruce Wayne', 'Peter Parker', 'Coney Hork'}

# Initialize current attendance
attendance = set()
attendance.add('Annathen')

# Challenge - Annathen left, remove her from attendance


# Test - size of attendance should be zero
print(len(attendance))

# Challenge
# Add two names to the current attendance set from the chemistry class


# Test - should always be False
print('Bruce Wayne' in attendance)

# Challenge
# Add a name to the current attendance set from the chemistry class twice


# Test - Added name should only appear once
print(attendance)

# Challenge - Get the number of total students using a union
total = 0


# Test - print total number of students
# 13
print(total)

# Challenge - use an intersection to check who is in both classes


# Test - print who is in both classes
# {'La-a', 'Leet'}
print(both_classes)

# Clear attendance
attendance = set()

# Stretch - check for attendance in the parkour class

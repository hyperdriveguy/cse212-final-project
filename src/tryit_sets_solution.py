# Initialize max attendance for different classes
chemistry = {'Joe', 'Bob', 'Squilliam', 'YeeYee', 'Annathen', 'Leet'}
parkour = {'Bruce Wayne', 'Peter Parker', 'Coney Hork'}

# Initialize current attendance
attendance = set()
attendance.add('Annathen')

# Challenge - Annathen left, remove her from attendance
attendance.remove('Annathen')

# Test - size of attendance should be zero
print(len(attendance))

# Challenge
# Add two names to the current attendance set from the chemistry class
attendance.add('Joe')
attendance.add('Squilliam')

# Test - should always be False
print('Bruce Wayne' in attendance)

# Challenge
# Add a name to the current attendance set from the chemistry class twice
attendance.add('Leet')
attendance.add('Leet')

# Test - Added name should only appear once
print(attendance)

attendance = set()

# Stretch - check for attendance in the parkour class

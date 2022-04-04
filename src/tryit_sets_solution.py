# Initialize max attendance for different classes
chemistry = {'Joe', 'Bob', 'Squilliam', 'YeeYee', 'Annathen', 'Leet', 'La-a'}
parkour = {'Bryce Whine', 'La-a','Pater Puker', 'Coney Hork', 'Juan Shiqua', 'Nicolas Rage', 'Leet', 'Yeetus McReetus'}

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
print(len(attendance.intersection(parkour)) > 0)

# Challenge
# Add a name to the current attendance set from the chemistry class twice
attendance.add('Leet')
attendance.add('Leet')

# Test - Added name should only appear once
print(attendance)

# Challenge - Get the number of total students using a union
# total = 0
total = len(chemistry.union(parkour))

# Test - print total number of students
# 13
print(total)

# Challenge - use an intersection to check who is in both classes
both_classes = chemistry.intersection(parkour)

# Test - print who is in both classes
# {'La-a', 'Leet'}
print(both_classes)

attendance = set()

# Stretch - check for attendance in the parkour class

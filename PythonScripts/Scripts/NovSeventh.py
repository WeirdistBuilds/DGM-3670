# int
# float
# strings
# list [] mutable, ordered, any data type can go in
# sets {} immutable, unordered, any data type can go in
# dictionaries {ball:definition}

# declaring variables:
# string $sels = 'ls -sl';

import maya.cmds as cmds
sels = cmds.ls(sl=True)
print sels

numInt = 3
numFloat = 6.3
print numInt
print numFloat

students = [['Bill,', 'Bob', 'Candace', 'Rebecca'],
            [100, 98, 67, 37],
            ['Clayton', 'Clayton', 'Clayton', 'Clayton']]

# access names
print students[0]

# access rebecca
print students[0][3], students[2][0]


# loops (prints each element in array)
for student in students:
    print student

# this is from 0-9
for i in range(10):
    print i

# this is like size(array)
for j in range(len(students)):
    print j
    print students[j]

for name in students[0]:
    # student is ['Bill,', 'Bob', 'Candace', 'Rebecca']
    print name, 'is great!'

# nested loops
for student in students:
    # student is ['Bill,', 'Bob', 'Candace', 'Rebecca']
    for s in student:
        print s, 'is great!'

# printing by index in list
for i in range(len(students[0])):
    print 'Name:', students[0][i]
    print 'Score:', students[1][i]
    print 'Fav:', students[2][i]
    print '---------------------'

print 'Complete.'

nameString = 'KyleHinckley'
print nameString[4:12]
print nameString[-1:-5]

# if statements
if 3 < 5:
    print '3 is less than 5'
else:
    print 'somehow, 3 is MORE than 5?!'


# do python sololearn as far as possible
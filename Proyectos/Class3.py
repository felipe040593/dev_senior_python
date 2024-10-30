age = int(input('How old are you?'))
country = 'COL'
userHasDNI = True

if age >= 21:
    print("You can buy alcohol in USA")
elif age >= 18:
    print('You can buy alcohol in COL')
elif age >= 16:
    print('You can buy alcohol in GER') 
else:
    print('You can\'t buy alcohol')

if age >= 21 and country == "USA":
    print("You can buy alcohol in USA")
elif age >= 18 and country == "COL":
    print('You can buy alcohol in COL')
elif age >= 16 and country == "GER":
    print('You can buy alcohol in GER') 
else:
    userHasDNI = False
    print('You can\'t buy alcohol')
    
# for variables in objectToIterate:
#   actions
# For each value of the i in the range of 10
# student = 0
# print(student)
# student = 1
# print(student)
# student = 2
# print(student)
# ...
# student = 9
# print (student)
for student in range(10):
    print(student)
    
# while condition:
#   actions
studentNumber = 0
while userHasDNI:
    studentNumber += 1 
    print(studentNumber)
    if studentNumber == 10:
        userHasDNI = False
    if age >= 21 and country == "USA":
        print("You can buy alcohol in USA")
    elif age >= 18 and country == "COL":
        print('You can buy alcohol in COL')
    elif age >= 16 and country == "GER":
        print('You can buy alcohol in GER') 
    else:
        userHasDNI = False
    print('You can\'t buy alcohol')
    
print("####################################")

for student in range(10):
    
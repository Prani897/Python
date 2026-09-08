# print("Pranali Dukhande")
# print("o----")
# print(" ||||")
# print("*" * 10 )

# variables

price = 10
rating = 4.9
name = "Pranali"
is_published = True
print(price)

#Assignment `Hospital`

pateint_name = "Pranali"
pateint_age = 20
is_new  = True

#input

name = input("What is your name? ")
favorite_color = input("What is your favorite color? ")
print(name + " likes " + favorite_color)

#calculation
birth_year = input("Birth year: ")
print(type(birth_year))
age = 2026 - int(birth_year)
print(type(age))
print(age)

weight_lbs = input("Weight (lbs): ")
weight_kg = int(weight_lbs) * 0.45 #TYPE CASTING
print(weight_kg)

#strings
course =   "Python for Beginners"
#INDEX      012345 678 91011121314151617
# -VE INDEX 0-17

print(course)
print(course[0])
print(course[-2])
print(course[0:3])
course1 = "Python's course for Beginners"
print(course1)
course2 = 'Python for "Beginners"'
print(course2)
course3 = '''
Hi Pranali,

Here is our first email to you.

Thank you,
The Team '''

print(course3)  

#FORMATING STRIBGS
first = "Pranali"
Last = "Dukhande"
Message = first + " [" + Last + "] is a coder"
msg = f"{first} [{Last}] is a coder"
print(Message)
print(msg)

#string methods
course = "Python for Beginners"
print(len(course)) #not a method its a function
print(course.upper())
print(course.lower())
print(course.find('P'))
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course) #boolean expression
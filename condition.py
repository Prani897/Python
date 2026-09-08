is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a Lovely day")
print("Enjoy your day!")


price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price 
print(f"Down payment: ${down_payment}")

#logical operators
# AND: BOTH
# OR: EITHER
# NOT: OPPOSITE

has_high_income = True
has_criminal_record = True

if has_high_income and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


#comnparison operators
temperature = 30

if temperature > 30:
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
else:
    print("It's a lovely day")  

#ASSIGNMENT 

name = input("Enter your name: ")
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")


# assignment2

enter_weight = int(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    weight = enter_weight * 0.45
    print(f"You are {weight} kilos")
elif unit.upper() == "K":
    weight = enter_weight / 0.45
    print(f"You are {weight} pounds")
else:
    print("Invalid unit")
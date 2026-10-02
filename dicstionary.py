customer ={
    "Name" : "John Smith",
    "age" : 30,
    "is_verified" : True
}

print(customer["Name"])

#assignment

numbers = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero",
}

phone =input("Enter Your Phone No : ")

output =""
for i in phone:
    output += numbers.get(i, "!") + " "
print(output)
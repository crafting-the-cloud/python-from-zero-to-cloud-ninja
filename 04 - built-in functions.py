# get the variable's data type

name = "Ahmed"
age = 42
is_employee = True

type(name)

###########################################################################################
# print something on screen

print(name)
print (type(name))

name_type = type(name)
print(name_type)

##########################################################################################
# get user input

city = input("Enter city name : ")
print("City name is : " +city)


##########################################################################################
# Casting data types

# Getting numeric input
age = input("Enter your age: ")  # Returns a string
age = int(age)  # Convert to integer

# Getting decimal input
height = input("Enter your height in meters: ")
height = float(height)  # Convert to float

# Using conversion directly
salary = float(input("Enter your salary: "))

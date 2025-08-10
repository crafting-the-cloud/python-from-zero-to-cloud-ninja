
# Equals ==
# Not equals !=
# Greater than >
# Less than <
# Greater than or equals >=
# Less than or equals <=

age1 = 40
age2 = 40


if age1 == age2:
    print("Ages are aequal")
    
age1 = 30
age2 = 40

if age1 < age2:
    print("age1 is less than age2")
    
if age1 > age2:
    print("age1 is greater than age2 !")
    
# Let make it bit complex

if age1 > age2:
    print("age1 is greater than age2 !!")
elif age1 < age2:
    print("age1 is less than age2 !!")
    
# Let make it more complex  

if age1 > age2:
    print("age1 is greater than age2 !!!")
elif age1 == age2:
    print("age1 is less than age2 !!!")
else:
    print("None of the conditions applied !!!")
    
# AND  - OR
#true and true = true
#true or false = false
#false and false = false
#false or false = false
################################

gender = 'male'

#false or tue = true
if age1 > age2 or gender=='male':
    print("Condition applied #" )

#false and true
if age1 > age2 and gender=='male':
    print("Condition applied ##" )
    
if age1 > age2 and gender=='male':
    print("Condition applied ###" )
else:
    print("Else applied ###" )    
    
    
# # Assignment 3
'''
Write a Python program that asks the user to enter their age.
- If the age is less than 13, print "You are a child."
- If the age is between 13 and 19 (inclusive), print "You are a teenager."
- If the age is 20 or above, print "You are an adult."
 
Bonus:
Modify the program to also check if the user enters a negative number or zero, and display an appropriate message.
'''    


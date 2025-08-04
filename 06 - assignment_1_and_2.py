# Assignment 1
# Write a program with a variable item price 500 and define a variable price increate pct that 
# takes its value as a user input
# increase the item price with 25% and print the final item price after the increase

item_price = 500
increase_pct = float(input("Please entewr the price increment pct : "))

print ("The program will increase the price with "+str(increase_pct))
final_price = item_price + item_price*increase_pct

print ("The fnal price is  "+str(final_price))


# Assignment 2
# Write a prgram with a variable item name define a variable item code that 
# takes its value as a user input
#print the following output 'The code of item #item_name is #item_code'
#Example : 'The code of item Asus ROG Laptop  is ARL001'

item_name = "Asus ROG Laptop"
item_code = input("Please enter item code : ")
print("The code of item "+item_name+" is "+item_code)

print("The code of item {0} is {1}".format(item_name,item_code))
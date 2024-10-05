# Operator Precedence
#Describes the order in which operations are performed in an expression
# Given expressions dealing with differnet operators
#Operators of the high precedence are executed first
#The law of BODMAS
#Examples
result = 3*4+5
print(result)

result_two = 3*(4+5)
print(result_two)

result_three = 3*4 +5-1
print(result_three)

reslut_four = 3*(4+5)-1
print(reslut_four)

result_five = 5*3**2
print(result_five)

result_six = (5+3)*2**2-10/2
print(result_six)

result_seven = 25/5 + 2*1
print(result_seven)

result_eight = (25/5)+ 2*1
print(result_eight)

#CONTROL FLOW STRUCTURES
#Porgram can be executed basing on conditions or loops


#Create a program that asks a user for the food type bought from the market.
# The prpgram should print
# you brought chicken if the user bougfht or print liver if the user bought liver
#else the program should print the part of fish

food_type = input("Enter the food type bought: ")
#Working with condtional statments # Approach One

   
if food_type == "chicken":
    print(f"you bought chicken from the market: ")
elif food_type == "liver":
    print(f"you bought liver from the market: ")
elif food_type =="fish":
    print(f"you bought fish from the market")

else: 
    print(f"please choose from chicken, liver and fish") 

#Approach two
if food_type != "chicken" or food_type != "fish" or food_type !="liver":
     print(f"please choose from chicken liver and fish")



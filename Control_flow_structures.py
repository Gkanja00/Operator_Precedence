#Control flow structures
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

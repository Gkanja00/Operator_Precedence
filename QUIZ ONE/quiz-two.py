# Write a program that takes two numbers as inputs and displays their sum, product, difference and quotient?
#Write a program that compare two intergers and prints whether the first number is greater than, less than or equal t the second number?
#Write a program that checks if a given number is between 10 and 20 using logical operators( 20 is inclusive)
# Write the program that prints the squares if all intergers from 1-10 uing a for loop?
# Write a simple program that asks a user for their age, if the user age is greater or equal to 18, print adult and you are qualified, else you tell them you are not qualified.

#QUESTION 1
# We have the following student details and marks, enter these details from the key board
#first student detail is the student name = Ritah Liz
# Student number+ SEP23/BCS/14
#Programming = 78
#Data science = 89
# Computer Applications =55
# Calculate the average mark and print the answer in 3 decimal places

#QUESTION 2
#Write a program that converts celcious temperature to faranahight, the program should ask the user to enter the temp in celicious degrees and then display the temp converted to faranahight degrees
#A car's miles can be counted by a gallaton can be calculated by the following formula:
#Write a program that asks a user for number of miles driven and gallons used. It should calculate the car's miles-per-gallon;-used and display the result
# MPG = Milesdriven/gallons of gas used.

#ANSWERS
#ONE
first_number = int(input('enter the first number: '))
second_number = int(input('enter the second number: '))
sum = first_number + second_number
print(f"The sum of {first_number} and {second_number} is : {sum}")

product = first_number *second_number
print(f"The product of {first_number} and {second_number} is :{product}")
difference =  second_number-first_number
print(f"The difference of {first_number} and {second_number} is :{difference}")
quotient = second_number/first_number
print(f"The quotient of {second_number} and {first_number} is : {quotient}")
modulus = second_number % first_number
print(f'The modulus of{second_number} and {first_number} is : {modulus}')
floor_division =first_number // second_number
print(f"The floor_division of{first_number} and {second_number} is : {floor_division}")

#TWO
#Comparision operators
# f loops
a = int(input("enter"))

first_number = int(input("Enter the first_number: "))
second_number = int(input("Enter the second_number: "))
if first_number> second_number:
    print(f"{first_number} is greater than {first_number}")

elif first_number<second_number:
    print(f" {first_number}is less than {second_number}")
else:
    print(f"{first_number} is equal to {second_number}")
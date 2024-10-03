#ASSIGNMEMT
# Question 1 Write a program that checks if a given number is between 10 and 20 using logical operators( 20 is inclusive)
#Question 2 Write the program that prints the squares if all intergers from 1-10 using a for loop?
#Question 3 Write a simple program that asks a user for their age, if the user age is greater or equal to 18, print adult and you are qualified, else you tell them you are not qualified.

#QUESTION 1
# We have the following student details and marks, enter these details from the key board
#first student detail is the student name = Ritah Liz
# Student number= SEP23/BCS/14
#Programming = 78
#Data science = 89
# Computer Applications =55
# Calculate the average mark and print the answer in 3 decimal places

#QUESTION 2
#Write a program that converts celcious temperature to faranahight, the program should ask the user to enter the temp in celicious degrees and then display the temp converted to faranaheight degrees
#A car's miles can be counted by a gallaton can be calculated by the following formula:
#Write a program that asks a user for number of miles driven and gallons used. It should calculate the car's miles-per-gallon;-used and display the result
# MPG = Milesdriven/gallons of gas use

#ANSWERS
#ONE
# number = int(input("Enter number: "))
# if 10 < number <= 20:
#     print("number is between 10 and 20 and 20 is inclusive")
# else:
#     print("number is not between 10 and 20")

 #TWO   
 
# intergers = [1, 2, 3, 4 , 5 , 6, 7, 8, 9, 10]
# for x in intergers:
#     x= x*x
#     print(x)

# #THREE
# age = int(input("Enter age: "))
# qualified_adult = 18
# if age >= qualified_adult:
#     print(f"adult and you are qualified")
# else:
#      print(f"you are not qualified")

 #FOUR
# student_name = input("Enter your student name: ") 
# student_number = input("Enter student number: ") 
# programming = int(input("Enter marks for programming :"))
# data_science = int(input("Enter marks for data_science :"))
# computer_application = int(input("Enter marks for computer application :"))    
# total_mark=programming + data_science + computer_application
# number_of_course_units =  3
# average_mark = total_mark / number_of_course_units
# print(f"The average mark is: {average_mark:.3f}")

#FIVE
temperature_in_celicious = float(input("Enter th temperature in celicous degress: "))
degrees_in_faranaheight = temperature_in_celicious *1.8
result = temperature_in_celicious / degrees_in_faranaheight
print(f"The result is: {result:.2f}")

# # # #SIX
# miles_driven = int(input("Enter the number of miles: "))
# gallons_used = int(input("Enter the number of gallons used: "))
# mpg = miles_driven / gallons_used
# print(f"The car's miles driven per gallon is : {mpg}")



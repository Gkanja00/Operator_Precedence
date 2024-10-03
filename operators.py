#Arithmatic operators involves mathematical operations

#ASSIGNMENT OPERATORS
#first access the variable and then access the operator
sum = 5
sum+= 7
print(sum)
#given that we have two products a laptop and a mouse such that the price of a laptop is 300,000 and the price of the mouse is 50,000,
# use a for loop to find the total sum of the product
laptop = 300000
mouse = 50000

product_prices = [laptop, mouse, 7000]
for price in product_prices:
    sum = 0
    sum+=price
print(f"The total sum of the product is: {sum:,}")
#final value, print should start from the edge
#VALUABLES NAMES
#Variable names
my_name= "grace"

#Camel Case
myName = "grace"

#Pascal Case
MyName = "grace"

#Snake case
my_name_is = "grace"

#ASSIGN MULTIPLE VALUES
#Many values to multiple valuables
x,y,z = "apples","peas","watermelon"
print(x)
print(y)
print(z)

#One value to multiple valuables
x=y=z="apples"
print(x)
print(y)
print(z)

#unpacking a collection
fruits = ("apples","peas","watermelon")
x,y,z = fruits
print(x)
print(y)
print(z)

#OUTPUT VALUABLES
x = "python is great"
print(x)

x="python" #multiple variables separated by a comma
y="is"
z="great"
print(x,y,z)

#add + operator to output multple variables
x="python"
y="is"
z="great"
print(x+y+z)

#GLOBAL VARIABLES
x="awesome"
def myfunc():
    print("python is" + x)

myfunc()
x="great"
def myfunc():
    global x
x="fantastic"
myfunc()
print("python is" + x)


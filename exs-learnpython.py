mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)

print("****************************")
# Accessing an index which does not exist generates an exception (an error).
myNewlist = [5,6,7]
# print(myNewlist[10]) error!!!!!
print(myNewlist)

# In this exercise, we need to add numbers and strings
# to the correct lists using the "append" list method.
# You must add the numbers 1,2, and 3 to the "numbers" list,
# and the words 'hello' and 'world' to the strings variable.
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# add numbers
print("****************************")
numbers.append(1)
numbers.append(2)
numbers.append(3)

second_name = names[1]

strings.append("Hello")

strings.append("World!")

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
print("****************************")

# Using two multiplication symbols makes a power relationship.
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)
print("****************************")


# The target of this exercise is to create two lists called x_list and y_list,
# which contain 10 instances of the variables x and y, respectively.
# You are also required to create a list called big_list,
# which contains the variables x and y, 10 times each,
# by concatenating the two lists you have created.
x = object()
y = object()

x_list = [x]*10
y_list = [y]*10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
print("****************************")

# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))
print("****************************")

data = ("John", "Doe", 53.44)
format_string = "Hello"

print("%s %s %s! Your current balance is %f" % (format_string, data[0], data[1], data[2]))

print("****************************")
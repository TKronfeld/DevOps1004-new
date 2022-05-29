isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Three"
my_names = ["Adi", "Ben", "Noam", "Arthur", "Ron"]
my_list = []
# function that get input and put to variable age as string
age = int(input("Enter your age:"))
if 0<age<120:
    print("OK")
else:
    print("Can't be!!!")

if a < b and not (strThree == 3 or isTrue == 4):
    print ("a is less than b")
elif a == b:
    print("a is equal to b")
elif strOne != strThree:
    print("Hello")
else:
    print("a is greater than b")
print("*************************")

if my_names[0] == "Zohar" or my_names[1] == "Zohar" or my_names[2] == "Zohar" or my_names[3] == "Zohar":
    print("Zohar")
else:
    print("Other names")

if "Zohar" in my_names:
    print("Zohar")
else:
    print("Other names")
print("*************************")

if my_list:
    print("My list id not empty")

if my_names:
    print("My names is not empty")

# function len - number of the elements in the list
if len(my_names) > 3:
    print("I remember enough names - %d" % len(my_names) )
else:
    print("I need memory exercises")

print("*************************")

aa = 2
bb = 2
cc = [1, 2, 3]
dd = [1, 2, 3]

if aa == bb:
    print("aa equal to bb")
if cc == dd:
    print("cc equal to dd")
# integer - the same pointer to the number for all equal integers
if aa is bb:
    print("aa is bb")
# list - different pointer in memory, then the answer is not equal
if cc is dd:
    print("cc is dd")
if type(a) is int:
    print("What a great integer!")

print("*************************")



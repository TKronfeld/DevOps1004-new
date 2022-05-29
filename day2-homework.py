print("Second day homework")
print("******************************")
print("Exersice A")
X = 0
Y = 2
if X < Y:
    print("X smaller than Y")
else:
    print("X bigger than Y")
print("******************************")

print("Exersice B")
for i in range(5):
    print(f"Iteration number #{i + 1}")
print("******************************")

print("Exersice C")
my_variable = 1
if my_variable == 1:
    print("Summer")
elif my_variable == 2:
    print("Winter")
elif my_variable == 3:
    print("Fall")
elif my_variable == 4:
    print("Spring")
else:
    print("Undefined season name")

print("******************************")
print("Exersice D")
count = 1
print(f"While will be running #{11 - count} times")
while count < 11:
    print(count)
    count = count + 1
print("******************************")

print("Exersice E")
age = 46
first_name_letter = 'K'
current_shekels_dollar_currency = 3.27
abroad_flight = True
apartment_number = 16
print("My personal info")
print(f"My age {age}")
print(f"First letter of my last name is {first_name_letter}")
print(f"Current shekels-dollar currency is {current_shekels_dollar_currency}")
print(f"Did I flew abroad?  {abroad_flight}")
print(f"My apartment number is {apartment_number}")
print(f"Currency + age - {current_shekels_dollar_currency + age}")
print("******************************")

print("Exersice F")
current_input = input("Enter your phone number. At the end press enter: ")
print(f"Phone number {current_input}")
print("******************************")

print("Exersice G")


def printHello():
    print("Hello")


def calculate():
    number = 5 + 3.2
    print(f"Number is {number}")


printHello()
calculate()
print("******************************")

print("Exersice H")


def namepr():
    input_from_user1 = input("Enter your name: ")
    if input_from_user1.isalpha():
        print(f"Your name is: {input_from_user1}")
    else:
        print(f"Your name contains wrong characters: {input_from_user1}")


def numberdiv():
    input_from_user2 = input("Enter your number: ")
    if input_from_user2.isnumeric():
        input_from_user2 = int(input_from_user2)
        print(f"Number after division by 2: {input_from_user2 / 2}")
    else:
        print(f"Your number contains wrong characters: {input_from_user2}")


namepr()
numberdiv()
print("******************************")

print("Exersice I")


# Write a program with the following:
# 1. Method that receive two numbers, add them, and return the sum.
# 2. Method that receive two Strings, add space between them, and return one spaced string.
def numberadd():
    number_from_user1 = input("Enter your first number: ")
    number_from_user2 = input("Enter your second number: ")
    if number_from_user1.isnumeric() and number_from_user2.isnumeric():
        return int(number_from_user2) + int(number_from_user1)
    else:
        return 0


def stringsadd():
    string_from_user1 = input("Enter your first string: ")
    string_from_user2 = input("Enter your second string: ")
    return f"{string_from_user1} {string_from_user2}"


print(f"The summary we have get - {numberadd()}")
print(f"The spaced strings - {stringsadd()}")
print("******************************")

print("Exersice K")
for i in range(10):
    print('#' * i)

print("******************************")
# I know I didn't do it well, but I didn't find another way
print("Exersice L")
i = 7
for n in range(0, 5, 1):
    if (i - 2 * n) == 0 or (i - 2 * n) < 0:
        print(" " * n + "#" + " " * (i - 2 * n) + "")
    else:
        print(" " * n + "#" + " " * (i - 2 * n) + "#")

k = 8
for m in range(3, -1, -1):
    if (m - k) < 0:
      print(" " * m + "#" + " " * (k-1-2*m) + "#")

print("******************************")
print("Exersice M")

def getnum():
    number_from_user3 = input("Enter your number to calculate digit summary: ")
    if number_from_user3.isnumeric():
        return int(number_from_user3)
    else:
        return 0


def calcul(num, sumnum):
    for digit in str(num):
        sumnum += int(digit)
    return sumnum


print(calcul(getnum(), 0))
print("******************************")

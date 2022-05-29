# Overdramatic code

def get_age():
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age can not be negative")

try:
    get_age()
except ValueError as e:
    print(e.args)


a = int(input("enter your number"))

# OR

def check_my_num(num):
    a = ""
    try:
        a = num
    except ValueError:
        return False
    if str(num).isdecimal() or str(num).isdigit():
        return False


a = input("enter number: ")
check_my_num(a)

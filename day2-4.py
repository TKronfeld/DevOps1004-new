# function definition
def square(num):
    result = num * num
    return result


a = square(4)
print(a)
print("*********************")

aa = int(input("Enter your age: "))
if 0 < aa < 120:
    print("OK")
else:
    print("Not OK")
b = int(input("Enter amount of pets: "))
if 0 < b < 4:
    print("OK")
else:
    print("Not OK")

print("*********************")


# The same but with function
def validate(prompt, minT, maxT, ok, not_ok):
    input_from_user = int(input(prompt))
    if minT < input_from_user < maxT:
        return ok
    else:
        return not_ok


print(validate("Enter your age: ", 0, 120, "age is good", "age is not good"))
print(validate("Enter amount of pets: ", 0, 4, "Wow!", "Can't believe!"))

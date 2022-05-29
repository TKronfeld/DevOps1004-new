# Error handling
# for i in range(5):
#   print("hello")

# import requests
# requests.get("ht5p://www.google.com")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)
    r = open("file_not_exist.txt")
except ZeroDivisionError:
    print("Can not divide by zero")
except FileNotFoundError:
    print("Could not find file")
except Exception as e:
    print("Something went wrong")
    print(e.args)
print("**************")



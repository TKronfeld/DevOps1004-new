from PIL import Image

print("3-d day homework")
print("******************************")
print("Exersice 1-2")


def check_my_num(num):
    tmp_int = 0
    try:
        tmp_int = int(num)
    except ValueError:
        print("Invalid literal - ", num)
        return False


print("Need to print the result of a = 1/0")
a = "1 / 0"
check_my_num(a)

print("******************************")
print("Exersice 3")


def finally_func():
    try:
        x = 1
    finally:
        print("finally")
        print("Finally block always gets executed either exception is generated or not")


finally_func()

print("******************************")
print("Exersice 4-5")

try:
    r = open("file_not_exist.txt")
except Exception as e:
    print("General Exception - catch all exceptions. Doesn't give indication for specific problem")

print("******************************")
print("Exersice 6")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)
    rx = open("file_not_exist.txt")
except ValueError:
    print("Invalid character")
except ZeroDivisionError:
    print("An error raised if the result is infinite number. Can't divide by zero.")
except IOError:
    print("An error raised when an input/output operation fails. Check if disk full or file can be not found”.")

print("******************************")
print("Exersice 7-9")


def create_and_write_file(file, my_name):
    my_file1 = open(file, "w+")
    my_file1.write(f"{my_name}\n")


def read_and_print_file(file):
    with open(file) as my_file2:
        for line in my_file2.readlines():
            #   line = line.encode('UTF-8')
            print(f"{line}", end='')


my_file = "words.txt"
my_name = "Tanya Kronfeld"

create_and_write_file(my_file, my_name)
read_and_print_file(my_file)

print("******************************")
print("Exersice 10")

hebrew_content = "אני טניה"

my_file2 = open("hebrewfile.txt", 'w', encoding='utf-8')
my_file2.write(hebrew_content)
my_file2.close()

my_file2 = open("hebrewfile.txt", 'r', encoding='utf-8')
str1 = my_file2.read()
print(str1)

print("******************************")

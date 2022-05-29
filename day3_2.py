my_file = open("urls.txt")
# get file descriptor - memory pointer and move it while reading
# default file openning is read only
for line in my_file.readlines():
    print(line, end='')  # instead new line put ''
    # or print(line.strip())
# seek(0) - move the pointer to the beginning
print("************")
my_file = open("names.txt", "w")
# If file exist, it reopen it, all previous content is removed
for i in range(5):
    current_name = input("enter your name: ")
    my_file.write(f"{current_name}\n")

my_file.close()


names_fun(my_file, my_name)
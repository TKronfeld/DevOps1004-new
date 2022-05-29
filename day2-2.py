a = "hello world!"

# print list of what range return
print(list(range(5)))
# print list of what range return from to
print(list(range(1,5)))
# print list of what range return from to with steps
print(list(range(1,10,3)))
print(list(range(20,-10,-3)))
print("*************************")
for i in range(5):
    # f-sum of list
    print(f"hello world #{i}")

my_names = ["Adi", "Ben", "Noam", "Arthur", "Ron"]
# foreach
# after loop ends, name doesn't exit
for name in my_names:
    print(f"hello {name}")
else:
    print("all names")

# old syntax for foreach
for i in range(len(my_names)):
    print(my_names[i])

vvv = 0
while vvv < 5:
    print(vvv)
    if vvv == 2:
       break
    vvv = vvv + 1




l = []
current_input = input("enter letter: ")
while current_input != "q":
    l.append(current_input)
    current_input = input("enter letter: ")
print("the letters you have entered %s" %l)
print(f"inputs are {l}")

print("*************************")
# print "Hello world" 10 times
print(a*10)

print("*************************")
n = [1, 2, 3, 4, 5]
result = []
for num in n:
    result.append (num*2)
# the same is before
result = [num * 2 for num in n if num > 2]

print("*************************")

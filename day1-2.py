# float number
a = 7.3
af = "Moshe"

# Few ways for implementation to add strings
# Way 1
aName = "Moshe"
bName = "Dayan"
cName = aName + " " + bName
print("Way1 printing name - ", cName)
# Way 2
dName = f"{aName} {bName}"
print("Way2 printing name - ",dName)
# Way 3
eName = "%s %s" % (aName, bName)
print("Way3 printing name - ", eName)
# Way 4
fName = "{} {}".format(aName, bName)
print("Way4 printing name - ", fName)

# Try lists with "" in value
myList1 = "Alex \"Kronfeld\""
myList2 = 'Alex "Kronfeld"'
print("My list 1 - ", myList1)
print("My list 2 - ", myList2)

# Fix err in way 2 - ' instead of " in f
iName = {"newName": "Maya"}
print(iName)
dNewName = f"{iName['newName']} {bName}"
print("Way2 new way printing name - ",dNewName)

# Print string and number
myString = "Kuku"
myNumber = 5
newString = myString + str(myNumber)
print("My new string - ", newString)



from csv_logics.logics import *

print("Option (a). add random user")
print("Option (b). sort random user")
print("Option (c). find user")
chooseOption = input("\nEnter corresponding option number : ")

if chooseOption == "a":
    addRandomEntries()
elif chooseOption == "b":
    sortData()
elif chooseOption == "c":
    findUser()
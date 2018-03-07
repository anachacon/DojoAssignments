#Write a program that takes a list and prints a message 
#for each element in the list, based on that element's 
#data type.
#Your program input will always be a list. For each item in 
#the list, test its data type. If the item is a string, concatenate 
#it onto a new string. If it is a number, add it to a running sum. 
#At the end of your program print the string, the number and an 
#analysis of what the list contains. 
#If it contains only one type, print that type, otherwise, print 'mixed'.

lst = [2,3,1,7,4,12]

myString = ""
myNumber = 0
dataType = "The list you entered "

for element in lst:
    if isinstance(element, str):
        myString += " " + element

    else:
         myNumber += element
  
if myNumber > 0 and len(myString) > 0:
    dataType += "is of mixed type."
elif myNumber > 0:
    dataType += "is of number type."
else:
    dataType += "is of string type."

print(dataType)
print("String: " + myString)
print("Sum: " + str(myNumber))

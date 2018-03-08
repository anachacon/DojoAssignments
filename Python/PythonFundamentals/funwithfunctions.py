#Odd/Even:
#Create a function called odd_even that counts from 1 to 2000. 
#As your loop executes have your program print the number of that 
#iteration and specify whether it's an odd or even number.

def odd_even():
    for i in range(1,2001):
        if i%2 != 0:
            print ("Number is "+ str(i) + ". This is an odd number.")
        else:
            print ("Number is "+str(i) + ". This is an even number.")
odd_even()

#Multiply:
#Create a function called 'multiply' that iterates through each value 
#in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value 
#has been multiplied by 5.

def multiply(myList, mult):
    myList2 = []
    for i in range (0, len(myList)):
        myList2.append(myList[i] * mult)
    return myList2
print(multiply([1,2,3], 6))

#Write a function that takes the multiply function call as an argument. 
#Your new function should return the multiplied list as a two-dimensional list. 
#Each internal list should contain the 1's times the number in the original list.

def layered_mult(arr):
    new_arr = []
    for i in range (0, len(arr)):
        newValue=[]
        for j in range (0, arr[i]):
            newValue.append('1')
        new_arr.append(newValue)
    return new_arr
x = (layered_mult ( multiply([1,2,3],5) ))
print (x)
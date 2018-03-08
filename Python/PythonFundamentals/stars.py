#Part I
#Create a function called draw_stars() that takes a list of numbers and prints out *.

def draw_stars(myList):
    for element in myList:
        myRow = ""
        for i in range (0,element):
            myRow += "*"
        print (myRow)

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

#Modify the function above. Allow a list containing integers and 
#strings to be passed to the draw_stars() function. When a string is passed, 
#instead of displaying *, display the first letter of the string according to 
# the example below. You may use the .lower() string method for this part.

def draw_stars_mod(myList):
    for i in range (0, len(myList)):
        myRow = ""
        if isinstance(myList[i], int):
            for x in range (0,myList[i]):
                myRow += "*"
            print (myRow)
        else:
            for x in range (0,len(myList[i])):
                myRow += (str(myList[i][0])).lower()
            print (myRow)
z = ["Isabel", 6, 1, 3, 5, 7, "Tommy"]
draw_stars_mod(z)
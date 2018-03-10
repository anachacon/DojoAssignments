myNumbers = [1,2,3,4,5,6,7,8,9,10,11,12]

for i in range (0, (len(myNumbers)+1)):
    myString = "x"
    if i == 0:
        for element in myNumbers:
            myString += "  "+str(element)
        print myString
    else:
        myString = str(i)
        for element in myNumbers:
            myString += "  "+str(element*i)
        print myString
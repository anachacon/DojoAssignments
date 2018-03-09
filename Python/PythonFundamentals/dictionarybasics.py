
myDictionary = {"name":"Isabel", "country":"Mexico", "age":"30", "language":"Javascript"}

def printDict(myDictionary):
    for key,value in myDictionary.items():
        print ("My "+key+" is "+value)

printDict(myDictionary)
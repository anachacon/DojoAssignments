#In this string: words = "It's thanksgiving day. It's my birthday, too!" 
#print the position of the first instance of the word "day". Then create 
#a new string where the word "day" is replaced with the word "month".

mystr = "It's thanksgiving day. It's my birthday,too!" 
position = mystr.find("day")
print (position)

newstring = mystr.replace("day", "month")
print (newstring)

#Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.

x = [2,54,-2,7,12,98]
print (min(x))
print (max(x))

#Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. 
#Now create a new list containing only the first and last values in the original list. 
#Your code should work for any list

x = ["hello",2,54,-2,7,12,98,"world"]
print (x[0])
print (x[len(x)-1])

newlist = [x[0], x[len(x)-1]]
print (newlist)


#Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. 
#Then, split your list in half. Push the list created from the first half to position 0 of the 
#list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. 
#Stick with it, this one is tough!

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
y = x[:int(len(x)/2)]
x = x[int(len(x)/2):]
x.insert(0, y)

print(x)

#Write a program that compares two lists and prints a 
#message depending on if the inputs are identical or not.
#Your program should be able to accept and compare two lists: 
#list_one and list_two. If both lists are identical print 
#"The lists are the same". If they are not identical print 
#"The lists are not the same."


list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
myString = "The lists are the same."

if len(list_one) == len(list_two):
    for i in range(0, len(list_one)):
        if list_one[i] == list_two[i]:
             continue
        else:
            myString = "The lists are not the same."
    print(myString)
else:
    print ("The lists are not the same.")
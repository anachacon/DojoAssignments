#Write a program that takes a list of strings and a string 
#containing a single character, and prints a new list of all 
#the strings containing that character.

word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []

for element in word_list:
    if element.find(char) >= 0:
        new_list.append(element)
print (new_list)
#Write a function that generates ten scores between 60 and 100.
#Each time a score is generated, your function should display what 
#the grade is for a particular score. Here is the grade table:

#Score: 60 - 69; Grade - D
#Score: 70 - 79; Grade - C
#Score: 80 - 89; Grade - B
#Score: 90 - 100; Grade - A

#Scores and Grades
#Score: 87; Your grade is B
#Score: 67; Your grade is D
#Score: 95; Your grade is A
#Score: 100; Your grade is A
#Score: 75; Your grade is C
#Score: 90; Your grade is A
#Score: 89; Your grade is B
#Score: 72; Your grade is C
#Score: 60; Your grade is D
#Score: 98; Your grade is A
#End of the program. Bye!

import random
print ("Scores and Grades")
for i in range (0,10):
    random_num = random.randint(60,100)
    if random_num < 70:
        print ("Score: "+str(random_num)+"; Your grade is D")
    elif random_num < 80:
        print ("Score: "+str(random_num)+"; Your grade is C")
    elif random_num < 90:
        print ("Score: "+str(random_num)+"; Your grade is B")
    else:
        print ("Score: "+str(random_num)+"; Your grade is A")
print ("End of the program. Bye!")

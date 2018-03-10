
def sqrt(x):
    counter = 0
    while counter*counter < x:
        counter += 1
    if counter*counter != x:
        return False
    else:
        return True

def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

for i in range(100,100000):
    if sqrt(i) == False and prime(i) == False:
        print "Foobar"
    elif sqrt(i) == True:
        print "Bar"
    else:
        print "Foo"
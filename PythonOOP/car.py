class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = price * .15
        else:
             self.tax = price * .12
        self.displayall()
    def displayall(self):
        print "Price: {} dlls".format(self.price)
        print "Speed: {} mph".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Mileage: {}".format(self.mileage)
        print "Tax: {}".format(self.tax)
        return ("The car price is: {}. The speed is: {}. The fuel is: ")

myCar = Car (100,100,100,100)

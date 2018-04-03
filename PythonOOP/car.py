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
        print(self.displayall())
    def displayall(self):
        return ("The car price is: {}. The speed is: {}. The fuel is: {}. The mileage is: {}. The tax is: {}.".format(self.price, self.speed, self.fuel, self.mileage, self.tax))

myCar = Car(10500,160,"Full",100)
myCar2 = Car(10500,160,"Empty",90)
myCar3 = Car(10500,160,"Almost Full",80)
myCar4 = Car(10500,160,"Full",70)
myCar5 = Car(10500,160,"Full",60)
myCar6 = Car(10500,160,"Full",50)
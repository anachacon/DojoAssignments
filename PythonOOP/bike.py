class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print "This bike costs {} dlls. Its maximum speed is {} miles. Total miles: {}.".format(self.price, self.max_speed, self.miles)
        return self
    def ride(self):
        self.miles = self.miles + 10
        return self
    def reverse(self):
        if self.miles >= 5:
            self.miles = self.miles - 5
        return self

myBike = Bike(150,40)
myBike.ride().ride().ride().reverse().displayinfo()

myBike2 = Bike(120,30)
myBike2 = myBike.ride().ride().reverse().reverse().displayinfo()

myBike3 = Bike(110,60)
myBike3 = myBike.reverse().reverse().reverse().displayinfo()
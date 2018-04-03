class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayinfo(self):
        print "This bike costs {} dlls. Its maximum speed is {} miles. Total miles: {}.".format(self.price, self.max_speed, self.miles)
        return self
    def ride(self):
        self.miles = self.miles + 10
        return self
    def reverse(self):
        self.miles = self.miles - 5
        return self
myBike = Bike(150,40,15)
myBike.ride().displayinfo()
myBike.reverse().displayinfo()
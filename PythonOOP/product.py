class Product(object):
    def __init__(self, price, item_name, weight, brand, status = "for sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
    def sell(self):
        self.status = "Sold"
        return self
    def addtax(self, tax):
        self.price = tax * self.price + self.price
        return self.price
    def displayinfo(self):
        print "Item name: {}".format(self.item_name)
        print "Item price: {}".format(self.price)
        print "Item brand: {}".format(self.brand)
        print "Item weight: {}".format(self.weight)
        print "Item status: {}".format(self.status)
        return self
    def returnitem(self,reason):
        defective = "defective"
        likenew = "like new"
        used = "opened"
        if reason.find(defective, 0, len(reason)) > -1:
            self.status = "Defective"
            self.price = 0
        elif reason.find(likenew, 0, len(reason)) > -1:
            self.status = "For Sale"
        elif reason.find(used, 0, len(reason)) > -1:
            self.status = "Used"
            self.price = self.price - (self.price * .20)
        return self

myProduct = Product (100, "Tea set", 20, "World Fair")
myProduct.returnitem("box was opened").displayinfo()
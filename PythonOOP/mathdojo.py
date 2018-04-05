class MathDojo(object):
    def __init__(self, total= 0):
        self.total = total
    def add(self, *args):
        subtotal = 0
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                for i in range(0, len(arg)):
                    subtotal += arg[i]
            else:
                subtotal += arg
        self.total += subtotal
        print self.total
        return self
    def subtract(self, *args):
        subtotal = 0
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                for i in range(0, len(arg)):
                    subtotal += arg[i]
            else:
                subtotal += arg
        self.total -= subtotal
        print self.total
        return self

md = MathDojo(10)
md.subtract(2,3,3)
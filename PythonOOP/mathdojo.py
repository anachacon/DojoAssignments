class MathDojo(object):
    def __init__(self, total= 0):
        self.total = total
    def add(self, arg1, *args):
        subtotal = 0
        for i in range(0, len(args)):
            subtotal += args[i]
        self.total += arg1 + subtotal
        return self
    def subtract(self, arg1, *args):
        subtotal = 0
        for i in range(0, len(args)):
            subtotal += args[i]
        self.total -= arg1 + subtotal
        print self.total
        return self

md = MathDojo(10)
md.subtract(2, 3,3)
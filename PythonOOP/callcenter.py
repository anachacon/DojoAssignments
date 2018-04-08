import datetime

class Call(object):
    def __init__(self, id, name, phone, time, reason):
        self.id = id
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason
    def display(self):
        print "Id: {}".format(self.id)
        print "Name: {}".format(self.name)
        print "Phone: {}".format(self.phone)
        print "Time: {}".format(self.time)
        print  "Reason: {}".format(self.reason)

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = 0
    def add(self, call):
        self.calls.append(call)
        self.queue += 1
        return self
    def remove(self, call):
        self.calls.remove(call)
    def info(self):
        for c in self.calls:
            c.display()
         
  
myCall = Call(123,"Isabel", "425-588-9517", datetime.datetime.now(), "Python breaking")
myCallCenter = CallCenter()
myCallCenter.add(myCall)
myCallCenter.remove(myCall)
myCallCenter.info()
import datetime

class Patient(object):
    ids = 0
    def __init__(self, name, allergies=[]):
        self.id = Patient.ids
        self.name = name
        self.allergies = allergies
        self.bed_number = 0
        Patient.ids += 1

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
    def add(self, patient):
        bednumber = len(self.patients) + 1
        if bednumber <= self.capacity:
            patient.bed_number = bednumber
            self.patients.append(patient)
            print("Patient admitted to bed number: {}".format(bednumber))
        else:
            print ("Hospital is at capacity")
        return self
    def discharge(self, patient):
        self.patients.remove(patient)
        patient.bed_number = 0
        return self
    def display(self):
        for p in self.patients:
            print p.id
            print p.name

myHospital = Hospital("Washington Hospital", 2)
patient = Patient("Isabel")
patient2 = Patient("Francisco")
myHospital.add(patient)
myHospital.add(patient2)
myHospital.discharge(patient2)

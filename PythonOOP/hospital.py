import datetime

class Patient(object):
    def __init__(self, id, name, allergies=[]):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = 0

class Hospital(object):
    def __init__(self, name, capacity, patients = []):
        self.patients = patients
        self.name = name
        self.capacity = capacity
    def add(self, patient):
        bednumber = len(self.patients) + 1
        if bednumber < self.capacity:
            patient.bed_number = bednumber
        else:
            print ("Hospital is at capacity")
        return self
    def discharge(self, patient):
        self.calls.remove(patient)
        patient.bed_number = 0
        return self

myHospital = Hospital("Washington Hospital", 2)
patient = Patient(123,"isabel")
myHospital.add(patient)


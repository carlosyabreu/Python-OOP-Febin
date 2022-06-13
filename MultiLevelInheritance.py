class MusicalInstruments:
    numberOfMajorKeys = 15
class TypeOfInstruments(MusicalInstruments):
    typeofWood = "Tonewood"
class Guitar(TypeOfInstruments, MusicalInstruments):
    def __init__(self):
        self.numberOfString = 6
        print(f"This guitar consists of {self.numberOfString} strings. It is made of {self.typeofWood} and can play {self.numberOfMajorKeys} keys.")

guitar = Guitar()

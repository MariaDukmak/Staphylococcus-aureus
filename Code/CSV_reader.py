import csv

class readit:
    def __init__(self, filepath, plot):
        self.filepath = filepath
        self.plot = plot
        self.__new__()

    def __new__(cls, filepath, plot):
     if plot is None:
        M = cls.readd(filepath)
        gr = cls.bereken_growthrate(M[1])
        maxcellem = cls.bereken_maxcellen(M)
        print(gr, maxcellem)
        return gr, maxcellem
     else:
         return cls.readd(filepath)

    def readd(filepath, lijst2=[], lijst =[]): # moet nog de time en de CFU/ml uit de lijst te verwijderen
        with open(str(filepath)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                 lijst.append(row[0])
                 lijst2.append(row[1])
            if " CFU/ml" in lijst2:
                 lijst2.remove(" CFU/ml")

            if "ï»¿time" in lijst:
                 lijst.remove("ï»¿time")

            tijd_lijst =[float(i) for i in lijst]
            cellen_lijst = [float(i) for i in lijst2]
            return [tijd_lijst, cellen_lijst]

    def bereken_growthrate( lijst):
        lijst3 = [float(lijst[item+1] - lijst[item]) for item in range(len(lijst)-1)]
        growthrate = max(lijst3)
        return growthrate

    def bereken_maxcellen( lijst):
        deltatijd = max(lijst[0])- min(lijst[0])
        deltacellen = max(lijst[1]) -min(lijst[1])
        return [deltatijd, deltacellen]


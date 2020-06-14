import csv

class readit:
    def __init__(self, filepath):
        self.filepath = filepath

    def verzamel(self, filepath):
        M = self.readd(filepath)
        gr = self.bereken_growthrate(M[1])
        maxcellem = self.bereken_maxcellen(M)
        print(gr, maxcellem)
        return gr, maxcellem

    def readd(self, filepath, lijst2=[], lijst =[]): # moet nog de time en de CFU/ml uit de lijst te verwijderen
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

    def bereken_growthrate(self, lijst):
        lijst3 = [float(lijst[item+1] - lijst[item]) for item in range(len(lijst)-1)]
        growthrate = max(lijst3)
        return growthrate

    def bereken_maxcellen(self, lijst):
        deltatijd = max(lijst[0])- min(lijst[0])
        deltacellen = max(lijst[1]) -min(lijst[1])
        return [deltatijd, deltacellen]

# if __name__ == "__main__":
#         mm = readit("C:/Users/marya/OneDrive/Bureaublad/xx-waardes.csv")
#         mm.verzamel("C:/Users/marya/OneDrive/Bureaublad/xx-waardes.csv")
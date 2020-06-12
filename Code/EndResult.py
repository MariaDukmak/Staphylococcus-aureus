
import numpy as np
from numpy import log as ln

from Code.JsonChecker import JsonChecker

"""Lag-fase: de periode die verloopt voordat de vermeerdering van de bacteriecellen begint;
logaritmische fase: de periode, waarin de feitelijke groei plaatsvindt, hierbij verdubbelt het aantal zich elke generatietijd
de stationaire fase: de periode, waarin het aantal levende cellen per ml constant blijft
afstervingsfase:de periode, waarin het aantal levende cellen per ml afneemt"""

#    s-aureus
 # van 6 tot 7 is lagfase
 #van 7.1 t/m 38 is logfase
 #van 38 t/m 48 is sss fase
 #van 48.1 is sterffase


class EndResult(JsonChecker):
    def __init__(self, bactName: str, temperature: float, pH: float, endTime: float, typeG: int):
        super().__init__(bactName, temperature, pH, endTime, typeG)


    def logistic(self, bact_name:str, time:float):

          """"c= is de beperkende factor, kan tempratuur, ph of max aantaal cellen zijn
            b= is de groeifactor
            a = is de beginwaarde"""""

          groeisFcator = self.read_json(self, bact_name, "gr")
          beperkendeFactor = self.read_json(self, bact_name, "br")
          beginWaarde = beperkendeFactor[0] - 1
          list = []
          for t in range(0, int(time) + 1):
              list.append(beperkendeFactor[0] / (1 + beginWaarde * np.exp(-groeisFcator[0] * t)))
              #xx=  np.exp((b[0])-(c[0]*time))
              #list.append(a/(1 + xx))# komt van de bron vandaan
          return np.array(list)


    def temp_logistic(self, bact_name: str, temp_check:list):
        """hier moet de grafiek van de growth getekend, in verglijking met de tempratuur verandering per uur
             begint bij de min temp en eindigt bij de max """
        list = []
        beginRange = 0
        eindRange = 0
        groeisFactor = self.read_json(self, bact_name, "gr")

        if temp_check is not None:
            if len(temp_check) == 3:
                beginRange = temp_check[0]
                eindRange = temp_check[2] + 1
                # optimum?? moeten iets ermee doen
            elif len(temp_check) == 2:
                beginRange = temp_check[0]
                eindRange = temp_check[1] + 1

            elif len(temp_check) == 1:
                beginRange = temp_check[0]
                eindRange = temp_check[0] + 1

        begingValue = eindRange -1

        for time in range(int(beginRange), int(eindRange+1)):
            if list:
                if list[-1] != eindRange:
                    list.append(eindRange / (1 + begingValue * np.exp(-groeisFactor[0] * time)))
                    #list.append(eindRange/(1+np.exp((4*groeisFactor/eindRange))))
                else:
                    print(np.array(list))
                    return np.array(list)
            else:
                list.append(eindRange / (1 + begingValue * np.exp(-groeisFactor[0] * time)))


    def log_growth(self, bact_name, time):
        """log N -log N0 = growth rate /2.303(t-t0)"""
        lijst= []
        logN0 = np.log(2.05e6)
        growthrate = self.read_json(self, bact_name, "gr")
        beperkendeFactor = self.read_json(self, bact_name, "br")
        lijst.append(logN0)
        for t in range(0, int(time)+1):
             logN = (growthrate[0]/2.303*(t)) + logN0
             if logN < beperkendeFactor[0]:
                lijst.append(logN)
             else:
                 lijst.append(beperkendeFactor[0])
        print(lijst)
        M = max(lijst) - min(lijst)
        print(M)

        return np.array(lijst)

    def Gompertz(self, bact_input, t, b, c):  # TODO: maak in versie 2 de Gompertz af
        """the zwietering modification w(t) = A exp (-exp (e.kz/A). (Tlog - t)+1))"""
        pass

    @classmethod
    def growth_endresult(self, bact_input, tem_input,ph_input, end_time, typeG):
        temp_check = self.values_check(self, bact_input, tem_input, "temp")
        ph_check = self.values_check(self, bact_input, ph_input, "ph")
        if (temp_check and ph_check) is not None:
            if typeG == 1:
                antwoord = self.logistic(self, bact_input, end_time)
            if typeG ==2:
                antwoord = self.temp_logistic(self, bact_input, temp_check)
            if typeG ==3:
                antwoord = self.log_growth(self,bact_input, end_time)
                #x = self.Gomptz()
            print("we got this temp after the value check ", temp_check)
            print("we got this ph after the value check ", ph_check)
            return antwoord
        else:
            raise ValueError("incorrect type of value was entered")



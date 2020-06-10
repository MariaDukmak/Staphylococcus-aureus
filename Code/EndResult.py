import numpy as np

from Code.JsonChecker import JsonChecker


#    s-aureus

class EndResult(JsonChecker):
    def __init__(self, bactName: str, temperature: float, pH: float, startTime: int, endTime: int, typeG: int):
        super().__init__(bactName, temperature, pH, startTime, endTime, typeG)

    def logistic(self, bactName:str, time: list, cFactor:list):
        # cFactor is the factor that could change the growth rate

        """c is the max : 1000000
        initial value: we start at 1 so, c/(a+1)= 1 , 1000/(1+a)=1 , a = 999
        the growth rate: b = 2 -> *could  changes with temperature and pH*
        time: we start at 0 end at 10 hours"""

        b = self.read_json(self, bactName, "gr")
        c = self.read_json(self, bactName, "br")
        a = c[0]-1

        # hier moet er goede getallen in komen + dat in de loop van de tijd moet de b wel ++ or --
        if len(cFactor) == 1:
            b[0] = b[0]/0.5
        if len(cFactor) == 2:
            b[0] = b[0]*2
        if len(cFactor) == 3:
            b = b[0] * 2.2
        list = []

        for time in range(time[0], time[1] + 1):
            list.append(c[0] / (1+a * np.exp(-b[0]*time)))
            #list.append(float(a)/(1.0+ np.exp(float(b[0])-(c[0]*time))))# komt van de bron vandaan
        return np.array(list)


    def Gompertz(self, bact_input, t, b,  c): # TODO: maak in versie 2 de Gompertz af
        """the zwietering modification w(t) = A exp (-exp (e.kz/A). (Tlog - t)+1))"""
        pass


    @classmethod
    def growth_endresult(self, bact_input, tem_input,ph_input,  start_time, end_time, typeG):
        temp_check = self.values_check(self, bact_input, tem_input, "temp")
        ph_check = self.values_check(self, bact_input, ph_input, "ph")
        if (temp_check and ph_check) is not None:
            if typeG == 1:
                antwoord = self.logistic(self, bact_input, [start_time, end_time], temp_check)
            #if typeG == 2:
                #x = self.Gomptz()
            print("we got this temp after the value check ", temp_check)
            print("we got this ph after the value check ", ph_check)
            return antwoord
        else:
            raise ValueError("incorrect type of value was entered")


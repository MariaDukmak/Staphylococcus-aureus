import json

import numpy as np

from Code.InputVrager import Inputs


#    s-aureus


class Endresult(Inputs):
    def __init__(self, bacteriaName: str, temperature: float, pH: float, startTime: int, endTime: int, typeG: int):
        super().__init__(bacteriaName, temperature, pH, startTime, endTime, typeG)

    def json_lezen(self, b: str, item: str):
        try:
            with open(b + ".json", "r") as f:
                info = json.load(f)
                optimum_item = info["env-info"][item][item]
                max_item = info["env-info"][item]["max"]
                min_item = info["env-info"][item]["min"]
                return [optimum_item, max_item, min_item]
        except KeyError as e:
            return [optimum_item]

    def waardes_check(self, bestand: str, inputWaarde: float, item: str):
        values = self.json_lezen(self, bestand, item)
        if (values[2] <= inputWaarde <= values[1]) or (inputWaarde == values[0]):
            return[inputWaarde, values[1]]
        else: # TODO: laat de error op een andere manier en niet alles kapot maken
            raise ValueError("incorrect type of value was entered {}".format(inputWaarde))

    def my_logstic(self, bact_input: str, t: list, b: str, c: str):
        """c is the max : 1000000
        initial value: we start at 1 so, c/(a+1)= 1 , 1000/(1+a)=1 , a = 999
        the growth rate: b = 2
        time: we start at 0 end at 10 hours"""

        b = self.json_lezen(self, bact_input, b)
        c = self.json_lezen(self, bact_input, c)
        a = c[0]-1
        lijst = []
        for time in range(t[0], t[1]+1):
            lijst.append(c[0] / (1+a * np.exp(-b[0]*time)))
            # lijst.append(float(a)/(1.0+ np.exp(float(b[0])-(c[0]*time)))) komt van de bron vandaan
        return np.array(lijst)
        # return lambda t :[(c / (1+a * np.exp(-b[0]*time)) for time in range(t[0], t[1]+1))]

    def Gomptz(self, bact_input, t, b,  c ): # TODO: maak in versie 2 de Gompertz af
        """the zwietering modification w(t) = A exp (-exp (e.kz/A). (Tlog - t)+1))"""
        pass

    @classmethod
    def growth_endresult(self, bact_input, start_time, end_time, tem_input, ph_input,  typeG):
        temp = self.waardes_check(self, bact_input, tem_input, "temp")
        phh = self.waardes_check(self, bact_input, ph_input, "ph")
        if (temp and phh) is not None:
            if typeG == 1:
                x = self.my_logstic(self, bact_input, [start_time, end_time], "gr", "br")
            #if typeG == 2:
                #x = self.Gomptz()
            print("we got this its waarde check ", temp)
            print("we got this its waarde check ", phh)
            return x


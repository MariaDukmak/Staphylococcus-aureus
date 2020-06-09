import numpy as np

from Code.JsonChecker import JsonChecker


#    s-aureus


class EndResult( JsonChecker):
    def __init__(self, bacteriaName: str, temperature: float, pH: float, startTime: int, endTime: int, typeG: int):
        super().__init__(bacteriaName, temperature, pH, startTime, endTime, typeG)

    def logistic(self, bact_input: str, t: list, b: str, c: str, bb:list):
        """c is the max : 1000000
        initial value: we start at 1 so, c/(a+1)= 1 , 1000/(1+a)=1 , a = 999
        the growth rate: b = 2
        time: we start at 0 end at 10 hours"""

        b = self.json_lezen(self, bact_input, b)
        c = self.json_lezen(self, bact_input, c)
        a = c[0]-1

        #hier moet er goede getallen in komen + dat in de loop van de tijd moet de b wel ++ or --
        if len(bb)== 1:
            b[0] = b[0]/0.5
        if len(bb) == 2:
            b[0] = b[0]*2
        if len(bb) ==3:
            b = b[0]* 2.2
        lijst = []
        for time in range(t[0], t[1]+1):
            lijst.append(c[0] / (1+a * np.exp(-b[0]*time)))
            # lijst.append(float(a)/(1.0+ np.exp(float(b[0])-(c[0]*time)))) komt van de bron vandaan
        return np.array(lijst)


    def Gompertz(self, bact_input, t, b,  c): # TODO: maak in versie 2 de Gompertz af
        """the zwietering modification w(t) = A exp (-exp (e.kz/A). (Tlog - t)+1))"""
        pass


    @classmethod
    def growth_endresult(self, bact_input, start_time, end_time, tem_input, ph_input,  typeG):
        temp = self.waardes_check(self, bact_input, tem_input, "temp")
        phh = self.waardes_check(self, bact_input, ph_input, "ph")
        if (temp and phh) is not None:
            if typeG == 1:
                x = self.logistic(self, bact_input, [start_time, end_time], "gr", "br", temp)
            #if typeG == 2:
                #x = self.Gomptz()
            print("we got this its waarde check ", temp)
            print("we got this its waarde check ", phh)
            return x
        else:
            raise ValueError(f"incorrect type of value was entered {temp + phh}")


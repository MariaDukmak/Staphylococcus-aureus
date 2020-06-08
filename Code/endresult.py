import json
import numpy as np
from Code.inputs import Inputs
#    s-aureus


class Endresult(Inputs):
    def __init__(self, bact_input, tem_input, ph_input, start_time, end_time):
        super().__init__(bact_input, tem_input, ph_input, start_time, end_time)

    def json_lezen(self, b, item):
        try:
            with open(b + ".json", "r") as f:
                info = json.load(f)
                optimum_item = info["env-info"][item][item]
                max_item = info["env-info"][item]["max"]
                min_item = info["env-info"][item]["min"]
                return [optimum_item, max_item, min_item]
        except KeyError as e:
            return [optimum_item]

    def waardes_check(self, b, t, w):
        values = self.json_lezen(self, b, w)
        if (values[2] <= t <= values[1]) or (t == values[0]):
            return [t, values[1]]
        else:
            raise ValueError("value error")

    def my_logstic(self, bact_input, t, b, c):

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
        return np.array(lijst)
        # return lambda t :[(c / (1+a * np.exp(-b[0]*time)) for time in range(t[0], t[1]+1))]

    @classmethod
    def growth_endresult(self, bact_input, start_time, end_time, tem_input, ph_input):
        temp = self.waardes_check(self, bact_input, tem_input, "temp")
        phh = self.waardes_check(self, bact_input, ph_input, "ph")
        x = self.my_logstic(self, bact_input, [start_time, end_time], "gr", "br")
        print(x)
        print("we got this its waarde check ", temp)
        print("we got this its waarde check ", phh)
        return x


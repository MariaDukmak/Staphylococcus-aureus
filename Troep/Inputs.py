import json

import matplotlib.pyplot as plt
import numpy as np
from click._compat import raw_input


class Info_json(): #werkt
    def __init__(self, file_name, user_input):
        super().__init__(file_name, user_input)

    def find(self, file_name, user_input):
        try:
            with open(file_name + ".json", "r") as f:
                info = json.load(f)
                optimum_item = info["env-info"][user_input][user_input]
                max_item = info["env-info"][user_input]["max"]
                min_item = info["env-info"][user_input]["min"]
                print(optimum_item, max_item, max_item)
                return [optimum_item, max_item, min_item]

        except ValueError as e:
            return [optimum_item]

class Logstic:
    def __init__(self, t, a, b, c ):
        self.t = t
        self.a = a
        self.b = b
        self.c = c
    @classmethod
    def bereken(self):
        lijst = []
        print(self.t[0], self.t[1])
        for time in range(self.t[0], self.t[1] + 1):
            lijst.append(self.c / (1 + self.a * np.exp(-self.b * time)))
        return np.array(lijst)

class Values_check(Info_json): #TODO: fix the connection between the classes
    def __init__(self, file_name, user_input, t):
        super().__init__(file_name, user_input, t)
        self.file_name = file_name
        self.user_input = user_input
        self.t = t

    def check(self):
        values = Info_json(self.file_name, self.user_input )
        if (values[2] <= self.t <= values[1]) or (self.t == values[0]):
            return [self.t, values[1]]
        else:
            print("Deze  is ongeldig in de json bestand van de bactrie")


class growth(Logstic, Values_check):
    def __init__(self, bact_name, temp, ph, start_time, end_time ):
        try:
            self.bact_name = bact_name
            self.temp = temp
            self.ph = ph
            self.start_time = start_time
            self.end_time = end_time
        except ValueError as e:
            print("uncorrected", e)

        #tempp = Values_check(bact_name, temp, "temp")
        #phh = Values_check( bact_name, ph, "ph")
    @classmethod
    def result(self):
        x = Logstic([start_time, end_time], 9999999999999999999999999999, 2, 10000000000000000000000000000)
        return x


class Inputs(growth):
    def __init__(self, bact_name, temp, ph, start_time, end_time ):
        try:
            self.bact_name = bact_name
            self.temp = temp
            self.ph = ph
            self.start_time = start_time
            self.end_time = end_time
        except ValueError as e:
            print("uncorrected", e)

    @property
    def get_name(self):
        return self.bact_name

    @property
    def get_temp(self):
        return self.temp

    @property
    def get_ph(self):
        return self.ph

    @property
    def get_start_time(self):
        return self.start_time

    @property
    def get_end_time(self):
        return self.end_time

    def tostring(self):
        print("fuck", self.result())


bact_name = raw_input('Welke bact?')
temp = int(raw_input('Wat is de temp? '))
ph = int(raw_input('Wat is de ph waarde?'))
start_time = int(raw_input('Wat is de begintijd? '))
end_time = int(raw_input('Wat is de eindtijd? '))


er = Inputs( bact_name, temp, ph, start_time, end_time)
print(er.bact_name)
print(er.get_end_time)
print(er.tostring())


class plot_that(growth):
    def __init__(self, bact_name,start_time, end_time, temp, ph):
        super().__init__(bact_name, start_time, end_time, temp, ph)

    x= np.linspace(start_time, end_time, 11)
    print(x)
    y = growth.result()
    print(y)
    plt.plot(x, y)
    plt.show()


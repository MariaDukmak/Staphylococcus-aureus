import matplotlib.pyplot as plt
import numpy as np

from Code.EndResult import EndResult
from Code.InputVrager import Inputs, endTime, temperatureInput, pHInput, bacteriaNameInput, typeG


class Plots(Inputs): # s-aureus
    def __init__(self, bacteriaName: str, temperature: float, pH: float, startTime: int, endTime: int, typeG: int):
        super().__init__(bacteriaName, temperature, pH, startTime, endTime, typeG)

    def plot_dingen(self):

        y = EndResult.growth_endresult(bacteriaNameInput, temperatureInput, pHInput, endTime, typeG)
        x = np.linspace(0, len(y), (len(y)))
        plt.plot(x, y)
        plt.xlabel("tijd in uur")
        plt.ylabel("groei per uur ")
        plt.show()


test = Plots(Inputs.get_name, Inputs.get_temp, Inputs.get_ph, Inputs.get_startTime, Inputs.get_endTime, Inputs.get_typeG)
test.plot_dingen()

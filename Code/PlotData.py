import matplotlib.pyplot as plt
import numpy as np

from Code.EndResult import Endresult
from Code.InputVrager import Inputs, startTime, endTime, temperatureInput, pHInput, bacteriaNameInput, typeG


class Plots(Inputs): # s-aureus
    def __init__(self, bacteriaName: str, temperature: float, pH: float, startTime: int, endTime: int, typeG: int):
        super().__init__(bacteriaName, temperature, pH, startTime, endTime, typeG)

    def plot_dingen(self):
        x = np.linspace(startTime, endTime, endTime+1)  # dit moet je fixen dat ie meer dan 10 indexes kan
        y = Endresult.growth_endresult(bacteriaNameInput, startTime, endTime, temperatureInput, pHInput, typeG)
        plt.plot(x, y)
        plt.xlabel("tijd in uur")
        plt.ylabel("groei per uur ")
        plt.show()


test = Plots(Inputs.get_name, Inputs.get_temp, Inputs.get_ph, Inputs.get_startTime, Inputs.get_endTime, Inputs.get_typeG)
test.plot_dingen()


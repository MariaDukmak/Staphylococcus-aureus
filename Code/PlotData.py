import matplotlib.pyplot as plt
import numpy as np

from Code.EndResult import Endresult
from Code.InputVrager import Inputs, startTime, endTime, temperatureInput, pHInput, bacteriaNameInput, typeG


class Plots(Inputs):  # s-aureus
    def __init__(self, bacteriaNameInput: str, temperatureInput: float, pHInput: float, startTime: int, endTime: int,
                 typeG: int):
        super().__init__(bacteriaNameInput, temperatureInput, pHInput, startTime, endTime, typeG)
        self.plot_dingen()

    def plot_dingen(self):
        x = np.linspace(startTime, endTime, (endTime - startTime + 1))
        y = Endresult.growth_endresult(bacteriaNameInput, startTime, endTime, temperatureInput, pHInput, typeG)
        plt.plot(x, y)
        plt.xlabel("tijd in uur")
        plt.ylabel("groei per uur ")
        plt.show()


if __name__ == "__main__":
    test = Plots(bacteriaNameInput, temperatureInput, pHInput, startTime, endTime, typeG)

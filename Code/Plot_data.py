import matplotlib.pyplot as plt
import numpy as np

from Code.endresult import Endresult
from Code.inputs import Inputs, start_time, end_time, tem_input, ph_input, bact_input


class Plots(Inputs): # s-aureus
    def __init__(self, bact_input, tem_input, ph_input, start_time, end_time):
        super().__init__(bact_input, tem_input, ph_input, start_time, end_time)

    def plot_dingen(self):
        x = np.linspace(start_time, end_time, 11)  # dit moet je fixen dat ie meer dan 10 indexes kan
        y = Endresult.growth_endresult(bact_input, start_time, end_time, tem_input, ph_input)
        plt.plot(x, y)
        plt.show()


test = Plots(Inputs.get_name, Inputs.get_temp, Inputs.get_ph, Inputs.get_start_time, Inputs.get_end_time)
test.plot_dingen()


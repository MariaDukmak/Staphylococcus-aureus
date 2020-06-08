import matplotlib.pyplot as plt
import numpy as np

from Code.endresult import endresult
from Code.inputs import inputs, start_time, end_time, tem_input, ph_input, bact_input


class Plots(inputs): # s-aureus
    def __init__(self, bact_input, tem_input, ph_input, start_time, end_time):
        super().__init__(bact_input, tem_input, ph_input, start_time, end_time)

    def plot_dingen(self):
        x = np.linspace(start_time, end_time, 11)  # dit moet je fixen dat ie meer dan 10 indexes kan
        y = endresult.growth_endresult(bact_input, start_time, end_time, tem_input, ph_input)
        plt.plot(x, y)
        plt.show()


test = Plots(inputs.get_name, inputs.get_temp, inputs.get_ph, inputs.get_start_time, inputs.get_end_time)
test.plot_dingen()

# bact_name = ip.bact_input
# start_time = ip.start_time
# nd_time = ip.end_time
# tem_input = ip.tem_input
# ph_input = ip.ph_input

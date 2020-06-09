from tkinter import *

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from Code.EndResult import EndResult
from Code.InputVrager import startTime, endTime, temperatureInput, pHInput, bacteriaNameInput, typeG


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Growth model")
        self.minsize(640,400)
        self.configure(background ='gray')
        self.mat()
    def mat(self):
        f = Figure(figsize= (5,5), dpi= 100 )
        a =f.add_subplot(111)
        x = np.linspace(startTime, endTime, (endTime - startTime + 1))
        y = EndResult.growth_endresult(bacteriaNameInput, startTime, endTime, temperatureInput, pHInput, typeG)
        a.plot(x,y)
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side = BOTTOM, fill= BOTH, expand= True)


if __name__ == '__main__':
    root = Root()
    root.mainloop()


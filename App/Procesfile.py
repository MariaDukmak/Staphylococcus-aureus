import tkinter as tk
from tkinter import filedialog

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from Code.CSV_reader import readit


class ProcesFile(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frameBovenPlotGraph = tk.Frame(self, bg="#49A")
        tk.Frame.configure(self, bg="#49A")
        titel1= tk.Label(frameBovenPlotGraph,text="Bereken constanten van een dataset",  font='Arial 18 bold', bg="#49A")
        infoUitprinten = tk.Label(frameBovenPlotGraph,
                                  text="\n\n\nUpload je csv bestand eerst \n "
                                       "Daarna kies de constanten die je wilt laten uitrekenen\n\n\n",
                                  font='Arial 18 ', bg="#49A")
        buttonTerugNaarHome = tk.Button(frameBovenPlotGraph, text="Terug naar de homepagina", height=5, width=23,
                                        fg="#49A",
                                        bg="white", font='Arial 10', command=lambda: controller.showFrame("MainPage"))
        buttoChoosFile = tk.Button(frameBovenPlotGraph, text="Selecteer een bestand", height=5, width=23,
                                        fg="#49A",
                                        bg="white", font='Arial 10', command=lambda: ProcesFile.file(self))

        buttonPlotGrafiekFile = tk.Button(frameBovenPlotGraph, text="Klik hier om het grafiek \nte laten tekenen", height=5, width=23,
                                        fg="#49A",
                                        bg="white", font='Arial 10', command=lambda: plot_file())

        printBerekeningenButton = tk.Button(frameBovenPlotGraph, text="Laat de antwoord zien", height=5, width=23,
                                        fg="#49A", bg="white", font='Arial 10', command= lambda:print_uitkomsten())

        statusbar = tk.Label(self, bd=1, relief=tk.SUNKEN, padx=10, pady=20, bg="light blue",
                             text="Copyright© Marya Dukmak")

        var = tk.IntVar()
        var2 = tk.IntVar()
        antwoordShowLabel = tk.Label(frameBovenPlotGraph, font='Arial 16 ', bg="#49A", width=40, text='')
        antwoordShowLabel2 = tk.Label(frameBovenPlotGraph, font='Arial 16 ', bg="#49A", width=40, text='')


        checkButtton = tk.Checkbutton(frameBovenPlotGraph, text= "Growth rate", variable = var, font='Arial 16 ', bg="#49A" )
        checkButtton2 = tk.Checkbutton(frameBovenPlotGraph, text=" Max aantaal gemaakte cellen", variable=var2, font='Arial 16 ', bg="#49A")

        frameBovenPlotGraph.pack(side=tk.LEFT, fill=tk.BOTH)
        buttonTerugNaarHome.grid(row=60, column=0)
        buttoChoosFile.grid(row=50, column=0, )
        titel1.grid(row = 0 , column= 0)
        infoUitprinten.grid(row=4, column=0, sticky = "w")
        checkButtton.grid(row=20, column=0, sticky = "w")
        checkButtton2.grid(row=25, column=0, sticky = "w")
        antwoordShowLabel.grid(row=30, column=0)
        antwoordShowLabel2.grid(row=35, column=0)
        buttonPlotGrafiekFile.grid(row=60, column=1)
        printBerekeningenButton.grid(row=50, column=1)
        statusbar.pack(side=tk.BOTTOM, fill=tk.BOTH)

        def print_uitkomsten():
            answer = readit(self.fileDai)
            answeeer = answer.verzamel(self.fileDai)

            if var.get() == 1:
                antwoordShowLabel.config(text = f"De growth rate is "+str(answeeer[0]))
            if var2.get() == 1:
                antwoordShowLabel2.config(text= " De max aantaal gemaakte cellen is " + str(answeeer[1][1]))

        def plot_file():
            xeny =readit(self.fileDai)
            xenyy = xeny.readd(self.fileDai)
            x, y = xenyy[0], xenyy[1]
            f = Figure(figsize=(5, 5), dpi=100)
            f.suptitle('Growth Curve', fontsize=14, fontweight='bold')
            a = f.add_subplot(111)
            a.set_ylabel('Groei in CFU/ml')
            a.set_xlabel('Tijd in uur')
            a.plot(np.array(x),np.array(y))
            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()

            canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def file(self):
        self.fileDai= filedialog.askopenfilename(initialdir = "/Bureaublad",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
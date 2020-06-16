#  Copyright (c) 2020 Marya Dukmak
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import tkinter as tk
from tkinter import filedialog

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from Code.CSV_reader import readit


class ProcesFile(tk.Frame):
    """In dit klasse kan de gebruiker een csv file uploaden en de progranmmma een bepaalde constanten laten uitrekenen
      die de gebruiker zelf kan kiezen, er kan ook het grafiek van de csv bestand laten aantoenen"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frameBovenPlotGraph = tk.Frame(self, bg="#49A")
        tk.Frame.configure(self, bg="#49A")

        titel = tk.Label(frameBovenPlotGraph,text="Bereken constanten van een dataset",  font='Arial 18 bold', bg="#49A")
        infoUitprinten = tk.Label(frameBovenPlotGraph,
                                  text="\n\n\nUpload je csv bestand eerst \n "
                                       "Daarna kies de constanten die je wilt laten uitrekenen\n\n\n",
                                  font='Arial 18 ', bg="#49A")
        buttonTerugNaarHome = tk.Button(frameBovenPlotGraph, text="Terug naar de homepagina", height=5, width=23,
                                        fg="#49A",
                                        bg="white", font='Arial 10', command=lambda: controller.showFrame("MainPage"))
        buttoChoosFile = tk.Button(frameBovenPlotGraph, text="Selecteer een bestand", height=5, width=23,
                                        fg="#49A", bg="white", font='Arial 10', command=lambda: ProcesFile.file(self))

        buttonPlotGrafiekFile = tk.Button(frameBovenPlotGraph, text="Klik hier om het grafiek \nte laten tekenen", height=5,
                                          width=23, fg="#49A", bg="white", font='Arial 10', command=lambda: plot_file())

        buttonPrintBerekeningen = tk.Button(frameBovenPlotGraph, text="Laat de antwoord zien", height=5, width=23,
                                        fg="#49A", bg="white", font='Arial 10', command= lambda:print_uitkomsten())

        statusbar = tk.Label(self, bd=1, relief=tk.SUNKEN, padx=10, pady=20, bg="light blue",text="Copyright© Marya Dukmak")

        antwoordShowLabel = tk.Label(frameBovenPlotGraph, font='Arial 16 ', bg="#49A", width=40, text='')
        antwoordShowLabel2 = tk.Label(frameBovenPlotGraph, font='Arial 16 ', bg="#49A", width=40, text='')

        # variabel voor de checkbuttons om te kijken of ze geselecteerd
        var = tk.IntVar()
        var2 = tk.IntVar()
        # hier kan de gebruiker de opties kiezen die hij wil laten berekenen
        checkButtton = tk.Checkbutton(frameBovenPlotGraph, text= "Growth rate", variable = var, font='Arial 16 ', bg="#49A" )
        checkButtton2 = tk.Checkbutton(frameBovenPlotGraph, text="Max aantaal gemaakte cellen", variable=var2, font='Arial 16',
                                       bg="#49A")

        # Hier wordt alles in de schrem aangetood
        frameBovenPlotGraph.pack(side=tk.LEFT, fill=tk.BOTH)
        buttonTerugNaarHome.grid(row=60, column=0)
        buttoChoosFile.grid(row=50, column=0, )
        titel.grid(row = 0 , column= 0)
        infoUitprinten.grid(row=4, column=0, sticky = "w")
        checkButtton.grid(row=20, column=0, sticky = "w")
        checkButtton2.grid(row=25, column=0, sticky = "w")
        antwoordShowLabel.grid(row=30, column=0)
        antwoordShowLabel2.grid(row=35, column=0)
        buttonPlotGrafiekFile.grid(row=60, column=1)
        buttonPrintBerekeningen.grid(row=50, column=1)
        statusbar.pack(side=tk.BOTTOM, fill=tk.BOTH)

        def print_uitkomsten():
            # hier wordt de classes aangroepen die de growth rate en/de max aantaal cellen kan uitrekenen
            # en vervolgens aangetoond
            answer = readit(self.fileDai)
            eind_answer = answer.verzamel(self.fileDai)

            if var.get() == 1: # als de growth rate wordt gekozen
                antwoordShowLabel.config(text = f"De growth rate is "+str(eind_answer[0]))
            if var2.get() == 1: # als de max aantaal cellen wordt gekozen
                antwoordShowLabel2.config(text= " De max aantaal gemaakte cellen is " + str(eind_answer[1][1]))

        def plot_file():
            # hier kunnnen de data van de file in een grafiek getekend worden
            try:
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
            except Exception as e:
                infoUitprinten = tk.Label(frameBovenPlotGraph,
                                          text="Je hebt 1 of meerdere inputs verkeerd ingevoerd, probeer het opnieuw",
                                          font='Arial 16 ', bg="#49A")
                infoUitprinten.grid(row=25, column=0)

    def file(self):
        # hierdoor kan de gebruiker een file uploaden
        self.fileDai= filedialog.askopenfilename(initialdir = "/Bureaublad",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
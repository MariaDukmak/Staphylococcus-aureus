import tkinter as tk

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from Code.EndResult import EndResult


class PlotGraph(tk.Frame):
    """In dit klass worden de inputs dir nodig voor het bereken van de intervals en het tekenen van het grafiek gevraagd
       verolgens wordt de gerafiek aan de rechtere kant van de scherm geschowed, hier ook maak ik gebruik van de try,
       except voor het geval dat de gebruiker een verkerede type in toetst """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frameBovenPlotGraph = tk.Frame(self, bg="#49A")

        titel = tk.Label(frameBovenPlotGraph, text="Grafiek tekenen", fg='black', bg= "#49A", font='Arial 35 bold')
        tk.Frame.configure(self, bg="#49A")

        buttonTerugNaarHome=tk.Button(frameBovenPlotGraph, text="Terug naar de homepagina",height=5,width=23, fg="#49A",
                             bg="white", font='Arial 10', command=lambda: controller.showFrame("MainPage"))

        buttonNaarInfoBact =tk.Button(frameBovenPlotGraph, text="Inforamatie de bacterie",height=5, width=23, fg="#49A",
                             bg="white", font='Arial 10', command=lambda: controller.showFrame("InfoBact"))

        bactLab= tk.Label(frameBovenPlotGraph,text="Welke bacterie?", font='Arial 18', bg="#49A")
        tempLab = tk.Label(frameBovenPlotGraph, text="Wat is het tempratuur?",font='Arial 18', bg="#49A")
        pHLab= tk.Label(frameBovenPlotGraph,text="Wat is de PH grade?",font='Arial 18', bg="#49A")
        tim2Lab= tk.Label(frameBovenPlotGraph, text="Wat is de eindtijd in uren?",font='Arial 18', bg="#49A")
        grafiekLab = tk.Label(frameBovenPlotGraph, text="Kies de soort berekneing \n 1.logstic met max aantaal cellen"
                                                        "\n als beperkende factor \n 2.logstic met max tempratuur \nals "
                                                        "beperkende factor\n 3.log groei met 4 faces, lag, log, \nstationaire en sterffases",
                                                        font='Arial 16', bg="#49A")
        statusbar = tk.Label(self, bd=1, relief=tk.SUNKEN, padx=10, pady=20, bg="light blue",
                             text="Copyright© Marya Dukmak")
        legeLabel = tk.Label(frameBovenPlotGraph, bg="#49A")
        bactEN = tk.Entry(frameBovenPlotGraph)
        tempEN = tk.Entry(frameBovenPlotGraph)
        phEN = tk.Entry(frameBovenPlotGraph)
        tim2EN = tk.Entry(frameBovenPlotGraph)
        grafiekEN = tk.Entry(frameBovenPlotGraph)
        try:
            laatGrafiekZien=tk.Button(frameBovenPlotGraph, text="Laat het grafiek zien!", height=5, width=23, fg="#49A",
                                        bg="white", font='Arial 10',command=lambda: PlotGrafiek(str(bactEN.get()),
                                        int(tempEN.get()), int(phEN.get()),int(tim2EN.get()), int(grafiekEN.get())))
        except ValueError:
            infoUitprinten = tk.Label(frameBovenPlotGraph,
                                      text="Je hebt 1 of meerdere inputs verkeerd ingevoerd,\n probeer het opnieuw",
                                      font='Arial 16 ', bg="#49A")
            infoUitprinten.grid (row = 40, column = 0)

        def PlotGrafiek(bacteriaName, temperature, pH, endTime, typeG):

                try:
                    y = EndResult.growth_endresult(bacteriaName, temperature, pH, endTime, typeG)
                    x = np.linspace(0, len(y), (len(y)))
                    f = Figure(figsize=(5, 5), dpi=100)
                    f.suptitle('Growth Curve', fontsize=14, fontweight='bold')
                    a = f.add_subplot(111)
                    #a.set_title('axes title')
                    a.set_ylabel('Groei in CFU/ml')
                    if typeG == 1 or typeG == 3:
                        a.set_xlabel('Tijd in uur')
                    else:
                        a.set_xlabel("Temperature in celsius")
                    a.plot(x, y)
                    canvas = FigureCanvasTkAgg(f, self)
                    canvas.draw()

                    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

                    toolbar = NavigationToolbar2Tk(canvas, self)
                    toolbar.update()
                    canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

                except ValueError:
                    infoUitprinten = tk.Label(frameBovenPlotGraph,
                                              text="Je hebt 1 of meerdere inputs verkeerd ingevoerd, probeer het opnieuw",
                                              font='Arial 16 ', bg="#49A")
                    infoUitprinten.grid(row=25, column=0)

        frameBovenPlotGraph.pack(side=tk.LEFT, fill=tk.BOTH)

        titel.grid(row=0, column=1)
        bactLab.grid(row=6, column=0, sticky = "w")
        tempLab.grid(row=8, column=0, sticky = "w")
        pHLab.grid(row=10, column=0, sticky = "w")
        tim2Lab.grid(row=14, column=0, sticky = "w")
        grafiekLab.grid(row=16, column=0, sticky = "w")
        laatGrafiekZien.grid(row=25, column=0)
        buttonTerugNaarHome.grid(row=33, column=0)
        buttonNaarInfoBact.grid(row=25, column=1)
        statusbar.pack(side=tk.BOTTOM, fill=tk.BOTH)

        bactEN.grid(row=6, column = 1, pady= 10, padx= 10, ipady=10, ipadx=130)
        tempEN.grid(row=8, column = 1, pady= 10, padx= 10, ipady=10, ipadx=130)
        phEN.grid(row=10, column = 1, pady= 10, padx= 10, ipady=10, ipadx=130)
        tim2EN.grid(row=14, column =  1, pady= 10, padx= 10, ipady=10, ipadx=130)
        grafiekEN.grid(row=16, column = 1, pady= 10, padx= 10, ipady=30, ipadx=130)
        legeLabel.grid(row=20, column= 0,  pady= 10, padx= 10, ipady=10, ipadx=130)


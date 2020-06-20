import tkinter as tk
from tkinter import messagebox

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from Code.EndResults import EndResults
from Code.JsonChecker import JsonChecker


class PlotGraph(tk.Frame):
    """In dit klass worden de inputs die nodig voor het bereken van de intervals en het tekenen van het
       grafiek van het gebruiker gevraagd verolgens wordt het gerafiek aan de rechtere kant van de scherm
       geschowed, hier ook maak ik gebruik van de try, except voor het geval dat de gebruiker een verkerede
        type input in toetst """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frameBovenPlotGraph = tk.Frame(self, bg="#49A")

        titel = tk.Label(frameBovenPlotGraph, text="Grafiek tekenen", fg='black', bg= "#49A", font='Arial 35 bold')
        tk.Frame.configure(self, bg="#49A")

        buttonTerugNaarHome =tk.Button(frameBovenPlotGraph, text="Terug naar de homepagina",height=5,width=23, fg="#49A",
                             bg="white", font='Arial 10', command=lambda: controller.showFrame("MainPage"))

        buttonNaarInfoBact =tk.Button(frameBovenPlotGraph, text="Inforamatie de bacterie",height=5, width=23, fg="#49A",
                             bg="white", font='Arial 10', command=lambda: controller.showFrame("InfoBact"))
        procesFileButton = tk.Button(frameBovenPlotGraph, text="Upload a file", height=5, width=23, fg="#49A",
                                     bg="white", font='Arial 10', command=lambda: controller.showFrame("ProcesFile"))

        bactLab= tk.Label(frameBovenPlotGraph,text="Welke bacterie?", font='Arial 18', bg="#49A")
        tempLab = tk.Label(frameBovenPlotGraph, text="Wat is het tempratuur?",font='Arial 18', bg="#49A")
        pHLab= tk.Label(frameBovenPlotGraph,text="Wat is de PH grade?",font='Arial 18', bg="#49A")
        tim2Lab= tk.Label(frameBovenPlotGraph, text="Wat is de eindtijd in uren?",font='Arial 18', bg="#49A")
        grafiekLab = tk.Label(frameBovenPlotGraph, text="Kies de soort berekneing \n" ,font='Arial 18', bg="#49A")

        typeGrafiek = tk.IntVar()
        typeGrafiek.set(1)

        RadioButton1= tk.Radiobutton( frameBovenPlotGraph, text = "1.logstic met max aantaal cellen\n als beperkende factor",
                                      variable = typeGrafiek, value = 1,  bg="#49A",  font='Arial 16')
        RadioButton2= tk.Radiobutton( frameBovenPlotGraph, text = "2. logsistic curve\n met sterf fase", variable = typeGrafiek,
                                      value = 2,  bg="#49A", font='Arial 16')
        RadioButton3= tk.Radiobutton( frameBovenPlotGraph, text = "3.log groei met 4 faces, lag, log, \nstationaire en sterffases",
                                      variable = typeGrafiek, value = 3,  bg="#49A", font='Arial 16')
        RadioButton4= tk.Radiobutton( frameBovenPlotGraph, text = "4.logstic met max tempratuur \nals beperkende factor",
                                      variable = typeGrafiek, value = 4,  bg="#49A",  font='Arial 16')


        statusbar = tk.Label(self, bd=1, relief=tk.SUNKEN, padx=10, pady=20, bg="light blue",text="Copyright© Marya Dukmak")
        legeLabel = tk.Label(frameBovenPlotGraph, bg="#49A")

        bactEN = tk.Entry(frameBovenPlotGraph, font='Arial 14')
        tempEN = tk.Entry(frameBovenPlotGraph, font='Arial 14')
        phEN = tk.Entry(frameBovenPlotGraph, font='Arial 14')
        tim2EN = tk.Entry(frameBovenPlotGraph, font='Arial 14')
        try:
            laatGrafiekZien=tk.Button(frameBovenPlotGraph, text="Laat het grafiek zien!", height=5, width=23, fg="#49A",
                                        bg="white", font='Arial 10',command=lambda: PlotGrafiek(str(bactEN.get()),
                                        float(tempEN.get()), float(phEN.get()),int(tim2EN.get()), int(typeGrafiek.get())))
        except ValueError:
            messagebox.showwarning("warning", "Je hebt 1 of meerdere inputs verkeerd ingevoerd,\n probeer het opnieuw")


        def PlotGrafiek(bact_naam, temperature, pH, endTime, typeG):
            """Hier wordt de y voor het grafiek van het aloritme opgehaald en getekent."""
            temp_check = JsonChecker(bact_naam, temperature, pH, "temp", temperature)
            temp_check_terug = temp_check.values_check()
            print(temp_check_terug)

            ph_check = JsonChecker(bact_naam, temperature, pH, "ph", pH)
            ph_check_terug = ph_check.values_check()
            if (temp_check_terug and ph_check_terug) is not None:
                try:
                    y = EndResults(bact_naam, temperature, pH, endTime, typeG)
                    x = np.linspace(0, len(y), (len(y)))  # wordt op basis van de lengte van y gemaakt
                    f = Figure(figsize=(5, 5), dpi=100)
                    f.suptitle('Growth Curve', fontsize=14, fontweight='bold')
                    a = f.add_subplot(111)
                    a.set_ylabel('Groei in CFU/ml')
                    if typeGrafiek.get() == 1 or typeGrafiek.get() == 3 or typeGrafiek.get() == 2: # hier moet de x-as tijd zijn
                        a.set_xlabel('Tijd in uur')
                    if typeGrafiek.get() == 4:
                        x = np.linspace(int(tempEN.get()), 46 ,len(y))
                        a.set_ylabel("μ (h−1)")
                        a.set_xlabel("Temperature in celsius")
                        print(int(tempEN.get()))

                    a.plot(x, np.array(y))

                    # Hier wordt het grafiek in getekend
                    canvas = FigureCanvasTkAgg(f, self)
                    canvas.draw()
                    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
                    # Hier wordt de toolbar aangetoond
                    toolbar = NavigationToolbar2Tk(canvas, self)
                    toolbar.update()
                    canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
                except ValueError:
                    messagebox.showwarning("warning", "Je hebt 1 of meerdere inputs verkeerd ingevoerd,\n probeer het opnieuw")
            else:
                messagebox.showwarning("warning",
                                       "Je hebt 1 of meerdere inputs verkeerd ingevoerd,\n probeer het opnieuw")

        frameBovenPlotGraph.pack(side=tk.LEFT, fill=tk.BOTH)

        #Hier wordt alles in de schrem aangetood
        titel.grid(row=0, column=1)
        bactLab.grid(row=6, column=0, sticky="w")
        tempLab.grid(row=8, column=0, sticky="w")
        pHLab.grid(row=10, column=0, sticky="w")
        tim2Lab.grid(row=14, column=0, sticky="w")
        grafiekLab.grid(row=16, column=0, sticky="w")
        laatGrafiekZien.grid(row=25, column=0)
        buttonTerugNaarHome.grid(row=33, column=0)
        buttonNaarInfoBact.grid(row=25, column=1)
        procesFileButton.grid(row=33, column=1)
        statusbar.pack(side=tk.BOTTOM, fill=tk.BOTH)

        bactEN.grid(row=6, column=1, pady= 10, padx= 10, ipady=10, ipadx=100)
        tempEN.grid(row=8, column=1, pady= 10, padx= 10, ipady=10, ipadx=100)
        phEN.grid(row=10, column=1, pady= 10, padx= 10, ipady=10, ipadx=100)
        tim2EN.grid(row=14, column=1, pady= 10, padx= 10, ipady=10, ipadx=100)
        legeLabel.grid(row=20, column=0,  pady= 10, padx= 10, ipady=10, ipadx=100)

        RadioButton1.grid(row=17, column=0, sticky="w")
        RadioButton2.grid(row=17, column=1, sticky="w")
        RadioButton3.grid(row=19, column=0, sticky="w")
        RadioButton4.grid(row=19, column=1, sticky="w")

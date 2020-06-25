import tkinter as tk
from tkinter import filedialog, messagebox

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from Code.CSV_reader import ReadIt


class ProcesFile(tk.Frame):
    """In dit klasse kan de gebruiker een csv file uploaden en de progranmmma een bepaalde constanten laten uitrekenen
      die de gebruiker zelf kan kiezen, er kan ook het grafiek van de csv bestand getekent worden"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # kleuren voor de background en fg
        bg_background = "#81B29A"
        fg = "#3D405B"

        frameBovenPlotGraph = tk.Frame(self, bg=bg_background)
        tk.Frame.configure(self, bg=bg_background)

        titel = tk.Label(frameBovenPlotGraph,text="Bereken constanten van een dataset",  font='Arial 22 bold',
                         bg=bg_background)
        infoUitprinten = tk.Label(frameBovenPlotGraph,
                                  text="\n\n\nUpload je csv bestand eerst \n "
                                       "Daarna kies de constanten die je wilt laten uitrekenen\n\n\n",
                                  font='Arial 18 ', bg=bg_background, fg=fg)

        buttonTerugNaarHome = tk.Button(frameBovenPlotGraph, text="Terug naar de homepagina", height=5, width=23,
                                        fg=fg, font='Arial 10', command=lambda: controller.showFrame("MainPage"))
        buttoChoosFile = tk.Button(frameBovenPlotGraph, text="Selecteer een bestand", height=5, width=23,
                                        fg=fg,  font='Arial 10', command=lambda: ProcesFile.file(self))

        buttonPlotGrafiekFile = tk.Button(frameBovenPlotGraph, text="Laat de grafiek zien!", height=5,
                                          width=23, fg=fg,  font='Arial 10', command=lambda: plot_file())

        buttonPrintBerekeningen = tk.Button(frameBovenPlotGraph, text="Laat het antwoord zien!", height=5, width=23,
                                        fg=fg,  font='Arial 10', command= lambda:print_uitkomsten())

        antwoordShowLabel = tk.Label(frameBovenPlotGraph, font='Arial 16',bg=bg_background, width=40, text='', fg=fg)
        antwoordShowLabel2 = tk.Label(frameBovenPlotGraph, font='Arial 16',bg=bg_background, width=40, text='',fg=fg)
        antwoordShowLabel3 = tk.Label(frameBovenPlotGraph, font='Arial 16', bg=bg_background, width=40, text='', fg=fg)
        antwoordShowLabel_leeg = tk.Label(frameBovenPlotGraph, font='Arial 16',bg=bg_background, width=40, text='\n\n',fg=fg)


        # variabel voor de checkbuttons om te kijken of ze geselecteerd
        var = tk.IntVar()
        var2 = tk.IntVar()
        var3 = tk.IntVar()

        # hier kan de gebruiker de opties kiezen die hij wil laten berekenen
        checkButtton = tk.Checkbutton(frameBovenPlotGraph, text= "De groeifactor                                     "
                                                                 "", variable = var, font='Arial 18 ',bg=bg_background)
        checkButtton2 = tk.Checkbutton(frameBovenPlotGraph, text="De maximum aantaal gemaakte cellen"
                                                                 "", variable=var2, font='Arial 18',
                                       bg=bg_background)
        checkButtton3 = tk.Checkbutton(frameBovenPlotGraph, text="De gekoste tijd voor het experiment     ", variable=var3,
                                       font='Arial 18',
                                       bg=bg_background)

        # Hier wordt alles in de schrem aangetood
        frameBovenPlotGraph.pack(side=tk.LEFT, fill=tk.Y)
        titel.pack(side=tk.TOP, fill=tk.BOTH)
        infoUitprinten.pack(side = tk.TOP, fill= tk.BOTH)

        checkButtton.pack(side = tk.TOP, fill=tk.BOTH ,ancho="w")
        checkButtton2.pack(side = tk.TOP, fill=tk.BOTH,ancho="w")
        checkButtton3.pack(side = tk.TOP, fill=tk.BOTH,ancho="w")

        antwoordShowLabel_leeg.pack(side=tk.TOP, fill=tk.BOTH, ancho= "w")
        antwoordShowLabel.pack(side=tk.TOP, fill=tk.BOTH, ancho= "w")
        antwoordShowLabel2.pack(side=tk.TOP, fill=tk.BOTH, ancho= "w")
        antwoordShowLabel3.pack(side=tk.TOP, fill=tk.BOTH, ancho= "w")

        buttoChoosFile.pack(side = tk.LEFT,  padx=5, ancho="w")
        buttonPlotGrafiekFile.pack(side = tk.LEFT,  padx=5, ancho="w")
        buttonPrintBerekeningen.pack(side = tk.LEFT,  padx=5, ancho="w")
        buttonTerugNaarHome.pack(side = tk.LEFT,  padx=5, ancho="w")

        def print_uitkomsten():
            """
            Hier wordt de class(CSV-Reader) aangroepen die de growth rate en/de max aantaal cellen kan uitrekenen
                en vervolgens worden de antwoorden op hets scherm aangetoond
            """

            answerr= ReadIt(self.fileDai)
            answe_growth_rate= answerr.bereken_growth_rate()
            answer_aantaal_cellen= answerr.bereken_maxcellen()
            if var.get() == 1:
                # als de growth rate wordt gekozen
                antwoordShowLabel.config(text="De growth rate is: "+str(answe_growth_rate) + "     ")
            if var2.get() == 1:
                # als de max aantaal cellen wordt gekozen
                antwoordShowLabel2.config(text="    De max aantaal cellen is: " + str(answer_aantaal_cellen[1]))
            if var3.get() == 1:
                # als de tijd woordt gekozen
                antwoordShowLabel3.config(text="De tijd van het experiment is :" + str(answer_aantaal_cellen[0]) + " uur           "
                                                                                                                   " ")
        def plot_file():
            """
              Hier kunnnen de data van de file in een grafiek getekend worden
            """
            try:
                anw = ReadIt.readd(self, self.fileDai)
                x, y = anw[0], anw[1]
                f = Figure(figsize=(5, 5), dpi=100)
                f.patch.set_facecolor("#fff8e8")
                f.suptitle('Growth Curve', fontsize=14, fontweight='bold')
                a = f.add_subplot(111)
                a.set_ylabel('Groei in CFU/ml')
                a.set_xlabel('Tijd in uur')
                a.plot(np.array(x),np.array(y), "#3D405B")
                a.plot(x, np.array(y), "o", color="#E07A5F")
                canvas = FigureCanvasTkAgg(f, self)
                canvas.draw()
                canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
            except Exception:
                messagebox.showwarning("warning","Je hebt 1 of meerdere inputs verkeerd ingevoerd,\n ----probeer het opnieuw----")

    def file(self):
        """ Hierdoor kan de gebruiker een file uploaden"""
        self.fileDai= filedialog.askopenfilename(initialdir="/Bureaublad",title="Select file",filetypes=(("csv files","*.csv"),("all files","*.*")))

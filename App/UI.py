import json
import tkinter as tk
from tkinter import filedialog

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from Code.CSV_reader import readit
from Code.EndResult import EndResult


#TODO: voeg comments, maak de plot specfieker

class GrowthCurve(tk.Tk):
    """Dit is de main window, in dit klasse worden de andere frames geshowed"""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Growth Curve app')
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.geometry("{}x{}+-7+0".format(screenWidth, screenHeight - 27))

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for page in (MainPage, PlotGraph, InfoBact, ProcesFile):
            pageName = page.__name__
            frame = page(parent=container, controller=self)
            self.frames[pageName] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame("MainPage")

    def showFrame(self, pageName):
        frame = self.frames[pageName]
        frame.tkraise()


class MainPage(tk.Frame):
    "Dit is de main frame, hier zijn er 3 buttons aangamaakt om vervolgens andere klasses aanteroepen"
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        self.controller = controller

        frameBovenMainpage = tk.Frame(self, bg="#49A")
        frameOnderMainpage = tk.Frame(self, bg="#49A")

        titel=tk.Label(frameBovenMainpage, text="Welcom to Growth Curve model!", fg='black', bg="white",
                       font='Arial 35 bold')
        tk.Frame.configure(self, bg="#49A")

        startGrafiekTekenen = tk.Button(frameOnderMainpage, text="Teken het grafiek", height=5, width=23, fg="#49A",
                             bg="white", font='Arial 14', command=lambda: controller.showFrame("PlotGraph"))
        infoBact = tk.Button(frameOnderMainpage, text="Informatie over de bacterie ", height=5, width=23, fg="#49A",
                             bg="white",font='Arial 14', command=lambda: controller.showFrame("InfoBact"))

        exitButton = tk.Button(frameOnderMainpage, text="Exit the program ",  height=5, width=23, fg="#49A",
                             bg="white", font='Arial 14',command=frameBovenMainpage.quit)

        procesButton= tk.Button(frameOnderMainpage, text="Upload a file",  height=5, width=23, fg="#49A",
                             bg="white", font='Arial 14',command=lambda :controller.showFrame("ProcesFile"))

        statusbar = tk.Label(self, bd=1, relief=tk.SUNKEN, padx=10, pady=20, bg="light blue",
                             text="Copyright© Marya Dukmak")
        statusbar.pack(side=tk.BOTTOM, fill=tk.BOTH)

        titel.pack(side=tk.TOP, fill=tk.X)
        startGrafiekTekenen.pack(side=tk.LEFT, fill=tk.X, padx=5)
        infoBact.pack(side=tk.LEFT, fill=tk.X, padx=5)
        procesButton.pack(side=tk.LEFT, fill=tk.X, padx=5)
        exitButton.pack(side=tk.LEFT, fill=tk.X, padx=5)
        frameBovenMainpage.pack(pady=0, expand=tk.TRUE)
        frameOnderMainpage.pack(expand=tk.TRUE)


class InfoBact(tk.Frame):
    """In dit klass kunnen er informatie over een bepaalde bactrie geshowed worden, door gebruik van de json bestand
    te maken"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        frameBovenInfoBact = tk.Frame(self, bg="#49A")
        frameOnderInfoBact = tk.Frame(self, bg="#49A")

        titel=tk.Label(frameOnderInfoBact, text="Informatie over de bacterie", fg='black', bg="#49A", font='Arial 35 bold')
        tk.Frame.configure(self, bg="#49A")

        buttonMainPage = tk.Button(frameBovenInfoBact, text="Terug naar de homepagina",height=5, width=23, fg="#49A",
                             bg="white", font='Arial 10',command=lambda: controller.showFrame("MainPage"))

        buttonPlotGraph = tk.Button(frameBovenInfoBact, text="Teken het grafiek",height=5, width=23, fg="#49A",
                             bg="white", font='Arial 10', command=lambda: controller.showFrame("PlotGraph"))

        LabelVraag = tk.Label(frameOnderInfoBact, text="Over welke bacterie wil je informatie krijgen?\n "
                                             "Type de naam van de  bacterie hieronder:", font='Arial 18', bg="#49A")

        entryBactName = tk.Entry(frameOnderInfoBact)

        buttonInfoJson = tk.Button(frameOnderInfoBact, text="Zoek het op!",height=2, width=12, fg="#49A",
                             bg="white", font='Arial 10', command=lambda: findJson(entryBactName.get()))
        statusbar = tk.Label(self, bd=1, relief=tk.SUNKEN, padx=10, pady=20, bg="light blue",
                             text="Copyright© Marya Dukmak")

        def findJson(input):
            """De entry van de gebruiker wordt naar deze functie doorgestuurd om vervolgens de bijhornde info in de json
                bestand te zoeken. Voor het gevaal dat de gebruiker een naam invoert die niet tussen de json bestanden staat,
                 gebruik ik een try except"""
            try:
                with open(str(input) + ".json", "r") as f:
                    info = json.load(f)
                    informatieVanJson= info["info"]
                    infoUitprinten= tk.Label(frameOnderInfoBact,text=informatieVanJson, font='Arial 16 ', bg="#49A")
                    infoUitprinten.pack(side=tk.TOP, fill=tk.X, padx=5)
            except FileNotFoundError:

                infoUitprinten = tk.Label(frameOnderInfoBact, text="We hebben helaas geen informatie kunnen vinden"
                                                                   " voor deze bacterie",font='Arial 16 ', bg="#49A")
                infoUitprinten.pack(side=tk.TOP, fill=tk.X, padx=5)

        frameOnderInfoBact.pack(pady=0, expand=tk.TRUE)
        frameBovenInfoBact.pack(expand=tk.TRUE)
        titel.pack(side=tk.TOP, fill=tk.X)
        LabelVraag.pack(side=tk.TOP, fill=tk.X, padx=5)
        entryBactName.pack(side=tk.TOP, padx=40, pady=40, ipady=10, ipadx=130)
        buttonInfoJson.pack(side=tk.TOP, ipady=10, ipadx=110)
        buttonPlotGraph.pack(side=tk.LEFT, fill=tk.X, padx=10)
        buttonMainPage.pack(side=tk.LEFT, fill=tk.X, padx=10)
        statusbar.pack(side=tk.BOTTOM, fill=tk.BOTH)

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


if __name__ == '__main__':
    app = GrowthCurve()
    app.mainloop()

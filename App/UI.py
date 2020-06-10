import json
import tkinter as tk

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from Code.EndResult import EndResult


#TODO: voeg comments, maak de plot specfieker

class GrowthCurve(tk.Tk):
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
        for page in (MainPage, PlotGraph, InfoBact):
            pageName = page.__name__
            frame = page(parent=container, controller=self)
            self.frames[pageName] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame("MainPage")

    def showFrame(self, pageName):
        frame = self.frames[pageName]
        frame.tkraise()


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        self.controller = controller

        frameBovenMainpage = tk.Frame(self, bg="#49A")
        frameOnderMainpage = tk.Frame(self, bg="#49A")

        titel = tk.Label(frameBovenMainpage, text="Welcom to Growth Curve model!", fg='black', bg="white", font='Arial 35 bold')
        tk.Frame.configure(self, bg="#49A")

        startGrafiekTekenen = tk.Button(frameOnderMainpage, text="Teken het grafiek", height=5, width=23, fg="#49A",
                             bg="white", font='Arial 14', command=lambda: controller.showFrame("PlotGraph"))
        infoBact = tk.Button(frameOnderMainpage, text="Informatie over de bacterie ", height=5, width=23, fg="#49A",
                             bg="white",font='Arial 14', command=lambda: controller.showFrame("InfoBact"))

        exitButton = tk.Button(frameOnderMainpage, text="Exit the program ",  height=5, width=23, fg="#49A",
                             bg="white", font='Arial 14',command=frameBovenMainpage.quit)
        statusbar = tk.Label(self, bd=1, relief=tk.SUNKEN, padx=10, pady=20, bg="light blue",
                             text="Copyright© Marya Dukmak")

        titel.pack(side=tk.TOP, fill=tk.X)
        startGrafiekTekenen.pack(side=tk.LEFT, fill=tk.X, padx=5)
        infoBact.pack(side=tk.LEFT, fill=tk.X, padx=5)
        exitButton.pack(side=tk.LEFT, fill=tk.X, padx=5)
        statusbar.pack(side=tk.BOTTOM, fill=tk.BOTH)
        frameBovenMainpage.pack(pady=0, expand=tk.TRUE)
        frameOnderMainpage.pack(expand=tk.TRUE)


class InfoBact(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frameBovenInfoBact = tk.Frame(self, bg="#49A")
        frameOnderInfoBact = tk.Frame(self, bg="#49A")

        titel = tk.Label(frameOnderInfoBact, text="Informatie over de bacterie", fg='black', bg="#49A", font='Arial 35 bold')
        tk.Frame.configure(self, bg="#49A")

        buttonMainPage = tk.Button(frameBovenInfoBact, text="Terug naar de homepagina",height=5, width=23, fg="#49A",
                             bg="white", font='Arial 10',command=lambda: controller.showFrame("MainPage"))

        buttonPlotGraph = tk.Button(frameBovenInfoBact, text="Teken het grafiek",height=5, width=23, fg="#49A",
                             bg="white", font='Arial 10', command=lambda: controller.showFrame("PlotGraph"))

        LabelVraag = tk.Label(frameOnderInfoBact, text="Over welke bacterie wil je informatie krijgen?\n "
                                                     "Type de naam van de  bacterie hieronder:", font='Arial 18 ', bg="#49A")

        entryBactName = tk.Entry(frameOnderInfoBact)

        buttonInfoJson = tk.Button(frameOnderInfoBact, text="Zoek het op!",height=2, width=12, fg="#49A",
                             bg="white", font='Arial 10', command=lambda: findJson(entryBactName.get()))

        def findJson(input):
            with open(str(input) + ".json", "r") as f:
                info = json.load(f)
                informatieVanJson= info["info"]
                infoUitprinten= tk.Label(frameOnderInfoBact,text=informatieVanJson, font='Arial 16 ', bg="#49A")
                infoUitprinten.pack(side=tk.TOP, fill=tk.X, padx=5)

        frameOnderInfoBact.pack(pady=0, expand=tk.TRUE)
        frameBovenInfoBact.pack(expand=tk.TRUE)
        titel.pack(side=tk.TOP, fill=tk.X)
        LabelVraag.pack(side=tk.TOP, fill=tk.X, padx=5)
        entryBactName.pack(side=tk.TOP, padx=40, pady=40, ipady=10, ipadx=130)
        buttonInfoJson.pack(side=tk.TOP, ipady=10, ipadx=110)
        buttonPlotGraph.pack(side=tk.LEFT, fill=tk.X, padx=10)
        buttonMainPage.pack(side=tk.LEFT, fill=tk.X, padx=10)


class PlotGraph(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frameBovenPlotGraph = tk.Frame(self, bg="#49A")

        titel = tk.Label(frameBovenPlotGraph, text="Grafiek tekenen", fg='black', bg= "#49A", font='Arial 35 bold')
        tk.Frame.configure(self, bg="#49A")

        buttonTerugNaarHome =tk.Button(frameBovenPlotGraph, text="Terug naar de homepagina", height=5, width=23, fg="#49A",
                             bg="white", font='Arial 10', command=lambda: controller.showFrame("MainPage"))

        buttonNaarInfoBact =tk.Button(frameBovenPlotGraph, text="Inforamatie de bacterie",height=5, width=23, fg="#49A",
                             bg="white", font='Arial 10', command=lambda: controller.showFrame("InfoBact"))

        bactLab= tk.Label(frameBovenPlotGraph,text="Welke bacterie?", font='Arial 18', bg="#49A")
        tempLab = tk.Label(frameBovenPlotGraph, text="Wat is het tempratuur?",font='Arial 18', bg="#49A")
        pHLab= tk.Label(frameBovenPlotGraph,text="Wat is de PH grade?",font='Arial 18', bg="#49A")
        tim1Lab = tk.Label(frameBovenPlotGraph, text="Wat is de begintijd in uren?",font='Arial 18', bg="#49A")
        tim2Lab= tk.Label(frameBovenPlotGraph, text="Wat is de eindtijd in uren?",font='Arial 18', bg="#49A")
        grafiekLab = tk.Label(frameBovenPlotGraph, text="Kies de soort berekneing \n 1.logistic \n 2.Gompertz",font='Arial 16', bg="#49A")
        legeLabel = tk.Label(frameBovenPlotGraph, bg="#49A")

        bactEN = tk.Entry(frameBovenPlotGraph)
        tempEN = tk.Entry(frameBovenPlotGraph)
        phEN = tk.Entry(frameBovenPlotGraph)
        tim1EN = tk.Entry(frameBovenPlotGraph)
        tim2EN = tk.Entry(frameBovenPlotGraph)
        grafiekEN = tk.Entry(frameBovenPlotGraph)

        laatGrafiekZien = tk.Button(frameBovenPlotGraph, text="Laat het grafiek zien!", height=5, width=23, fg="#49A", bg="white",
                                    font='Arial 10',command=lambda: PlotGrafiek(str(bactEN.get()), int(tempEN.get()), int(phEN.get()),
                                                       int(tim1EN.get()), int(tim2EN.get()), int(grafiekEN.get())))

        def PlotGrafiek(bacteriaName, temperature, pH, startTime, endTime, typeG):
            x = np.linspace(startTime, endTime, (endTime - startTime + 1))
            y = EndResult.growth_endresult(bacteriaName, temperature, pH, startTime, endTime, typeG)
            f = Figure(figsize=(5, 5), dpi=100)
            a = f.add_subplot(111)
            a.plot(x, y)
            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        frameBovenPlotGraph.pack(side=tk.LEFT, fill=tk.BOTH)

        titel.grid(row=0, column=2)
        bactLab.grid(row=6, column=0)
        tempLab.grid(row=8, column=0)
        pHLab.grid(row=10, column=0)
        tim1Lab.grid(row=12, column=0)
        tim2Lab.grid(row=14, column=0)
        grafiekLab.grid(row=16, column=0)
        laatGrafiekZien.grid(row=25, column=0)
        buttonTerugNaarHome.grid(row=25, column=2)
        buttonNaarInfoBact.grid(row=25, column=1)

        bactEN.grid(row = 6 , column = 2, pady= 10, padx= 10, ipady=10, ipadx=130)
        tempEN.grid(row = 8 , column = 2, pady= 10, padx= 10, ipady=10, ipadx=130)
        phEN.grid(row = 10 , column = 2, pady= 10, padx= 10, ipady=10, ipadx=130)
        tim1EN.grid(row = 12 , column = 2, pady= 10, padx= 10, ipady=10, ipadx=130)
        tim2EN.grid(row = 14 , column =  2, pady= 10, padx= 10, ipady=10, ipadx=130)
        grafiekEN.grid(row = 16 , column = 2, pady= 10, padx= 10, ipady=10, ipadx=130)
        legeLabel.grid(row= 20, column= 0,  pady= 10, padx= 10, ipady=10, ipadx=130)


if __name__ == '__main__':
    app = GrowthCurve()
    app.mainloop()

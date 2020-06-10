import json
import tkinter as tk

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from Code.EndResult import EndResult


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

        frameBovenMainpage = tk.Frame(self, bg="red")
        frameOnderMainpage = tk.Frame(self, bg="white")

        titel = tk.Label(frameBovenMainpage, text="Welkom to Growth shit", fg='black', bg="white")
        tk.Frame.configure(self, background = "#49A",)
        titel.config(font='Arial 35 bold')

        startGrafiekTekenen = tk.Button(frameOnderMainpage, text="start grafiek tekenen", height=5, width=23, fg="#49A",
                             bg="white",
                                    command=lambda: controller.showFrame("PlotGraph"))
        infoBact = tk.Button(frameOnderMainpage, text="informatie over het bact ", height=5, width=23, fg="#49A",
                             bg="white",
                                     command=lambda: controller.showFrame("InfoBact"))

        exitButton = tk.Button(frameOnderMainpage, text="Exit ",  height=5, width=23, fg="#49A",
                             bg="white",
                                   command=frameBovenMainpage.quit)
        statusbar = tk.Label(self, bd=1, relief=tk.SUNKEN, padx=10, pady=20, bg="light blue",
                             text="Copyright© Me")

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
        frameBovenPlotGraph = tk.Frame(self, bg="#49A")
        frameOnderMainpage = tk.Frame(self, bg="#49A")

        titel = tk.Label(frameOnderMainpage, text="Informatie over de bactria", fg='black', bg="#49A")
        tk.Frame.configure(self, background="#49A" )
        titel.config(font='Arial 35 bold')

        button1 = tk.Button(frameBovenPlotGraph, text="Back to Home",height=5, width=23, fg="#49A",
                             bg="white",
                            command=lambda: controller.showFrame("MainPage"))

        button2 = tk.Button(frameBovenPlotGraph, text="PLot het grafiek",height=5, width=23, fg="#49A",
                             bg="white",
                            command=lambda: controller.showFrame("PlotGraph"))

        bactLab = tk.Label(frameOnderMainpage, text="Over welke bactrie wil je informatie krijgen?\n "
                                                     "Type de naam van de bactrie hieronder", font='Arial 18 ', bg="#49A")

        button3 = tk.Button(frameOnderMainpage, text="Zoek het op",height=2, width=12, fg="#49A",
                             bg="white",
                            command=lambda: VindInfo(bactEN.get()))
        bactEN = tk.Entry(frameOnderMainpage)

        def VindInfo(input):
            with open(str(input) + ".json", "r") as f:
                info = json.load(f)
                inf= info["info"]

                bb = tk.Label(frameOnderMainpage,
                      text=inf, font='Arial 16 ', bg="#49A")

                bb.pack(side=tk.TOP, fill=tk.X, padx=5)

        frameOnderMainpage.pack(pady=0, expand=tk.TRUE)
        frameBovenPlotGraph.pack(expand=tk.TRUE)
        titel.pack(side=tk.TOP, fill=tk.X)
        bactLab.pack(side=tk.TOP, fill=tk.X, padx=5)
        bactEN.pack(side=tk.TOP, padx=40, pady=40, ipady=10, ipadx=130)
        button3.pack(side=tk.TOP, ipady=10, ipadx=110)
        button2.pack(side=tk.LEFT, fill=tk.X, padx=10)
        button1.pack(side=tk.LEFT, fill=tk.X, padx=10)


class PlotGraph(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        frameBovenPlotGraph = tk.Frame(self, bg="#49A")

        titel = tk.Label(frameBovenPlotGraph, text="Grafiek tekenen", fg='black', bg= "#49A")
        tk.Frame.configure(self, background = "#49A",)
        titel.config(font='Arial 35 bold')

        buttonTerugNaarHome =tk.Button(frameBovenPlotGraph, text="Back to Home", height=5, width=23, fg="#49A",
                             bg="white",command=lambda: controller.showFrame("MainPage"))

        buttonNaarInfoBact =tk.Button(frameBovenPlotGraph, text="Inforamatie over de bactrie",height=5, width=23, fg="#49A",
                             bg="white",command=lambda: controller.showFrame("InfoBact"))

        bactLab= tk.Label(frameBovenPlotGraph,text="Welke bactria?", font='Arial 18 ', bg="#49A")
        bactEN = tk.Entry(frameBovenPlotGraph)
        tempLab = tk.Label(frameBovenPlotGraph, text="Wat is het tempratuur?",font='Arial 18 ', bg="#49A")
        tempEN = tk.Entry(frameBovenPlotGraph )
        pHLab= tk.Label(frameBovenPlotGraph,text="Wat is de PH?",font='Arial 18 ', bg="#49A")
        phEN = tk.Entry(frameBovenPlotGraph )
        tim1Lab = tk.Label(frameBovenPlotGraph, text="Wat is de begintijd in uren?",font='Arial 18 ', bg=  "#49A" )
        tim1EN = tk.Entry(frameBovenPlotGraph )
        tim2Lab= tk.Label(frameBovenPlotGraph, text="Wat is de eindtijd in uren?",font='Arial 18 ', bg=  "#49A" )
        tim2EN = tk.Entry(frameBovenPlotGraph)
        grafiekLab = tk.Label(frameBovenPlotGraph, text="Kies de soort berekneing \n 1.logstic \n 2.Gompertz",font='Arial 16', bg="#49A")
        grafiekEN = tk.Entry(frameBovenPlotGraph)
        legeLabel = tk.Label(frameBovenPlotGraph, bg="#49A")
        laatzien = tk.Button(frameBovenPlotGraph, text="laat t zien", height=5, width=23, fg="#49A", bg="white",
                             command=lambda: stuurdoor(str(bactEN.get()), int(tempEN.get()), int(phEN.get()),
                                                       int(tim1EN.get()), int(tim2EN.get()), int(grafiekEN.get())))

        def stuurdoor(bacteriaName, temperature, pH, startTime, endTime, typeG):
            y = EndResult.growth_endresult(bacteriaName, temperature, pH, startTime, endTime, typeG)
            x = np.linspace(startTime, endTime, (endTime - startTime + 1))
            f = Figure(figsize=(5, 5), dpi=100)
            a = f.add_subplot(111)
            a.plot(x, y)
            canvas = FigureCanvasTkAgg(f, self)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=tk.BOTTOM    , fill=tk.BOTH, expand=True)

        frameBovenPlotGraph.pack(side= tk.LEFT, fill = tk.BOTH)

        titel.grid(row = 0, column = 2)
        bactLab.grid(row= 6, column = 0)
        bactEN.grid(row = 6 , column = 2, pady= 10, padx= 10, ipady=10, ipadx=130)
        tempLab.grid(row =8 , column = 0)
        tempEN.grid(row = 8 , column = 2, pady= 10, padx= 10, ipady=10, ipadx=130)
        pHLab.grid(row= 10, column= 0)
        phEN.grid(row = 10 , column = 2, pady= 10, padx= 10, ipady=10, ipadx=130)
        tim1Lab.grid(row= 12, column = 0)
        tim1EN.grid(row = 12 , column = 2, pady= 10, padx= 10, ipady=10, ipadx=130)
        tim2Lab.grid(row= 14, column = 0)
        tim2EN.grid(row = 14 , column =  2, pady= 10, padx= 10, ipady=10, ipadx=130)
        grafiekLab.grid(row =16, column=0)
        grafiekEN.grid(row = 16 , column = 2, pady= 10, padx= 10, ipady=10, ipadx=130)

        legeLabel.grid(row= 20, column= 0,  pady= 10, padx= 10, ipady=10, ipadx=130)
        buttonTerugNaarHome.grid(row= 25, column= 2 )
        laatzien.grid(row=25, column = 0)

        buttonNaarInfoBact.grid(row= 25, column= 1 )


if __name__ == '__main__':

    app = GrowthCurve()
    app.mainloop()

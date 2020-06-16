

import json
import tkinter as tk


class InfoBact(tk.Frame):
    """In dit klass kunnen er informatie over een bepaalde bactrie geshowed worden, door gebruik van de json bestand
        te maken"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # 2 frames aangemaakt om  de layout beter te kunnen organisieren
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

        entryBactName = tk.Entry(frameOnderInfoBact, font="Arial 18")

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

        # hier wordt alles op het scherm aangetoond
        frameOnderInfoBact.pack(pady=0, expand=tk.TRUE)
        frameBovenInfoBact.pack(expand=tk.TRUE)
        titel.pack(side=tk.TOP, fill=tk.X)
        LabelVraag.pack(side=tk.TOP, fill=tk.X, padx=5)
        entryBactName.pack(side=tk.TOP, padx=40, pady=40, ipady=10, ipadx=130)
        buttonInfoJson.pack(side=tk.TOP, ipady=10, ipadx=110)
        buttonPlotGraph.pack(side=tk.LEFT, fill=tk.X, padx=10)
        buttonMainPage.pack(side=tk.LEFT, fill=tk.X, padx=10)
        statusbar.pack(side=tk.BOTTOM, fill=tk.BOTH)

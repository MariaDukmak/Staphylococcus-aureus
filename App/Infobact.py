
import json
import tkinter as tk
from tkinter import messagebox

from PIL import ImageTk, Image


class InfoBact(tk.Frame):
    """In dit klass kunnen er informatie over een bepaalde bactrie geshowed worden, door gebruik van de json bestand
        te maken"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # kleuren voor de background en fg
        bg_background = "#81B29A"
        fg = "#3D405B"

        # 2 frames aangemaakt om  de layout beter te kunnen organisieren
        frameBovenInfoBact = tk.Frame(self, bg=bg_background)
        frameOnderInfoBact = tk.Frame(self, bg=bg_background)
        frameMideen = tk.Frame(self, bg= bg_background)

        titel = tk.Label(frameOnderInfoBact, text="Informatie over de bacterie", fg='black', font='Arial 35 bold',
                         bg =bg_background)
        tk.Frame.configure(self, bg=bg_background)

        buttonMainPage = tk.Button(frameBovenInfoBact, text="Terug naar de homepagina",height=5, width=23, fg=fg,
                             bg="white", font='Arial 10',command=lambda: controller.showFrame("MainPage"))

        buttonPlotGraph = tk.Button(frameBovenInfoBact, text="Teken de grafiek",height=5, width=23, fg=fg,
                             bg="white", font='Arial 10', command=lambda: controller.showFrame("PlotGraph"))

        LabelVraag = tk.Label(frameOnderInfoBact,text="Over welke bacterie wil je informatie krijgen?\n "
                                             "Type de naam van de bacterie hiernaast:", font='Arial 18',bg=bg_background)

        entryBactName = tk.Entry(frameOnderInfoBact, font="Arial 18")

        buttonInfoJson = tk.Button(frameOnderInfoBact, text="Zoek het op!",height=2, width=12, fg=fg,
                             bg="white", font='Arial 10', command=lambda: findJson(entryBactName.get()))

        def findJson(input):
            """De entry van de gebruiker wordt naar deze functie doorgestuurd om vervolgens de bijhornde info in de json
                bestand te zoeken.Er wordt ook een foto van de bactie gelaten zien als het bestaat.
                Voor het gevaal dat de gebruiker een naam invoert die niet tussen de json bestanden
                staat, gebruik ik een try except"""
            try:
                with open("../Extra bestanden/"+str(input) + ".json", "r") as f:
                    info = json.load(f)
                    informatieVanJson = info["info"]
                    infoUitprinten= tk.Label(frameMideen, text="", font='Arial 20 ', bg=bg_background, fg=fg)
                    naamUitprinten = tk.Label(frameMideen, text =str(input),  font='Arial 20 bold', bg=bg_background,fg=fg)
                    infoUitprinten.config(text=informatieVanJson)
                    naamUitprinten.pack(side=tk.LEFT, fill=tk.X, padx=5, ancho="n")
                    infoUitprinten.pack(side=tk.LEFT, fill=tk.X, padx=5, ancho="nw")
            except FileNotFoundError:
                messagebox.showwarning("", "We hebben geen informatie over die bacterie kunnen vinden")

            img = ImageTk.PhotoImage(Image.open("../Extra bestanden/" + str(input)+".png"))
            panel = tk.Label(frameMideen, image=img)
            panel.image = img
            panel.pack(side="bottom",  ancho="center")

        # hier wordt alles op het scherm aangetoond
        frameOnderInfoBact.pack(pady=0, expand=tk.TRUE, fill= tk.X)
        frameMideen.pack(expand= tk.TRUE, fill = tk.X)
        frameBovenInfoBact.pack(expand=tk.TRUE)
        titel.pack(side=tk.TOP, fill=tk.X)
        LabelVraag.pack(side=tk.LEFT, fill=tk.X, padx=5)
        entryBactName.pack(side=tk.LEFT, padx=40, pady=40, ipady=10, ipadx=70, ancho="w")

        buttonInfoJson.pack(side=tk.LEFT, padx=5, pady=5, ancho="e")

        buttonPlotGraph.pack(side=tk.LEFT, fill=tk.X, padx=10)
        buttonMainPage.pack(side=tk.LEFT, fill=tk.X, padx=10)

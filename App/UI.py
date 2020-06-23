import tkinter as tk

from App.Infobact import InfoBact
from App.Mainpage import MainPage
from App.Plotgraph import PlotGraph
from App.Procesfile import ProcesFile


class GrowthCurve(tk.Tk):
    """Dit is de main window, in dit klasse worden de andere frames geshowed"""
    def __init__(self, *args, **kwargs):
        # Bouwt het aantal pagina's op als wordt ingegeven.
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
        """Plaatst de gewenste frame voor de andere frames."""
        frame = self.frames[pageName]
        frame.tkraise()


if __name__ == '__main__':
    """ runt de GUI door de root te runnen."""
    app = GrowthCurve()
    app.iconphoto(False, tk.PhotoImage(file="../Extra bestanden/homepageicon.png"))
    app.mainloop()

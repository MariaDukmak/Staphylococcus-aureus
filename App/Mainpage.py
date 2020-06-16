import tkinter as tk


class MainPage(tk.Frame):
    """Dit is de main frame (begin schrem) die de gebruiker meteen ziet als de programma runt,
      hier zijn er 3 buttons aangamaakt om vervolgens andere klasses aanteroepen"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        self.controller = controller
        # 2 frames aangemaakt om  de layout beter te kunnen organisieren
        frameBovenMainpage = tk.Frame(self, bg="#49A")
        frameOnderMainpage = tk.Frame(self, bg="#49A")
        tk.Frame.configure(self, bg="#49A")

        titel=tk.Label(frameBovenMainpage, text="Welcom to Growth Curve model!", fg='black', bg="white",
                       font='Arial 35 bold')

        startGrafiekTekenen = tk.Button(frameOnderMainpage, text="Teken het grafiek", height=5, width=23, fg="#49A",
                             bg="white", font='Arial 14', command=lambda: controller.showFrame("PlotGraph"))

        infoBact = tk.Button(frameOnderMainpage, text="Informatie over de bacterie ", height=5, width=23, fg="#49A",
                             bg="white",font='Arial 14', command=lambda: controller.showFrame("InfoBact"))

        exitButton = tk.Button(frameOnderMainpage, text="Exit the program ",  height=5, width=23, fg="#49A",
                             bg="white", font='Arial 14',command=frameBovenMainpage.quit)

        procesFileButton = tk.Button(frameOnderMainpage, text="Upload a file",  height=5, width=23, fg="#49A",
                             bg="white", font='Arial 14',command=lambda :controller.showFrame("ProcesFile"))

        statusbar = tk.Label(self, bd=1, relief=tk.SUNKEN, padx=10, pady=20, bg="light blue",
                             text="Copyright© Marya Dukmak")
        statusbar.pack(side=tk.BOTTOM, fill=tk.BOTH)

        # hier wordt alles op het schrem aangetoond
        titel.pack(side=tk.TOP, fill=tk.X)
        startGrafiekTekenen.pack(side=tk.LEFT, fill=tk.X, padx=5)
        infoBact.pack(side=tk.LEFT, fill=tk.X, padx=5)
        procesFileButton.pack(side=tk.LEFT, fill=tk.X, padx=5)
        exitButton.pack(side=tk.LEFT, fill=tk.X, padx=5)
        frameBovenMainpage.pack(pady=0, expand=tk.TRUE)
        frameOnderMainpage.pack(expand=tk.TRUE)


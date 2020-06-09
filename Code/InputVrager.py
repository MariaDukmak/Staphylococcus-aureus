class Inputs:
    """Voor elke model moet er Inputs van de user gevraagd worden
     dat wordt in de andere twee classes gebruikt

    Parameters :
    _____________
    bacteriaName : str
         De naam van de bactria
    temperature: float
        De begin waarde van de temperature van de model
    PH : float
        De begin waarde van de ph oftewel de zuurgragde voor het model
    startTime: int
         De begint tijd in uren
    endTime: int
        De eind tijd in uren voor het model
    typeG: int
        De type grafiek kiezen

    Attributs:
    _________
    get_name
        Slaat de naam van de bactria op
    get_temp
        Slaat de begin temperature op
    get_ph
        Slaat de PH graade op
    get_startTime
        Slaat de begin tijd voor de model op
    get_endTime
        Slaat de eind tijd voor het model op
    get_typeG
        Slaat de type grafiek voor het model op
         """

    #constructor
    def __init__(self, bacteriaName: str, temperature: float, pH: float, startTime: int, endTime: int, typeG: int):
        try:
            self.bact_name = bacteriaName
            self.temp = temperature
            self.ph = pH
            self.start_time = startTime
            self.end_time = endTime
            self.type_grafiek = typeG

        except ValueError as e:
            print("incorrect type of value was entered", e)

    # public methods
    @property
    def get_name(self):
        return self.bact_name

    @property
    def get_temp(self):
        return self.temp

    @property
    def get_ph(self):
        return self.ph

    @property
    def get_startTime(self):
        return self.start_time

    @property
    def get_endTime(self):
        return self.end_time

    @property
    def get_typeG(self):
        return self.type_grafiek


bacteriaNameInput = str(input("Welke bactrie?")).lower()
temperatureInput = int(input("Wat is het tempratuur?"))
pHInput = int(input("wat is de PH?"))
startTime = int(input("Wat is de begintijd in uren?"))
endTime = int(input("Wat is de eindtijd in uren?"))
typeG = int(input("Kies de soort berekneing \n 1.logstic \n 2.Gomptz"))
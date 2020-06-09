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


class Checkit:
    """"
        In dit class wordt de input van de user gecontroleerd of het een geldige input is voor de gevraagde waarde
        om de error messages duidelijker voor de gebruiker te maken
        Bron:
        https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response """

    def __init__(self,  type_=None, min_=None, max_=None):
        self.type_ = type_
        self.min_ = min_
        self.max_ = max_

    def sanitised_input(self, type_=None, min_=None, max_=None):
        if min_ is not None and max_ is not None and max_ < min_:
                raise ValueError("min_ must be less than or equal to max_.")
        while True:
                ui = input(self)
                if type_ is not None:
                    try:
                        ui = type_(ui)
                    except ValueError:
                        print("Input type must be {0}.".format(type_.__name__))
                        continue
                if max_ is not None and ui > max_:
                    print("Input must be less than or equal to {0}.".format(max_))
                elif min_ is not None and ui < min_:
                    print("Input must be greater than or equal to {0}.".format(min_))
                else:
                    return ui


bacteriaNameInput = Checkit.sanitised_input("Welke bactria?", str.lower)
temperatureInput = Checkit.sanitised_input("Wat is het tempratuur?", int)
pHInput = Checkit.sanitised_input("wat is de PH?", int)
startTime = Checkit.sanitised_input("Wat is de begintijd in uren?", int)
endTime = Checkit.sanitised_input("Wat is de eindtijd in uren?", int)
typeG = Checkit.sanitised_input("Kies de soort berekneing \n 1.logstic \n 2.Gomptz", int, 1, 2)

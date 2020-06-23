import numpy as np

from Code.JsonChecker import JsonChecker


class EndResults:
    """
    In this class, the intervals of growth of the bacteria are calculated using different formulas/equations that are
    specifically called in the class.
    There are a total of 4 different formulas/equations to calculate the growth of a bacterium.

    Parameters
    ----------
    bact_naam: String
        The name of a bacteria

    temp_input: Float
         The user input for the temperature

    ph_input: Float
         The user input of the PH

    end_time: Float
         The user input of end time

    type_graph: int
        The user choice for the equation / formulas

    Attributes
    ----------
     bact_naam: String
        Store the name of a bacteria

    temp_input: Float
         Store the user input for the temperature

    ph_input: Float
         Store the user input of the PH

    end_time: Float
         Store the user input of end time

    type_graph: int
        Store the user choice for the equation / formulas

    """
    def __init__(self, bact_naam: str, temp_input: float, ph_input: float, aw:float, end_time: float, type_graph: int):
        super().__init__(bact_naam, temp_input, ph_input, aw, end_time, type_graph)
        self.bact_naam = bact_naam
        self.temp_input = temp_input
        self.ph_input = ph_input
        self.aw = aw
        self.end_time = end_time
        self.type_graph = type_graph
        self.__new__()

    def __new__(cls, bact_naam: str, temp_input: float, ph_input: float, aw:float, end_time: float, type_graph: int) -> list:
        """
        Constructs based, got everything the same except that in the this method there is a return of the answer.
        Based on the type equation that the user chooses, calls a function.

        Raises
        --------
        ValueError
                when the check of the ph and the temperature returns a None

        Return
        --------
            list
                A list of the intervals of growth of the bacteria, that would be used by the plot of the graph

        """
        temp_check = JsonChecker(bact_naam, temp_input, ph_input, "temp", temp_input)
        temp_check_terug = temp_check.values_check()

        ph_check = JsonChecker(bact_naam, temp_input, ph_input, "ph", ph_input)
        ph_check_terug = ph_check.values_check()

        aw_check = JsonChecker(bact_naam, temp_input, ph_input, "aw", aw)
        aw_check_terug = aw_check.values_check()

        antwoord = 0
        try:
            if (temp_check_terug and ph_check_terug and aw_check_terug) is not None:
                if type_graph == 1:
                    antwoord = cls.logistic(cls,bact_naam, end_time, ph_input, temp_input)
                if type_graph == 2:
                    antwoord = cls.logstic_curve(cls, bact_naam,  end_time, ph_input, temp_input)
                if type_graph == 3:
                    antwoord = cls.log_growth(cls, bact_naam, end_time, ph_input, temp_input)
                if type_graph == 4:
                    antwoord= cls.temp_growth_rate(cls, bact_naam, ph_input, end_time, temp_check_terug)

                return antwoord
        except ValueError as e:
            print("incorrect type of value was entered", e)

    def new_growth_rate(self, bact_name: str, pH: float, temperature: float) -> list:
        """
        Here the growth factor is calculated at a certain temperature and ph value.
        Using the CTPM equation :

            μ max (T, pH) = CTPM(T, pH) = μ opt t(T)* p(pH)

            t(T)= (T - T MAX)(T - T MIN)**2 / (T opt 2 T min) [(Topt - Tmin)(T - Topt) - (Topt - Tmax) (Topt + Tmin - 2T)]

             p(pH) = (pH - pH min) (pH - pH max)/(pH - pH min)(pH - pH max) - (pH - pH opt) **2

        Return
        --------
            Float
                A float of the new growth rate

        """
        temp_check = JsonChecker(bact_name, temperature, pH, "temp", temperature)
        temp_waardes= temp_check.read_value_json()

        ph_check = JsonChecker(bact_name, temperature, pH, "ph", pH)
        pH_waardes = ph_check.read_value_json()

        groeisFcator = JsonChecker(bact_name, temperature, pH, "gr", None)
        groeisFcator_is = groeisFcator.read_value_json()

        # max growth rate(T, pH) = CTPM(T, pH)= optimum growth rate t(T) p(pH)

        # temerature t(T)
        # de noemer stukje 1
        tt = ((temp_waardes[1] - temp_waardes[0]) * (temperature - temp_waardes[1]) - (temp_waardes[1] - temp_waardes[2])
              * (temp_waardes[1] + temp_waardes[0] - 2 * temperature))

        # de noemer stukje 2
        tt2 = ((temp_waardes[1] - temp_waardes[0]) * tt)
        # de teller
        tt3 = ((temperature - temp_waardes[2]) * (temperature - temp_waardes[0]) ** 2 / tt2)

        # pH p(pH)
        # de noemer
        phh = ((pH - pH_waardes[0]) * (pH - pH_waardes[2]) - (pH - pH_waardes[1]) ** 2)
        # de teller
        phh2 = ((pH - pH_waardes[0]) * (pH - pH_waardes[2]) / phh)

        # new groei factor
        newgroeiFactor = groeisFcator_is[0] * tt3 * phh2

        return newgroeiFactor

    def log_growth(self, bact_name: str, time: float, pH: float, temperature: float) -> list:
        """
        This function calculates the growth of the bactria on the basis of 4 phases:
            Lag phase, logarithmic phase, the stationary phase and the death phase.
            Using this equation: Ln N -Ln N0 = μ *(t-t0)
                                where:
                                   μ stands for the growth rate per h^-1
                                   N stands for the number of CFU / ml at time t
                                   N0 stands for the initial number of CFU / ml at time t0
                                   t stands for time
        Parameters
        ----------
        bact_naam: String
            The name of a bacteria
        time: Float
             The user input of end time

        pH: Float
             The user input of the PH

        temperature: Float
             The user input for the temperature

        ant_lijst: List
             The list where the results of the algorithm are stored

        Return
        --------
            List
                A list of the intervals of growth of the bacteria, that would be used by the plot of the graph
        """

        ant_lijst, lijstDeath  = [], []
        beperkendeFactor = JsonChecker(bact_name, temperature, pH, "br", None)
        beperkendeFactor_is = beperkendeFactor.read_value_json()
        groeisFcator = JsonChecker(bact_name, temperature, pH, "gr", None)
        groeisFcator_is = groeisFcator.read_value_json()

        lnN0_ = JsonChecker(bact_name, temperature, pH, "bw", None)
        lnN0 = lnN0_.read_value_json()
        ant_lijst.append(lnN0[0])
        # beperkendeFactor = lnN0[0]*(np.exp(groeisFcator_is[0]* time))
        # print(beperkendeFactor)
        newgroeiFactor = EndResults.new_growth_rate(self, bact_name, pH, temperature)

        for t in range(0, int(time)+1):
            lnN = (newgroeiFactor * t) + (ant_lijst[-1])
            if lnN < beperkendeFactor_is[0]:
                ant_lijst.append(lnN)
            else:
                ant_lijst.append(beperkendeFactor_is[0])

        lijstDeath.append(beperkendeFactor_is[0])
        while lijstDeath[-1] >= lnN0[0]:
            antwoord= lijstDeath[-1] - (newgroeiFactor*len(lijstDeath))
            if antwoord >= lnN0[0]:
                 lijstDeath.append(antwoord)
            else:
                lijstDeath.append(lnN0[0])
                break

        for item in lijstDeath:
            ant_lijst.append(item)
        return ant_lijst

    def logistic(self, bact_name: str, time: float, pH: float, temperature: float) -> list:
        """
        This formula calculates the growth of the bacteria based on the logistics formula.
        Here the growth is calculated until reaching the limiting factor.
            Using the formula:
                    y(t) = limiting factor/ (1+ initial value* exp^(-growth rate *t ))

        Return
        --------
            List
                 A list of the intervals of growth of the bacteria, that would be used by the plot of the graph
        """
        ant_lijst = []
        groeisFcator = EndResults.new_growth_rate(self, bact_name, pH, temperature)
        beperkendeFactor = JsonChecker(bact_name, temperature, pH, "br", None)
        beperkendeFactor_is = beperkendeFactor.read_value_json()
        begingValue_is = JsonChecker(bact_name, None, None, "bw", None)
        begingValue = begingValue_is.read_value_json()

        for t in range(0, int(time) + 1):
            ant = (beperkendeFactor_is[0] / (1 + begingValue[0] * np.exp(-groeisFcator * t)))
            if ant <= beperkendeFactor_is[0]:
                ant_lijst.append(ant)
        return ant_lijst

    def logstic_curve(self, bact_name: str, time: float, pH: float, temperature: float )-> list:
        """
        This formula use the logistic formula to calculate the growth until the limiting factor.
        Then it would calculate the death phase of the bacteria.

        Return
        --------
            List
                A list of the intervals of growth of the bacteria, that would be used by the plot of the graph
        """
        list = EndResults.logistic(self, bact_name, time, pH, temperature)
        groeisFcator = EndResults.new_growth_rate(self, bact_name, pH, temperature)
        beperkendeFactor = JsonChecker(bact_name, temperature, pH, "br", None)
        beperkendeFactor_is = beperkendeFactor.read_value_json()
        lijstDeath = []
        lijstDeath.append(beperkendeFactor_is[0])

        while lijstDeath[-1] >= list[0]:
        # zolang de deathwaarde grooter of glijk is aan de beginwaarde van de groei is:
            antwoord = lijstDeath[-1] - (groeisFcator * len(lijstDeath))
            if antwoord <= beperkendeFactor_is[0]:
                # als de antwoord niet gelijk of groter aan de beperkende factor is
                lijstDeath.append(antwoord)
            else:
                lijstDeath.append(beperkendeFactor_is[0])
                break

        for item in lijstDeath:
            list.append(item)
        return list

    def temp_growth_rate(self, bact_name: str, pH: float, end_time: float, temp_check:list, ) -> list:
        """
        This formula calculates the growth factor per temperature difference. the temperature rises one grade up every
         hour, until the max temperature is reached.
         The temperatures are shown on the x-axis and the growth factors on the y-axis.

           Using the function : new_growth_rate

         Return
         ------
            list
                 A list with growth factors that were calculated in the algorithm
         """

        beginRange, eindRange = 0, 0
        list = []
        tijd_lijst = []
        if temp_check is not None:
            if len(temp_check) == 3:
                beginRange = temp_check[0]
                eindRange = temp_check[2] + 1

            elif len(temp_check) == 2:
                beginRange = temp_check[0]
                eindRange = temp_check[1] + 1

            elif len(temp_check) == 1:
                beginRange = temp_check[0]
                eindRange = temp_check[0] + 1

        begingValue_is = JsonChecker(bact_name, None, None, "bw", None)
        begingValue = begingValue_is.read_value_json()

        beperkingsFactor_is = JsonChecker(bact_name, None, None, "br", None)
        beperkingsFactor = beperkingsFactor_is.read_value_json()
        groei_lijst = []

        for time in range(0, int(end_time)+1):
            tijd_lijst.append(time)
        for temp in range(int(beginRange), int(eindRange)+1):
            if list:
                if list[-1] <= beperkingsFactor[0]:
                    if tijd_lijst:
                        groeisFactor = EndResults.new_growth_rate(self, bact_name, pH, temp)
                        groei_lijst.append(groeisFactor)
                        list.append(beperkingsFactor[0] / (1 + begingValue[0] * np.exp(-groeisFactor * tijd_lijst[0])))
                        tijd_lijst.pop(0)
            else:
                list.append(0)
        return groei_lijst

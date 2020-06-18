import numpy as np

from Code.JsonChecker import JsonChecker


class EndResults:
    def __init__(self, bact_naam: str, temp_input: float, ph_input:float, end_time: float, type_graph: int):
        super().__init__(bact_naam, temp_input, ph_input, end_time, type_graph)
        self.bact_naam = bact_naam
        self.tem_input = temp_input
        self.ph_input = ph_input
        self.end_time = end_time
        self.type_graph = type_graph
        self.__new__()

    def __new__(cls, bact_naam: str, temp_input: float, ph_input: float, end_time: float, type_graph: int):
        temp_check = JsonChecker(bact_naam, temp_input, ph_input, "temp", temp_input)
        temp_check_terug = temp_check.values_check()

        ph_check = JsonChecker(bact_naam, temp_input, ph_input, "ph", ph_input)
        ph_check_terug = ph_check.values_check()

        if (temp_check_terug and ph_check_terug) is not None:
            if type_graph == 1:
                antwoord = cls.logistic( cls, bact_naam, end_time, ph_input, temp_input)
            if type_graph == 2:
                antwoord = cls.logstic_curve(cls, bact_naam,  end_time, ph_input, temp_input)
            if type_graph == 3:
                antwoord = cls.log_growth(cls, bact_naam, end_time, ph_input, temp_input)
            if type_graph ==4 :
                antwoord= cls.temp_logistic(cls, bact_naam, ph_input, end_time, temp_check_terug)
            # print("we got this temp after the value check ", temp_check_terug)
            # print("we got this ph after the value check ", ph_check_terug)
            return antwoord
        else:
            raise ValueError("incorrect type of value was entered")

    def new_groeigrowth(self, bact_name: str, pH: float, temerature: float):
        temp_check = JsonChecker(bact_name, temerature, pH, "temp", temerature)
        temp_waardes= temp_check.read_json()

        ph_check = JsonChecker(bact_name, temerature, pH, "ph", pH)
        pH_waardes = ph_check.read_json()

        groeisFcator = JsonChecker(bact_name, temerature, pH, "gr", None)
        groeisFcator_is = groeisFcator.read_json()

        # max growth rate(T, pH) = CTPM(T, pH)= optimum growth rate t(T) p(pH)

        # temerature t(T)
        # de noemer stukje 1
        tt = ((temp_waardes[1] - temp_waardes[0]) * (temerature - temp_waardes[1])
              - (temp_waardes[1] - temp_waardes[2])
              * (temp_waardes[1] + temp_waardes[0] - 2 * temerature))

        # de noemer stukje 2
        tt2 = ((temp_waardes[1] - temp_waardes[0]) * tt)
        # de teller
        tt3 = ((temerature - temp_waardes[2]) * (temerature - temp_waardes[0]) ** 2 / tt2)

        # pH p(pH)
        # de noemer
        phh = ((pH - pH_waardes[0]) * (pH - pH_waardes[2]) - (pH - pH_waardes[1]) ** 2)
        # de teller
        phh2 = ((pH - pH_waardes[0]) * (pH - pH_waardes[2]) / phh)

        # new groei factor
        newgroeiFactor = groeisFcator_is[0] * tt3 * phh2

        return newgroeiFactor

    def log_growth(self, bact_name: str, time: float, pH: float, temerature: float, lijst = [], lijstDeath = []) -> np.array:

        """Lag-fase: de periode die verloopt voordat de vermeerdering van de bacteriecellen begint;
          logaritmische fase: de periode, waarin de feitelijke groei plaatsvindt, hierbij verdubbelt het
                              aantal zich elke generatietijd
          de stationaire fase: de periode, waarin het aantal levende cellen per ml constant blijft
          afstervingsfase:de periode, waarin het aantal levende cellen per ml afneemt
         Ln N -Ln N0 = growth rate *(t-t0)
         Ln N0 is de inoclum biomass oftewel de begincellen/culture in CFU/ml
         Growth rate is de groeisfactor, staat in de json file van de bactrie
         Beperkende factor is in dit geval de max aantaal cellen die gemaakt kunnen worden in XX C tempratuur.
         M is de max biomass = M(t)- M(0)
         De cijfers voor bactrie XX komen uit een onderzoek die in de bronnen(3) vermeld staat."""


        beperkendeFactor = JsonChecker(bact_name, temerature, pH, "br", None)
        beperkendeFactor_is = beperkendeFactor.read_json()

        lnN0_ = JsonChecker(bact_name, temerature, pH, "bw", None)
        lnN0 = lnN0_.read_json()
        lijst.append(lnN0[0])

        newgroeiFactor = EndResults.new_groeigrowth(self, bact_name, pH, temerature)

        for t in range(0, int(time)+1):
            lnN = (newgroeiFactor * t) + (lijst[-1])
            if lnN < beperkendeFactor_is[0]:
                lijst.append(lnN)
            else:
                lijst.append(beperkendeFactor_is[0])
        M = max(lijst) - min(lijst)

        lijstDeath.append(beperkendeFactor_is[0])
        while lijstDeath[-1] >= lnN0[0]:
            antwoord= lijstDeath[-1] - (newgroeiFactor*len(lijstDeath))
            if antwoord >= lnN0[0]:
                 lijstDeath.append(antwoord)
            else:
                lijstDeath.append(lnN0[0])
                break

        for item in lijstDeath:
            lijst.append(item)
        return lijst

    def logistic(self, bact_name: str, time: float, pH: float, temerature: float, list =[]) -> np.array:
        """"c = is de beperkende factor, kan tempratuur, ph of max aantaal cellen zijn
          b= is de groeifactor
          a = is de beginwaarde
          De gebuikte formule komt uit een atrtikel die in de bronnen(1) vermeld staat"""""

        groeisFcator = EndResults.new_groeigrowth(self, bact_name, pH, temerature)
        beperkendeFactor = JsonChecker(bact_name, temerature, pH, "br", None)
        beperkendeFactor_is = beperkendeFactor.read_json()
        begingValue_is = JsonChecker(bact_name, None, None, "bw", None)
        begingValue = begingValue_is.read_json()

        for t in range(0, int(time) + 1):
            ant = (beperkendeFactor_is[0] / (1 + begingValue[0] * np.exp(-groeisFcator * t)))
            if ant <= beperkendeFactor_is[0]:
                list.append(ant)
        return list

    def logstic_curve(self, bact_name: str, time: float, pH: float, temerature: float, lijstDeath=[]):
        list = EndResults.logistic(self, bact_name, time, pH, temerature)
        groeisFcator = EndResults.new_groeigrowth(self, bact_name, pH, temerature)
        beperkendeFactor = JsonChecker(bact_name, temerature, pH, "br", None)
        beperkendeFactor_is = beperkendeFactor.read_json()
        begingValue = JsonChecker(bact_name, None, None, "bw", None)
        begingValue_is = begingValue.read_json()
        lijstDeath.append(beperkendeFactor_is[0])

        while lijstDeath[-1] >= list[0]:
            antwoord = lijstDeath[-1] - (groeisFcator * len(lijstDeath))
            if antwoord <= beperkendeFactor_is[0]:
                lijstDeath.append(antwoord)
            else:
                lijstDeath.append(beperkendeFactor_is[0])
                break

        for item in lijstDeath:
            list.append(item)
        return list


    def temp_logistic(self, bact_name: str, pH, end_time: float, temp_check:list, list = []):
        """hier moet de grafiek van de growth getekend, in verglijking met de tempratuur verandering per uur
             begint bij de min temp en eindigt bij de max
             De gebruikt formule komt uit een atrikel die in de bronnen(2) vermeld staat """

        beginRange, eindRange = 0, 0
        print(temp_check)

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

        begingValue_is = JsonChecker(bact_name, None, None,"bw", None)
        begingValue = begingValue_is.read_json()
        print(beginRange, eindRange)
        for time in range(0, int(end_time)+1):
            for temp in range(int(beginRange), int(eindRange+1)):
                if list:
                    if list[-1] != eindRange:
                        groeisFactor = EndResults.new_groeigrowth(self, bact_name, pH,temp)
                        list.append(eindRange / (1 + begingValue[0] * np.exp(-groeisFactor * time)))
                        print(list)
                else:
                    list.append(0)
        return list
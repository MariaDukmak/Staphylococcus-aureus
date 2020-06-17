import numpy as np

from Code.JsonChecker import JsonChecker


class EndResults(JsonChecker):
    def __init__(self, bact_input, tem_input, ph_input, endTime: float, typeG: int):
        super().__init__(bact_input, tem_input, ph_input, endTime, typeG)
        self.bact_input = bact_input
        self.tem_input = tem_input
        self.ph_input = ph_input
        self.endTime = endTime
        self.typeG = typeG
        self.__new__()

    def __new__(cls,  bact_input, tem_input, ph_input, endTime: float, typeG: int):
        temp_check = JsonChecker(bact_input, tem_input, ph_input, "temp", tem_input)
        temp_check_terug = temp_check.values_check()

        ph_check = JsonChecker(bact_input, tem_input, ph_input, "ph", ph_input)
        ph_check_terug = ph_check.values_check()

        if (temp_check_terug and ph_check_terug) is not None:
            if typeG == 1:
                antwoord = cls.logistic( cls, bact_input, endTime, ph_input, tem_input)
            if typeG == 2:
                antwoord = cls.temp_logistic(cls, bact_input, temp_check_terug)
            if typeG == 3:
                antwoord = cls.log_growth(cls, bact_input, endTime, ph_input, tem_input)
            print("we got this temp after the value check ", temp_check_terug)
            print("we got this ph after the value check ", ph_check_terug)
            print(antwoord)
            return antwoord
        else:
            raise ValueError("incorrect type of value was entered")

    def log_growth(self, bact_name, time,  pH:float, temerature:float, lijst=[]):

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


        #https://aem.asm.org/content/aem/61/2/610.full.pdf
        #lnN0 = self.read_json(self, bact_name, "bw")
        #groeisFactor = self.read_json(self, bact_name, "gr")
        #beperkendeFactor = self.read_json(self, bact_name, "br")
        temp_check = JsonChecker(bact_name, temerature, pH, "temp", temerature)
        temp_waardes= temp_check.read_json()

        ph_check = JsonChecker(bact_name, temerature, pH, "ph", pH)
        pH_waardes = ph_check.read_json()
        groeisFcator = JsonChecker(bact_name, temerature, pH, "gr", None)
        groeisFcator_is = groeisFcator.read_json()
        beperkendeFactor = JsonChecker(bact_name, temerature, pH, "br", None)
        beperkendeFactor_is = beperkendeFactor.read_json()

        lnN0_ = JsonChecker(bact_name, temerature, pH, "bw", None)
        lnN0 = lnN0_.read_json()
        lijst.append(lnN0[0])

        # max growth rate(T, pH) = CTPM(T, pH)= optimum growth rate t(T) p(pH)

        # temerature t(T)
        tt = ((temp_waardes[1]-temp_waardes[0])*(temerature - temp_waardes[1])
              - (temp_waardes[1] - temp_waardes[2])
              * (temp_waardes[1] + temp_waardes[0] - 2*temerature)) # de noemer stukje 1

        tt2 = ((temp_waardes[1] - temp_waardes[0]) * tt) # de noemer stukje 2
        tt3 = ((temerature - temp_waardes[2])*(temerature - temp_waardes[0])**2 / tt2) # de teller

        # pH p(pH)
        phh = ((pH - pH_waardes[0])*(pH-pH_waardes[2]) - (pH - pH_waardes[1])**2) # de noemer
        phh2 = ((pH - pH_waardes[0])*(pH-pH_waardes[2])/phh) # de teller

        # new groei factor
        newgroeiFactpr = groeisFcator_is[0] * tt3 * phh2

        for t in range(0, int(time)+1):
            lnN = (newgroeiFactpr * t) + lnN0[0]
            if lnN < beperkendeFactor_is[0]:
                lijst.append(lnN)
            else:
                lijst.append(beperkendeFactor_is[0])
        M = max(lijst) - min(lijst)

        lijst2 = [int(item) for item in lijst[::-1] if int(item) != int(lnN0[0])]
        unique = [x for i, x in enumerate(lijst2) if i == lijst2.index(x)]

        for item in unique:
            lijst.append(item)
        return np.array(lijst)

    def logistic(self, bact_name: str, time: float, pH: float, temerature: float, list=[], ):
        """"c = is de beperkende factor, kan tempratuur, ph of max aantaal cellen zijn
          b= is de groeifactor
          a = is de beginwaarde
          De gebuikte formule komt uit een atrtikel die in de bronnen(1) vermeld staat"""""


        #[min_item, optimum_item, max_item]
        groeisFcator = JsonChecker(bact_name, temerature, pH,"gr", None)
        groeisFcator_is = groeisFcator.read_json()
        beperkendeFactor = JsonChecker(bact_name, temerature, pH,"br", None)
        beperkendeFactor_is = beperkendeFactor.read_json()

        groeisFcator = JsonChecker(bact_name, temerature, pH, "gr", None)
        groeisFcator_is = groeisFcator.read_json()

        begingValue_is = JsonChecker(bact_name, None, None, "gr", None)
        begingValue = begingValue_is.read_json()

        for t in range(0, int(time) + 1):
            list.append(beperkendeFactor_is[0]/ (1 + begingValue[0] * np.exp(-groeisFcator_is[0] * t)))
        return np.array(list)


    def temp_logistic(self, bact_name: str, temp_check:list, list = []):
        """hier moet de grafiek van de growth getekend, in verglijking met de tempratuur verandering per uur
             begint bij de min temp en eindigt bij de max
             De gebruikt formule komt uit een atrikel die in de bronnen(2) vermeld staat """

        beginRange, eindRange = 0, 0
        groeisFactor_is = JsonChecker(bact_name, None, None ,"gr", None)
        groeisFactor = groeisFactor_is.read_json()

        if temp_check is not None:
            if len(temp_check) == 3:
                beginRange = temp_check[0]
                eindRange = temp_check[2] + 1
                # optimum?? moeten iets ermee doen
            elif len(temp_check) == 2:
                beginRange = temp_check[0]
                eindRange = temp_check[1] + 1

            elif len(temp_check) == 1:
                beginRange = temp_check[0]
                eindRange = temp_check[0] + 1

        #begingValue = self.read_json(self, bact_name, "bw")
        begingValue_is = JsonChecker(bact_name, None, None,"bw", None)
        begingValue = begingValue_is.read_json()
        for temp in range(int(beginRange), int(eindRange+1)):
            if list:
                if list[-1] != eindRange:
                    list.append(eindRange / (1 + begingValue[0] * np.exp(-groeisFactor[0] * temp)))
                else:
                    print(np.array(list))
                    return np.array(list)
            else:
                list.append(eindRange / (1 + begingValue [0]* np.exp(-groeisFactor[0] * temp)))
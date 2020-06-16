
import numpy as np

from Code.JsonChecker import JsonChecker


# s-aureus

class EndResult(JsonChecker):
    def __init__(self, bactName:str, temperature: float, pH: float, endTime: float, typeG: int):
        super().__init__(bactName, temperature, pH, endTime, typeG)

    def logistic(self, bact_name: str, time: float, pH:float, temerature:float, list=[],):
        """"c = is de beperkende factor, kan tempratuur, ph of max aantaal cellen zijn
          b= is de groeifactor
          a = is de beginwaarde
          De gebuikte formule komt uit een atrtikel die in de bronnen(1) vermeld staat"""""
        #[min_item, optimum_item, max_item]
        groeisFcator = self.read_json(self, bact_name, "gr")
        beperkendeFactor = self.read_json(self, bact_name, "br")
        beginWaarde = self.read_json(self, bact_name, "bw")
        temp_waardes = self.read_json(self, bact_name, "temp")
        pH_waardes = self.read_json(self, bact_name, "ph")

        # tt = ((temp_waardes[1]-temp_waardes[0])*(temerature - temp_waardes[1]) - (temp_waardes[1]- temp_waardes[2])
        #       *(temp_waardes[1] + temp_waardes[0] - 2*temerature))
        # tt2 = ((temp_waardes[1] - temp_waardes[0]) * tt)
        # tt3 = ((temerature - temp_waardes[2])*(temerature - temp_waardes[0])**2 / tt2)
        # print("tt3", tt3)
        #
        # phh = ((pH -pH_waardes[0])*(pH-pH_waardes[2]) - (pH -pH_waardes[1])**2)
        # phh2 = ((pH -pH_waardes[0])*(pH-pH_waardes[2])/phh)
        #
        # print("phh2", phh2)
        # newgroeiFactpr = groeisFcator[0]*tt3 * phh2
        # print(newgroeiFactpr)

        for t in range(0, int(time) + 1):
            list.append(beperkendeFactor/ (1 + beginWaarde[0] * np.exp(-groeisFcator[0] * t)))
        return np.array(list)


    def temp_logistic(self, bact_name: str, temp_check:list, list = []):
        """hier moet de grafiek van de growth getekend, in verglijking met de tempratuur verandering per uur
             begint bij de min temp en eindigt bij de max
             De gebruikt formule komt uit een atrikel die in de bronnen(2) vermeld staat """

        beginRange, eindRange = 0, 0
        groeisFactor = self.read_json(self, bact_name, "gr")

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

        begingValue = self.read_json(self, bact_name, "bw")

        for temp in range(int(beginRange), int(eindRange+1)):
            if list:
                if list[-1] != eindRange:
                    list.append(eindRange / (1 + begingValue[0] * np.exp(-groeisFactor[0] * temp)))
                else:
                    print(np.array(list))
                    return np.array(list)
            else:
                list.append(eindRange / (1 + begingValue [0]* np.exp(-groeisFactor[0] * temp)))


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
        lnN0 = self.read_json(self, bact_name, "bw")
        growthrate = self.read_json(self, bact_name, "gr")
        beperkendeFactor = self.read_json(self, bact_name, "br")
        temp_waardes = self.read_json(self, bact_name, "temp")
        pH_waardes = self.read_json(self, bact_name, "ph")
        lijst.append(lnN0[0])

        tt = ((temp_waardes[1]-temp_waardes[0])*(temerature - temp_waardes[1]) - (temp_waardes[1] - temp_waardes[2])
              * (temp_waardes[1] + temp_waardes[0] - 2*temerature))
        tt2 = ((temp_waardes[1] - temp_waardes[0]) * tt)
        tt3 = ((temerature - temp_waardes[2])*(temerature - temp_waardes[0])**2 / tt2)
        print("tt3", tt3)

        phh = ((pH - pH_waardes[0])*(pH-pH_waardes[2]) - (pH - pH_waardes[1])**2)
        phh2 = ((pH - pH_waardes[0])*(pH-pH_waardes[2])/phh)

        print("phh2", phh2)
        newgroeiFactpr = growthrate[0]*tt3 * phh2
        print(newgroeiFactpr)

        for t in range(0, int(time)+1):
             lnN = (newgroeiFactpr * t) + lnN0[0]
             if lnN < beperkendeFactor[0]:
                lijst.append(lnN)
             else:
                 lijst.append(beperkendeFactor[0])
        M = max(lijst) - min(lijst)

        lijst2 = [int(item) for item in lijst[::-1] if int(item) != int(lnN0[0])]
        unique = [x for i, x in enumerate(lijst2) if i == lijst2.index(x)]

        for item in unique:
            lijst.append(item)
        return np.array(lijst)

    @classmethod
    def growth_endresult(self, bact_input, tem_input,ph_input, end_time, typeG):
        temp_check = self.values_check(self, bact_input, tem_input, "temp")
        ph_check = self.values_check(self, bact_input, ph_input, "ph")
        if (temp_check and ph_check) is not None:
            if typeG == 1:
                antwoord = self.logistic(self, bact_input, end_time, ph_input, tem_input)
            if typeG == 2:
                antwoord = self.temp_logistic(self, bact_input, temp_check)
            if typeG == 3:
                antwoord = self.log_growth(self, bact_input, end_time,ph_input, tem_input)
            print("we got this temp after the value check ", temp_check)
            print("we got this ph after the value check ", ph_check)
            return antwoord
        else:
            raise ValueError("incorrect type of value was entered")

import json

class JsonChecker:
    def __init__(self, bacteriaName: str, temperature: float, pH: float, startTime: int, endTime: float, typeG: float):
        super().__init__(bacteriaName, temperature, pH, startTime, endTime, typeG)

    def json_lezen(self, b: str, item: str):
        try:
            with open(b + ".json", "r") as f:
                info = json.load(f)
                optimum_item = info["env-info"][item][item]
                max_item = info["env-info"][item]["max"]
                min_item = info["env-info"][item]["min"]
                return [optimum_item, max_item, min_item]
        except KeyError as e:
            return [optimum_item]

    def waardes_check(self, bestand: str, inputWaarde: float, item: str):

        """"Hier wordt de input van de user voor de omstandigheden van de groei zoals:
            PH en de  tempatruur gechechet.Er wordt gekeken of de input waarde grooter,
            gelijk of kleiner dan de optimum waarde is.
                    - Als de waarder gelijk is aan de optimum, dan zou de groei op dat punt het snelleste zijn.
                        Hiervoor hebben we de optimum en de max waarde nodig

                    - Als de waarde gelijk is aan de max, dan zou de groei niet/heel langzaam zijn.
                        Hiervoor hebben we de max nodig

                    - Als de waarde gelijk is aan de min, dan zou de groei laangzaam zijn, maar gaat wel sneller worden.
                        Hiervoor hebben we de max, optimum en de min nodig.
        """
        try:
            values = self.json_lezen(self, bestand, item)
            if values[0] == inputWaarde:
                return [inputWaarde, values[1]]
            elif values[1] == inputWaarde or values[2] <= inputWaarde <= values[1]:
                return [inputWaarde]
            elif values[2] == inputWaarde:
                return [inputWaarde, values[0], values[1]]
            else: # TODO: laat de error op een andere manier en niet alles kapot maken
                print(f"incorrect type of value was entered {inputWaarde}")

        # handle exceptions
        except AttributeError as e:
            print("The json does not contain objects ", e)
        except ValueError as e:
            print("No iterable type is given", e)
        except Exception as e:
            print("Unexpected error while generating the ranking dictionary", e)
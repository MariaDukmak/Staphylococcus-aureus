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
        try:
            values = self.json_lezen(self, bestand, item)
            if (values[2] <= inputWaarde <= values[1]) or (inputWaarde == values[0]):
                return[inputWaarde, values[1]]
            #else: # TODO: laat de error op een andere manier en niet alles kapot maken
               # raise ValueError("incorrect type of value was entered {}".format(inputWaarde))
        # handle exceptions
        except AttributeError as e:
            print("The json does not contain objects of the class Ranking\n", e)
        except ValueError as e:
            print("No iterable type is given\n", e)
        except Exception as e:
            print("Unexpected error while generating the ranking dictionary\n", e)
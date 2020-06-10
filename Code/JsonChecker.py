# TODO: pas de error bij waardes_check aan

import json

class JsonChecker:
    def __init__(self, bacteriaName: str, temperature: float, pH: float, startTime: int, endTime: float, typeG: float):
        super().__init__(bacteriaName, temperature, pH, startTime, endTime, typeG)

    def read_json(self, b: str, item: str):
        try:
            with open(b + ".json", "r") as f:
                info = json.load(f)
                optimum_item = info["env-info"][item][item]
                max_item = info["env-info"][item]["max"]
                min_item = info["env-info"][item]["min"]
                return [optimum_item, max_item, min_item]
        except KeyError as e:
            return [optimum_item]

    def values_check(self, bestand: str, inputWaarde: float, item: str):

        """"Here the input of the user is checked for the conditions of growth such as: PH and the temperature.
            It is examined whether the input value is greater, equal or smaller than the optimum value.

            - If the value is equal to the optimum, the growth at that point would be the fastest.
                     For this we need the optimum and the max value
            - If the value is equal to the max, the growth would be not / very slow.
                    For this we need the max
            - If the value is equal to the minus, the growth would be slow, but it will get faster.
                         For this we need the max, optimum and the min.
        """
        try:
            values = self.read_json(self, bestand, item)
            if values[0] == inputWaarde:
                return [inputWaarde, values[1]]
            elif values[1] == inputWaarde or values[2] <= inputWaarde <= values[1]:
                return [inputWaarde]
            elif values[2] == inputWaarde:
                return [inputWaarde, values[0], values[1]]
            else:
                print(f"incorrect type of value was entered {inputWaarde}")

        # handle exceptions
        except AttributeError as e:
            print("The json does not contain that object ", e)
        except ValueError as e:
            print("No iterable type is given", e)
        except Exception as e:
            print("Unexpected error ", e)
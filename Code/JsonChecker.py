
import json


class JsonChecker:
    def __init__(self, bacteriaName: str, temperature: float, pH: float, item: str, inputWaarde: float):
        self.bacteriaName = bacteriaName
        self.temperature = temperature
        self.pH = pH
        self.item = item
        self.inputWaarde = inputWaarde

    def read_json(self):
        try:
            with open(self.bacteriaName + ".json", "r") as f:
                info = json.load(f)
                optimum_item = info["env-info"][self.item][self.item]
                max_item = info["env-info"][self.item]["max"]
                min_item = info["env-info"][self.item]["min"]
                return [min_item, optimum_item, max_item]
        except KeyError as e:
            return [optimum_item]

        except FileNotFoundError as e:
            return "File not found"

    def values_check(self):

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
            values = self.read_json()
            print("values", values)
            if len(values) == 3:
                if values[2] == self.inputWaarde:
                    return [self.inputWaarde]
                elif values[0] == self.inputWaarde or (values[0] <= self.inputWaarde <= values[1] and self.inputWaarde != values[1]):
                    return [self.inputWaarde, values[1], values[2]]
                elif values[1] == self.inputWaarde or (self.inputWaarde> values[1] and self.inputWaarde != values[2]):
                    return [self.inputWaarde, values[2]]
                else:
                    print(f"incorrect type of value was entered {self.inputWaarde}")
            elif len(values) == 1:
                if self.inputWaarde == values[0]:
                    return self.inputWaarde
        # handle exceptions
        except AttributeError as e:
            print("The json does not contain that object ", e)
        except ValueError as e:
            print("No iterable type is given", e)
        except Exception as e:
            print("Unexpected error ", e)

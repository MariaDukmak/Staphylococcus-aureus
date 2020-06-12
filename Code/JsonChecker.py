
import json


class JsonChecker:
    def __init__(self, bacteriaName: str, temperature: float, pH: float):
        super().__init__(bacteriaName, temperature, pH)

    def read_json(self, b: str, item: str):
        try:
            with open(b + ".json", "r") as f:
                info = json.load(f)
                optimum_item = info["env-info"][item][item]
                max_item = info["env-info"][item]["max"]
                min_item = info["env-info"][item]["min"]
                return [min_item, optimum_item, max_item]
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
            if len(values) == 3:
                if values[2] == inputWaarde:
                    return [inputWaarde]
                elif values[0] == inputWaarde or (values[1] > inputWaarde > values[2] and inputWaarde != values[2]):
                    return [inputWaarde, values[1], values[2]]
                elif values[1] == inputWaarde or (inputWaarde> values[1] and inputWaarde != values[2]):
                    return [inputWaarde, values[2]]
                else:
                    print(f"incorrect type of value was entered {inputWaarde}")
            elif len(values) == 1:
                if inputWaarde == values[0]:
                    return inputWaarde
        # handle exceptions
        except AttributeError as e:
            print("The json does not contain that object ", e)
        except ValueError as e:
            print("No iterable type is given", e)
        except Exception as e:
            print("Unexpected error ", e)

import json


class JsonChecker:
    """
    A JsonCheker object can be read from a json file. and compared with the user's input.

    Parameters
    ----------
    bacteria_name: String
         The name of the bacteria

    temperature: Float
         The user input for the temperature

    pH: Float
        The user input of the PH

    item: String
        The item that would be read from the json file

    inputWaarde: Float
        The input value that would be chacked, could be temperature or PH

    Attributes
    ----------

    bacteria_name: String
         Stores the name of the bacteria

    temperature: Float
         Stores the user input for the temperature

    pH: Float
        Stores the user input of the PH

    item: String
        Stores the item that would be read from the json file

    inputWaarde: Float
        Stores the input value that would be chacked, could be temperature or PH
    """

    # the constructor
    def __init__(self, bacteria_name: str, temperature: float, pH: float, item: str, inputWaarde: float):
        try:
            self.bacteria_name = bacteria_name
            self.temperature = temperature
            self.pH = pH
            self.item = item
            self.inputWaarde = inputWaarde
        except ValueError:
            print("incorrect variable type was entered")

    def read_value_json(self):
        """
        Opens a json file based on the bacteria name and reads the requested values.

        Raises
        ------
        KeyError
            when the key is not under "env-info", like aw value.

        FileNotFoundError
            when the file name (the bacteria name) not found.

        Returns
        -------
            list
                A list with the read values from the json file. In the order:
                    [min, optimum, max] or only [optimum]
        """
        try:
            with open("../json bestanden/" + self.bacteria_name + ".json", "r") as f:
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

        """"
        Here the input of the user is checked for the conditions of growth such as: PH , aw and the temperature.
            It is examined whether the input value is greater, equal or smaller than the optimum value.

            - If the value is equal to the optimum, the growth at that point would be the fastest.
                     For this we need the optimum and the max value
            - If the value is equal to the max, the growth would be not / very slow.
                    For this we need the max
            - If the value is equal to the minus, the growth would be slow, but it will get faster.
                         For this we need the max, optimum and the min.

        Raises
        --------
        Exception
            When an unexpected error happens

        Returns
        -------
        list
            A list with the required values based on the explanation above
        """
        try:
            values = self.read_value_json()
            if len(values) == 3:
                if values[2] == self.inputWaarde:
                    return [self.inputWaarde]
                elif values[2]< self.inputWaarde or values[0]> self.inputWaarde:
                    return None
                elif values[0] == self.inputWaarde or (values[0] <= self.inputWaarde <= values[1] and self.inputWaarde != values[1]):
                    return [self.inputWaarde, values[1], values[2]]
                elif values[1] == self.inputWaarde or (values[1] < self.inputWaarde < values[2] and self.inputWaarde != values[2]):
                    return [self.inputWaarde, values[2]]
                elif values[2] < self.inputWaarde:
                    return [0.0]
            elif len(values) == 1:
                if self.inputWaarde == values[0]:
                    return [self.inputWaarde]
                else:
                    return None
        # handle exceptions
        except Exception as e:
            print("Unexpected error ", e)

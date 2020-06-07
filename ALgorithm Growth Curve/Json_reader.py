
import json


class Info_json(): #werkt
    def __init__(self, file_name, user_input):
        super().__init__(file_name, user_input)

    def find(self, file_name, user_input):
        try:
            with open(file_name + ".json", "r") as f:
                info = json.load(f)
                optimum_item = info["env-info"][user_input][user_input]
                max_item = info["env-info"][user_input]["max"]
                min_item = info["env-info"][user_input]["min"]
                print(optimum_item, max_item, max_item)
                return [optimum_item, max_item, min_item]

        except ValueError as e:
            return [optimum_item]


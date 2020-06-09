import json

from Code import InputVrager as ip

b= ip.bacteriaNameInput

def waardes_check(b, t, w):
    values = json_lezen(b, w)
    if (values[2] <= t <= values[1]) or (t == values[0]):
        return [t, values[1]]
    else:
        print("Deze t is ongeldig in de json bestand van de bactrie")


def json_lezen(b, item):
    try:
        with open(b + ".json", "r") as f:
            info = json.load(f)
            optimum_item = info["env-info"][item][item]
            max_item = info["env-info"][item]["max"]
            min_item = info["env-info"][item]["min"]
            return [optimum_item, max_item, min_item]
    except KeyError as e:
        return [optimum_item]


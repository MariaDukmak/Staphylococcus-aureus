"""This is a modelation for the growth for Staphylococcus aureus bactrie """
import json
import numpy as np
import matplotlib.pyplot as plt

#    s-aureus


def inputs():
    bact_input = str(input("Welke bactrie?"))
    tem_input = int(input("Wat is het tempratuur?"))
    ph_input = int(input("wat is de ph?"))
    tijd1_input = int(input("Wat is de begintijd in uren?"))
    tijd2_input = int(input("Wat is de eindtijd in uren?"))

    x= np.linspace(tijd1_input, tijd2_input, 11)
    y = growth_endresult(bact_input, tijd1_input, tijd2_input, tem_input, ph_input)
    plt.plot(x,y)
    plt.show()


def growth_endresult(bact, t1, t2, temp_input, ph_input):
    temp = waardes_check(bact, temp_input, "temp")
    phh = waardes_check(bact, ph_input, "ph")
    x= my_logstic([t1, t2], 9999999999999999999999999999, 2, 10000000000000000000000000000)
    return x

def my_logstic(t, a, b, c):
    """c is the max : 1000
    initial value: we start at 1 so, c/(a+1)= 1 , 1000/(1+a)=1 , a = 999
    the growth rate: b = 2
    time: we start at 0 end at 10 hours"""
    lijst = []
    print(t[0], t[1])
    for time in range(t[0], t[1]+1):
        lijst.append(c / (1+a * np.exp(-b*time)))
    return np.array(lijst)


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
    except:
        return [optimum_item]


def main():
    if __name__ == "__main__":
        inputs()


main()

"""This is a modelation for the growth for Staphylococcus aureus bactrie """


class Inputs:
    def __init__(self, bact_input, tem_input, ph_input, start_time, end_time):
        try:
            self.bact_name = bact_input
            self.temp = tem_input
            self.ph = ph_input
            self.start_time = start_time
            self.end_time = end_time
        except ValueError as e:
            print("uncorrected", e)

    @property
    def get_name(self):
        return self.bact_name

    @property
    def get_temp(self):
        return self.temp

    @property
    def get_ph(self):
        return self.ph

    @property
    def get_start_time(self):
        return self.start_time

    @property
    def get_end_time(self):
        return self.end_time


bact_input = str(input("Welke bactrie?"))
tem_input = int(input("Wat is het tempratuur?"))
ph_input = int(input("wat is de ph?"))
start_time = int(input("Wat is de begintijd in uren?"))
end_time = int(input("Wat is de eindtijd in uren?"))


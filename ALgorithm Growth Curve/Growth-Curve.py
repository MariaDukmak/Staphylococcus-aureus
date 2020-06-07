class Values_check(Info_json): #TODO: fix the connection between the classes
    def __init__(self, file_name, user_input, t):
        super().__init__(file_name, user_input, t)
        self.file_name = file_name
        self.user_input = user_input
        self.t = t

    def check(self):
        values = Info_json(self.file_name, self.user_input )
        if (values[2] <= t <= values[1]) or (t == values[0]):
            return [t, values[1]]
        else:
            print("Deze t is ongeldig in de json bestand van de bactrie")



class Logstic:
    pass
class calculate_geowth(Values_check, Logstic):
    def __init__(self, bact_name, temp, ph, start_time, end_time ):
        self.bact_name = bact_name
        self.temp = temp
        self.ph = ph
        self.start_time = start_time
        self.end_time = end_time


class plot_data:
    pass

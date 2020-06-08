from click._compat import raw_input


class Inputs:
    def __init__(self, bact_name, temp, ph, start_time, end_time ):
        try:
            self.bact_name = bact_name
            self.temp = temp
            self.ph = ph
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

bact_name = raw_input('Welke bact?')
temp = int(raw_input('Wat is de temp? '))
ph = int(raw_input('Wat is de ph waarde?'))
start_time = int(raw_input('Wat is de begintijd? '))
end_time = int(raw_input('Wat is de eindtijd? '))


er = Inputs( bact_name, temp, ph, start_time, end_time)
print(er.bact_name)
print(er.get_end_time)


class json_work(Inputs):
    def __init__(self, bact_name, temp, ph, list_tocheck={}):
        super().__init__(bact_name, temp, ph)
        self.list_tocheck = list_tocheck
        list_tocheck['temp']=temp
        list_tocheck["ph"]=ph





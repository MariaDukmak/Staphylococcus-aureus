# def logistic(self, bactName: str, time: int, cFactor: list):
#     # cFactor is the factor that could change the growth rate
#
#     """c is the max : 1000000
#     initial value: we start at 1 so, c/(a+1)= 1 , 1000/(1+a)=1 , a = 999
#     the growth rate: b = 2 -> *could  changes with temperature and pH*
#     time: we start at 0 end at 10 hours"""
#
#     # de beperkende factor moet dat de ie de max temp heeft bereikt
#
#     b = self.read_json(self, bactName, "gr")
#     c = self.read_json(self, bactName, "br")
#     a = c[0] - 1
#     print(b, c, a)
#     # hier moet er goede getallen in komen + dat in de loop van de tijd moet de b wel ++ or --
#     # if len(cFactor) == 1:
#     #     b[0] = b[0]/0.5
#     # if len(cFactor) == 2:
#     #     b[0] = b[0]*2
#     # if len(cFactor) == 3:
#     #     b = b[0] * 2.2
#     list = []
#     for time in range(0, time + 1):
#         list.append(c[0] / (1 + a * np.exp(-b[0] * time)))
#         # list.append(float(a)/(1.0+ np.exp(float(b[0])-(c[0]*time))))# komt van de bron vandaan
#
#     print(list)
#
#     return np.array(list)
#
#
#
#
#
#



########

  # """
  #       c = self.read_json(self, bact_name, "br")
  #       c = c[0]
  #       beginRange=0
  #       eindRange = c+1
  #       list = [0, ]
  #       a = c-1
  #
  #       if factor is not None:
  #           c = self.read_json(self, bact_name, "temp")
  #           if len(c) == 3:
  #               beginRange = c[0]
  #               eindRange = c[2]+1
  #               a = eindRange -1
  #
  #               #optimum?? moeten iets ermee doen
  #           elif len(c) == 2:
  #               beginRange = c[0]
  #               eindRange = c[1] + 1
  #               a = eindRange -1
  #
  #
  #           elif len(c) == 1:
  #               beginRange= c[0]
  #               eindRange = c[0]+1
  #               a = eindRange -1
  #
  #           print(c)
  #
  #
  #
  #
  #       b = self.read_json(self, bact_name, "gr")
  #
  #
  #       for time in range(beginRange,eindRange):
  #           if list[-1] != c:
  #               list.append(c / (1 + a * np.exp(-b[0] * time)))
  #           else:
  #               print(np.array(list))
  #               return np.array(list)

x =[0,0,0]
print(len(x))
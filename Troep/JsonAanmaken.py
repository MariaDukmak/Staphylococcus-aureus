import json
#This is for Staphylococcus aureus bactrie
#gr is de growth rate
#br is de beperkingsfactor

aureus = {
  "name": "s-aureus",
  "info": "Staphylococcus aureus is een stafylokok die toxinen afscheidt en grampositief kleurt.\n De toxinen hebben een negatieve werking op het menselijk lichaam.\n"
          " Staphylococcus aureus zit in 20 tot 30 procent van de gevallen\n op de huid van mens en dier en op de slijmvliezen, zoals de neusholte. \nAls de bacterie door de huid heen het lichaam binnendringt kan deze huidinfecties en \nwondinfectie veroorzaken (ook na operaties), maar ook urineweginfecties,\n longontsteking en bij koeien uierontsteking.De identificatie van \nStaphylococcus aureus gebeurt via een coagulasetest,\n "
          "waarbij de typische Staphylococcus aureus een positief resultaat zal geven,\n in tegenstelling tot andere soorten stafylokokken.\n Atypische varianten kunnen echter ook een negatief resultaat geven bij de coagulasetest.",
  "env-info": {
                "temp": { "temp": 37, "min": 6 , "max": 48},
                "aw":{"aw": "bestaat ffetje niet"},
                "ph": {"ph": [6,7], "min": 4.0, "max":10.0},
                "gr":{"gr":2},
                "br":{"br":1000000000000000000000000000000},


  }
}
with open("../Code/s-aureus.json", "w") as f:
     json.dump(aureus, f)
     f.close()



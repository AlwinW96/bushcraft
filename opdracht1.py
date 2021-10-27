#alwin Wezenbeek 99060433

afstand = float(244)
zuinigheid = float(12)
dieselnodig = float(afstand / zuinigheid)
prijsperpersoon = float(8)
personen = float(5)
prijstotaalpersonen = float(prijsperpersoon * personen)

dieselprijs = float(input('hoeveel kost de diesel nu? '))
totaalprijs = float(dieselnodig * dieselprijs + prijstotaalpersonen)
print('de totaal prijs is: ')
print (totaalprijs)
